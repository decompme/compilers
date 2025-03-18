# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.7.2sn0001

RUN wget -O n64_sn272_0001.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/n64_sn272_0001.tar.gz"
RUN tar xvzf n64_sn272_0001.tar.gz -C /compilers/n64/gcc2.7.2sn0001
RUN wget -O psyq-obj-parser.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/psyq-obj-parser.tar.gz"
RUN tar xvzf psyq-obj-parser.tar.gz -C /compilers/n64/gcc2.7.2sn0001

RUN chown -R root:root /compilers/n64/gcc2.7.2sn0001/
RUN chmod +x /compilers/n64/gcc2.7.2sn0001/*


FROM scratch as release

COPY --from=base /compilers /compilers
