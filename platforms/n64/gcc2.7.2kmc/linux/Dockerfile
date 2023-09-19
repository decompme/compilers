# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.7.2kmc

RUN wget -O gcc-2.7.2-linux.tar.gz "https://github.com/decompals/mips-gcc-2.7.2/releases/download/main/gcc-2.7.2-linux.tar.gz"
RUN tar xvzf gcc-2.7.2-linux.tar.gz -C /compilers/n64/gcc2.7.2kmc
RUN wget -O binutils-2.6-linux.tar.gz "https://github.com/decompals/mips-binutils-2.6/releases/download/main/binutils-2.6-linux.tar.gz"
RUN tar xvzf binutils-2.6-linux.tar.gz -C /compilers/n64/gcc2.7.2kmc

RUN chown -R root:root /compilers/n64/gcc2.7.2kmc/
RUN chmod +x /compilers/n64/gcc2.7.2kmc/*


FROM scratch as release

COPY --from=base /compilers /compilers
