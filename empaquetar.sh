#!/usr/bin/env bash
# Genera un .zip por skill en dist/ para subirlo a claude.ai
set -e
cd "$(dirname "$0")"
rm -rf dist && mkdir -p dist
for d in plugins/*/skills/*/; do
  n=$(basename "$d")
  (cd "$(dirname "$d")" && zip -qr "$OLDPWD/dist/$n.zip" "$n")
done
ls -1 dist
