# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/wiiu/ghs5.3.22

RUN wget -O ghs5.3.22.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ghs5.3.22.tar.gz"
RUN tar xvzf ghs5.3.22.tar.gz -C /compilers/wiiu/ghs5.3.22

RUN chown -R root:root /compilers/wiiu/ghs5.3.22/
RUN chmod +x /compilers/wiiu/ghs5.3.22/*


FROM scratch AS release

COPY --from=base /compilers /compilers
