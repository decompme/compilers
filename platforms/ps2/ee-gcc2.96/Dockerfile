# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.96

RUN wget -O ee-gcc2.96.tar.xz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.96.tar.xz"
RUN tar xvJf ee-gcc2.96.tar.xz -C /compilers/ps2/ee-gcc2.96

RUN chown -R root:root /compilers/ps2/ee-gcc2.96/
RUN chmod +x /compilers/ps2/ee-gcc2.96/*


FROM scratch as release

COPY --from=base /compilers /compilers
