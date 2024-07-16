# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O armcc.zip "https://github.com/decompme/compilers/releases/download/compilers/armcc.zip"
RUN unzip armcc.zip

RUN mkdir -p /compilers/n3ds/armcc_41_894

RUN cp -r 4.1/b894/* /compilers/n3ds/armcc_41_894

RUN chown -R root:root /compilers/n3ds/armcc_41_894/
RUN chmod +x /compilers/n3ds/armcc_41_894/*


FROM scratch as release

COPY --from=base /compilers /compilers
