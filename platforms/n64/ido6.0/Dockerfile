# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/ido6.0

RUN wget -O ido6.0.tar.xz "https://github.com/LLONSIT/qemu-irix-helpers/raw/n/qemu/ido6.0.tar.xz"
RUN tar xvJf ido6.0.tar.xz -C /compilers/n64/ido6.0

RUN chown -R root:root /compilers/n64/ido6.0/
RUN chmod +x /compilers/n64/ido6.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
