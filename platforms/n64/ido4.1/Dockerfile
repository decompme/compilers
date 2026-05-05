# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ido4.1

RUN wget -O ido4.1.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ido4.1.tar.gz"
RUN tar xvzf ido4.1.tar.gz -C /compilers/n64/ido4.1

RUN chown -R root:root /compilers/n64/ido4.1/
RUN chmod +x /compilers/n64/ido4.1/*


FROM scratch AS release

COPY --from=base /compilers /compilers
