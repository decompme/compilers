# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# Copy of common/decomp.dev with legacy support for frank.py

RUN apk add --no-cache curl libarchive-tools

RUN mkdir compilers \
    && curl -L "https://files.decomp.dev/compilers_20240706.zip" \
    | bsdtar -xvf- -C /compilers


ARG FRANK_HASH=d19668657d2a5efa42cdffb801090d05734b9dbd
RUN wget -O /compilers/GC/1.2.5e/frank.py https://raw.githubusercontent.com/doldecomp/melee/${FRANK_HASH}/tools/frank.py
RUN cp -r /compilers/GC/1.2.5/mwcceppc.exe /compilers/GC/1.2.5e/mwcceppc.125.exe


FROM scratch AS release

COPY --from=base /compilers/GC/1.2.5e /compilers/gc_wii/mwcc_233_163e
