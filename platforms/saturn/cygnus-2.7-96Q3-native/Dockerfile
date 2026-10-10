# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/saturn/cygnus-2.7-96Q3-native

RUN wget -O cc1-native.tar.gz "https://github.com/sozud/saturn-compiler-repro/releases/download/v1.0.0/cc1-native.tar.gz"
RUN tar xvzf cc1-native.tar.gz -C /compilers/saturn/cygnus-2.7-96Q3-native

RUN chown -R root:root /compilers/saturn/cygnus-2.7-96Q3-native/
RUN chmod +x /compilers/saturn/cygnus-2.7-96Q3-native/*


FROM scratch AS release

COPY --from=base /compilers /compilers
