# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/gba/gcc2.96

RUN wget -O gcc-2.96-20000731-armelf.tar.gz "https://github.com/SBird1337/camelot-gcc/releases/download/2.96/gcc-2.96-20000731-armelf.tar.gz"
RUN tar xvzf gcc-2.96-20000731-armelf.tar.gz -C /compilers/gba/gcc2.96

RUN chown -R root:root /compilers/gba/gcc2.96/
RUN chmod +x /compilers/gba/gcc2.96/*


FROM scratch AS release

COPY --from=base /compilers /compilers
