# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.8.1sn

RUN wget -O /compilers/n64/gcc2.8.1sn/asn64.exe "https://github.com/marijnvdwerf/sn64/releases/download/1%2C0%2C0%2C2/asn64.exe"
RUN wget -O /compilers/n64/gcc2.8.1sn/cc1n64.exe "https://github.com/marijnvdwerf/sn64/releases/download/1%2C0%2C0%2C2/cc1n64.exe"
RUN wget -O /compilers/n64/gcc2.8.1sn/cc1pln64.exe "https://github.com/marijnvdwerf/sn64/releases/download/1%2C0%2C0%2C2/cc1pln64.exe"
RUN wget -O psyq-obj-parser.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/psyq-obj-parser.tar.gz"
RUN tar xvzf psyq-obj-parser.tar.gz -C /compilers/n64/gcc2.8.1sn

RUN chown -R root:root /compilers/n64/gcc2.8.1sn/
RUN chmod +x /compilers/n64/gcc2.8.1sn/*


FROM scratch as release

COPY --from=base /compilers /compilers
