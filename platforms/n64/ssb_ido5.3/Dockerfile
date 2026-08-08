# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ssb_ido5.3

RUN wget -O /compilers/n64/ssb_ido5.3/ssb_ido5.3.tar "https://github.com/LLONSIT/qemu-irix-helpers/raw/refs/heads/n/qemu/ssb_ido5.3.tar"

RUN chown -R root:root /compilers/n64/ssb_ido5.3/
RUN chmod +x /compilers/n64/ssb_ido5.3/*


FROM scratch AS release

COPY --from=base /compilers /compilers
