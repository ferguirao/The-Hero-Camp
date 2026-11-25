#!/usr/bin/env python3
"""Busca y descarga fotos libres (Pexels, Unsplash, Pixabay) para las slides.

Claves (en .env en la raíz del repo, o como variables de entorno; gratis en cada web): PEXELS_API_KEY, UNSPLASH_ACCESS_KEY, PIXABAY_KEY.

Buscar:    python3 scripts/buscar-imagen.py "audience raised hands" --fuente pexels --orientacion landscape --n 6
Descargar: python3 scripts/buscar-imagen.py --descargar pexels:12345 --a cursos/<curso>/sesiones/<s>/assets/nombre.jpg

Al descargar, añade una línea de crédito en ORIGEN.md junto al archivo.
"""
import argparse, json, os, sys, urllib.parse, urllib.request, datetime

UA = {"User-Agent": "course-builder/1.0"}


def cargar_env():
    """Lee las claves de .env (en la raíz del repo, ignorado por Git) sin pisar las que ya estén en el entorno."""
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    if os.path.isfile(ruta):
        for linea in open(ruta, encoding="utf-8"):
            linea = linea.strip()
            if linea and not linea.startswith("#") and "=" in linea:
                k, v = linea.split("=", 1)
                if v.strip():
                    os.environ.setdefault(k.strip(), v.strip())


cargar_env()


def get(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def clave(nombre):
    v = os.environ.get(nombre)
    if not v:
        sys.exit(f"Falta la variable de entorno {nombre}. Es gratis: regístrate en la web de la biblioteca (ver .claude/skills/imagenes-thc/SKILL.md).")
    return v


def buscar(fuente, q, orient, n):
    if fuente == "pexels":
        d = json.loads(get("https://api.pexels.com/v1/search?" + urllib.parse.urlencode({"query": q, "per_page": n, "orientation": orient}), {"Authorization": clave("PEXELS_API_KEY")}))
        return [(f"pexels:{p['id']}", p["photographer"], p["url"], f"{p['width']}x{p['height']}") for p in d["photos"]]
    if fuente == "unsplash":
        o = {"landscape": "landscape", "portrait": "portrait", "square": "squarish"}[orient]
        d = json.loads(get("https://api.unsplash.com/search/photos?" + urllib.parse.urlencode({"query": q, "per_page": n, "orientation": o}), {"Authorization": "Client-ID " + clave("UNSPLASH_ACCESS_KEY")}))
        return [(f"unsplash:{p['id']}", p["user"]["name"], p["links"]["html"], f"{p['width']}x{p['height']}") for p in d["results"]]
    if fuente == "pixabay":
        o = {"landscape": "horizontal", "portrait": "vertical", "square": "all"}[orient]
        d = json.loads(get("https://pixabay.com/api/?" + urllib.parse.urlencode({"key": clave("PIXABAY_KEY"), "q": q, "per_page": max(n, 3), "orientation": o, "image_type": "photo"})))
        return [(f"pixabay:{p['id']}", p["user"], p["pageURL"], f"{p['imageWidth']}x{p['imageHeight']}") for p in d["hits"][:n]]
    sys.exit("Fuente desconocida: usa pexels, unsplash o pixabay")


def descargar(ref, destino):
    fuente, id_ = ref.split(":", 1)
    if fuente == "pexels":
        p = json.loads(get(f"https://api.pexels.com/v1/photos/{id_}", {"Authorization": clave("PEXELS_API_KEY")}))
        url, autor, pagina, lic = p["src"]["large2x"], p["photographer"], p["url"], "Pexels License"
    elif fuente == "unsplash":
        k = clave("UNSPLASH_ACCESS_KEY")
        p = json.loads(get(f"https://api.unsplash.com/photos/{id_}", {"Authorization": "Client-ID " + k}))
        url, autor, pagina, lic = p["urls"]["regular"], p["user"]["name"], p["links"]["html"], "Unsplash License"
        get(p["links"]["download_location"], {"Authorization": "Client-ID " + k})  # la API de Unsplash exige registrar la descarga
    elif fuente == "pixabay":
        p = json.loads(get("https://pixabay.com/api/?" + urllib.parse.urlencode({"key": clave("PIXABAY_KEY"), "id": id_})))["hits"][0]
        url, autor, pagina, lic = p["largeImageURL"], p["user"], p["pageURL"], "Pixabay Content License"
    else:
        sys.exit("Fuente desconocida")
    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    open(destino, "wb").write(get(url))
    origen = os.path.join(os.path.dirname(destino) or ".", "ORIGEN.md")
    with open(origen, "a", encoding="utf-8") as f:
        f.write(f"- `{os.path.basename(destino)}`: {autor}, {pagina} ({lic}, {datetime.date.today()})\n")
    print(f"Guardada en {destino}; crédito añadido a {origen}")


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("consulta", nargs="?")
    a.add_argument("--fuente", default="pexels")
    a.add_argument("--orientacion", default="landscape", choices=["landscape", "portrait", "square"])
    a.add_argument("--n", type=int, default=6)
    a.add_argument("--descargar")
    a.add_argument("--a")
    x = a.parse_args()
    if x.descargar:
        if not x.a:
            sys.exit("Indica el destino con --a")
        descargar(x.descargar, x.a)
    elif x.consulta:
        for r in buscar(x.fuente, x.consulta, x.orientacion, x.n):
            print(" | ".join(r))
    else:
        a.print_help()
