# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ido5.2

RUN wget -O ido5.2.tar.xz "https://github.com/LLONSIT/qemu-irix-helpers/raw/refs/heads/n/qemu/ido5.2.tar.xz"
RUN tar xvJf ido5.2.tar.xz -C /compilers/n64/ido5.2

RUN chown -R root:root /compilers/n64/ido5.2/
RUN chmod +x /compilers/n64/ido5.2/*


FROM scratch AS release

COPY --from=base /compilers /compilers
