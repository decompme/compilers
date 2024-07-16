# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O armcc.zip "https://github.com/decompme/compilers/releases/download/compilers/armcc.zip"
RUN unzip armcc.zip

RUN mkdir -p /compilers/n3ds/armcc_41_921

RUN cp -r 4.1/b921/* /compilers/n3ds/armcc_41_921

RUN chown -R root:root /compilers/n3ds/armcc_41_921/
RUN chmod +x /compilers/n3ds/armcc_41_921/*


FROM scratch as release

COPY --from=base /compilers /compilers
