# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/ido4.1

RUN wget -O ido4.1.tar.xz "https://github.com/LLONSIT/qemu-irix-helpers/raw/refs/heads/n/qemu/ido4.1.tar.xz"
RUN tar xvJf ido4.1.tar.xz -C /compilers/n64/ido4.1

RUN chown -R root:root /compilers/n64/ido4.1/
RUN chmod +x /compilers/n64/ido4.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
