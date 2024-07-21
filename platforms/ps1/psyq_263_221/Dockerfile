# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/psyq_263_221

RUN wget -O psyq_263_221.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/psyq_263_221.tar.gz"
RUN tar xvzf psyq_263_221.tar.gz -C /compilers/ps1/psyq_263_221

RUN chown -R root:root /compilers/ps1/psyq_263_221/
RUN chmod +x /compilers/ps1/psyq_263_221/*


FROM scratch as release

COPY --from=base /compilers /compilers
