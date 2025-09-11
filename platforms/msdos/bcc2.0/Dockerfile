# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/msdos/bcc2.0

RUN wget -O bcc2.0.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/bcc2.0.tar.gz"
RUN tar xvzf bcc2.0.tar.gz -C /compilers/msdos/bcc2.0

RUN chown -R root:root /compilers/msdos/bcc2.0/
RUN chmod +x /compilers/msdos/bcc2.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
