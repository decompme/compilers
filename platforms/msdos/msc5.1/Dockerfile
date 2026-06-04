# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/msdos/msc5.1

RUN wget -O msc-5.1.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/msc-5.1.tar.gz"
RUN tar xvzf msc-5.1.tar.gz -C /compilers/msdos/msc5.1

RUN chown -R root:root /compilers/msdos/msc5.1/
RUN chmod +x /compilers/msdos/msc5.1/*


FROM scratch AS release

COPY --from=base /compilers /compilers
