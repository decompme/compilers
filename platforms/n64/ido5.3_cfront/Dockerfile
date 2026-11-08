# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ido5.3_cfront

RUN wget -O ido5.3_cfront.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ido5.3_cfront.tar.gz"
RUN tar xvzf ido5.3_cfront.tar.gz -C /compilers/n64/ido5.3_cfront

RUN chown -R root:root /compilers/n64/ido5.3_cfront/
RUN chmod +x /compilers/n64/ido5.3_cfront/*


FROM scratch AS release

COPY --from=base /compilers /compilers
