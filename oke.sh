#!/bin/bash

# Tentukan versi yang ingin diekstrak dari CHANGELOG.md
TAG_VERSION="1.0.1"  # Gantilah dengan versi yang diinginkan

# Cek jika TAG_VERSION adalah "0.1.0", lakukan ekstraksi dengan pola khusus
if [[ "$TAG_VERSION" == "0.1.0" ]]; then
  awk '/^## 0.1.0/,/^$/' CHANGELOG.md
else
  awk -v tag="$TAG_VERSION" '/^## /{p=0} $0 ~ "^## " tag{p=1} p' CHANGELOG.md
fi
