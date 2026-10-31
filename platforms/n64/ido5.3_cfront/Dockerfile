# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/n64/ido5.3_cfront

RUN wget -O ido5.3_cfront.tar.xz "https://github.com/LLONSIT/qemu-irix-helpers/raw/n/qemu/ido5.3_cfront.tar.xz?2024-03-03"
RUN tar xvJf ido5.3_cfront.tar.xz -C /compilers/n64/ido5.3_cfront

RUN chown -R root:root /compilers/n64/ido5.3_cfront/
RUN chmod +x /compilers/n64/ido5.3_cfront/*


FROM scratch AS release

COPY --from=base /compilers /compilers
