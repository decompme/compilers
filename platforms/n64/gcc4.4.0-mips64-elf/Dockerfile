# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc4.4.0-mips64-elf

RUN wget -O gcc4.4.0-mips64-elf.tar.gz "https://github.com/devwizard64/gcc4.4.0-mips64-elf/releases/download/latest/gcc4.4.0-mips64-elf.tar.gz"
RUN tar xvzf gcc4.4.0-mips64-elf.tar.gz -C /compilers/n64/gcc4.4.0-mips64-elf

RUN chown -R root:root /compilers/n64/gcc4.4.0-mips64-elf/
RUN chmod +x /compilers/n64/gcc4.4.0-mips64-elf/*


FROM scratch as release

COPY --from=base /compilers /compilers
