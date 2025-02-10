# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/iop-gcc2.95.2-102

RUN wget -O iop-gcc2.95.2-102.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/iop-gcc2.95.2-102.tar.gz"
RUN tar xvzf iop-gcc2.95.2-102.tar.gz -C /compilers/ps2/iop-gcc2.95.2-102

RUN chown -R root:root /compilers/ps2/iop-gcc2.95.2-102/
RUN chmod +x /compilers/ps2/iop-gcc2.95.2-102/*


FROM scratch as release

COPY --from=base /compilers /compilers
