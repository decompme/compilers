# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.7.2sn

RUN wget -O /compilers/n64/gcc2.7.2sn/asn64.exe "https://github.com/Mr-Wiseguy/pcsx-redux/releases/download/n64/asn64.exe"
RUN wget -O /compilers/n64/gcc2.7.2sn/cc1n64.exe "https://github.com/Mr-Wiseguy/pcsx-redux/releases/download/n64/cc1n64.exe"
RUN wget -O /compilers/n64/gcc2.7.2sn/psyq-obj-parser "https://github.com/Mr-Wiseguy/pcsx-redux/releases/download/n64/psyq-obj-parser"

RUN chown -R root:root /compilers/n64/gcc2.7.2sn/
RUN chmod +x /compilers/n64/gcc2.7.2sn/*


FROM scratch as release

COPY --from=base /compilers /compilers
