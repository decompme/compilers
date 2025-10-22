# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN apk add --no-cache curl libarchive-tools

RUN mkdir compilers \
    && curl -L "https://files.decomp.dev/compilers_20251015.zip" \
    | bsdtar -xvf- -C /compilers


FROM scratch AS release

COPY --from=base /compilers/ProDG/3.8.1 /compilers/gc_wii/prodg_381
