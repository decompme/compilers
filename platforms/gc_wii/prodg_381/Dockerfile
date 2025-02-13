# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gc_wii/prodg_381

RUN wget -O prodg_381.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/prodg_381.tar.gz"
RUN tar xvzf prodg_381.tar.gz -C /compilers/gc_wii/prodg_381

RUN chown -R root:root /compilers/gc_wii/prodg_381/
RUN chmod +x /compilers/gc_wii/prodg_381/*


FROM scratch as release

COPY --from=base /compilers /compilers
