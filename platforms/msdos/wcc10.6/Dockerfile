# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/msdos/wcc10.6

RUN wget -O wcc10.6.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/wcc10.5/wcc10.6.tar.gz"
RUN tar xvzf wcc10.6.tar.gz -C /compilers/msdos/wcc10.6

RUN chown -R root:root /compilers/msdos/wcc10.6/
RUN chmod +x /compilers/msdos/wcc10.6/*


FROM scratch AS release

COPY --from=base /compilers /compilers
