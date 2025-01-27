# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/msdos/bcc3.1

RUN wget -O bcc3.1.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/bcc3.1.tar.gz"
RUN tar xvzf bcc3.1.tar.gz -C /compilers/msdos/bcc3.1

RUN chown -R root:root /compilers/msdos/bcc3.1/
RUN chmod +x /compilers/msdos/bcc3.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
