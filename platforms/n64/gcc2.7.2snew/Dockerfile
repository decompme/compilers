# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.7.2snew

RUN wget -O SN64-gcc-2.7.2-970404-linux.tar.gz "https://github.com/decompals/SN64-gcc/releases/download/gcc-2.7.2-970404/SN64-gcc-2.7.2-970404-linux.tar.gz"
RUN tar xvzf SN64-gcc-2.7.2-970404-linux.tar.gz -C /compilers/n64/gcc2.7.2snew
RUN wget -O /compilers/n64/gcc2.7.2snew/modern-asn64.py "https://github.com/RocketRet/modern-asn64/releases/download/main-release/modern-asn64.py"

RUN chown -R root:root /compilers/n64/gcc2.7.2snew/
RUN chmod +x /compilers/n64/gcc2.7.2snew/*


FROM scratch as release

COPY --from=base /compilers /compilers
