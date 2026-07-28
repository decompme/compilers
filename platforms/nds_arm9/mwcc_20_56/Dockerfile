# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/nds_arm9/mwcc_20_56

RUN wget -O mwcc_20_56.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwcc_20_56.tar.gz"
RUN tar xvzf mwcc_20_56.tar.gz -C /compilers/nds_arm9/mwcc_20_56

RUN chown -R root:root /compilers/nds_arm9/mwcc_20_56/
RUN chmod +x /compilers/nds_arm9/mwcc_20_56/*


FROM scratch AS release

COPY --from=base /compilers /compilers
