# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.7.2sn0004

RUN wget -O /compilers/n64/gcc2.7.2sn0004/asn64.exe "https://github.com/Mr-Wiseguy/pcsx-redux/releases/download/n64/asn64.exe"
RUN wget -O /compilers/n64/gcc2.7.2sn0004/cc1n64.exe "https://github.com/Mr-Wiseguy/pcsx-redux/releases/download/n64/cc1n64.exe"
RUN wget -O psyq-obj-parser.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/psyq-obj-parser.tar.gz"
RUN tar xvzf psyq-obj-parser.tar.gz -C /compilers/n64/gcc2.7.2sn0004

RUN chown -R root:root /compilers/n64/gcc2.7.2sn0004/
RUN chmod +x /compilers/n64/gcc2.7.2sn0004/*


FROM scratch as release

COPY --from=base /compilers /compilers
