# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/msdos/wcc10.0a

RUN wget -O wcc10.0a.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/wcc10.0a.tar.gz"
RUN tar xvzf wcc10.0a.tar.gz -C /compilers/msdos/wcc10.0a

RUN chown -R root:root /compilers/msdos/wcc10.0a/
RUN chmod +x /compilers/msdos/wcc10.0a/*


FROM scratch AS release

COPY --from=base /compilers /compilers
