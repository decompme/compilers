# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gc_wii/prodg_37

RUN wget -O ProDG-v3.7.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ProDG-v3.7.tar.gz"
RUN tar xvzf ProDG-v3.7.tar.gz --strip-components=1 -C /compilers/gc_wii/prodg_37

RUN chown -R root:root /compilers/gc_wii/prodg_37/
RUN chmod +x /compilers/gc_wii/prodg_37/*


FROM scratch as release

COPY --from=base /compilers /compilers
