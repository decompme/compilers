# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ssb_ido7.1

RUN wget -O /compilers/n64/ssb_ido7.1/ssb_ido7.1.tar "https://github.com/LLONSIT/qemu-irix-helpers/raw/refs/heads/n/qemu/ssb_ido7.1.tar"

RUN chown -R root:root /compilers/n64/ssb_ido7.1/
RUN chmod +x /compilers/n64/ssb_ido7.1/*


FROM scratch AS release

COPY --from=base /compilers /compilers
