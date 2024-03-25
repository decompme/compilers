# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/mwcps2-3.0.1-020123

RUN wget -O mwcps2-3.0.1-020123.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwcps2-3.0.1-020123.tar.gz"
RUN tar xvzf mwcps2-3.0.1-020123.tar.gz -C /compilers/ps2/mwcps2-3.0.1-020123
RUN wget -O binutils-mips-ps2-decompals-linux-x86-64.tar.gz "https://github.com/decompals/binutils-mips-ps2-decompals/releases/download/v0.1/binutils-mips-ps2-decompals-linux-x86-64.tar.gz"
RUN tar xvzf binutils-mips-ps2-decompals-linux-x86-64.tar.gz -C /compilers/ps2/mwcps2-3.0.1-020123

RUN chown -R root:root /compilers/ps2/mwcps2-3.0.1-020123/
RUN chmod +x /compilers/ps2/mwcps2-3.0.1-020123/*


FROM scratch as release

COPY --from=base /compilers /compilers
