# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gc_wii/prodg_35_b140

RUN wget -O prodg_35_b140.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/prodg_35_b140.tar.gz"
RUN tar xvzf prodg_35_b140.tar.gz -C /compilers/gc_wii/prodg_35_b140

RUN chown -R root:root /compilers/gc_wii/prodg_35_b140/
RUN chmod +x /compilers/gc_wii/prodg_35_b140/*


FROM scratch as release

COPY --from=base /compilers /compilers
