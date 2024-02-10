# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/psp/pspsnc_1.2.7503.0

RUN wget -O pspsnc_1.2.7503.0.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/pspsnc_1.2.7503.0.tar.gz"
RUN tar xvzf pspsnc_1.2.7503.0.tar.gz -C /compilers/psp/pspsnc_1.2.7503.0

RUN chown -R root:root /compilers/psp/pspsnc_1.2.7503.0/
RUN chmod +x /compilers/psp/pspsnc_1.2.7503.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
