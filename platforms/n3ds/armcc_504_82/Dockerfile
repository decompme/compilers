# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O armcc.zip "https://cdn.discordapp.com/attachments/710646040792924172/1148006502980927528/armcc.zip"
RUN unzip armcc.zip

RUN mkdir -p /compilers/n3ds/armcc_504_82

RUN cp -r 5.04/b82/* /compilers/n3ds/armcc_504_82

RUN chown -R root:root /compilers/n3ds/armcc_504_82/
RUN chmod +x /compilers/n3ds/armcc_504_82/*


FROM scratch as release

COPY --from=base /compilers /compilers
