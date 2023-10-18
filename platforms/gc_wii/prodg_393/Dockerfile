# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gc_wii/prodg_393

RUN wget -O ProDG-v3.9.3.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ProDG-v3.9.3.tar.gz"
RUN tar xvzf ProDG-v3.9.3.tar.gz --strip-components=1 -C /compilers/gc_wii/prodg_393

RUN chown -R root:root /compilers/gc_wii/prodg_393/
RUN chmod +x /compilers/gc_wii/prodg_393/*


FROM scratch as release

COPY --from=base /compilers /compilers
