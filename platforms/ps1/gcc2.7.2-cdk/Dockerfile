# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/ps1/gcc2.7.2-cdk

RUN wget -O gcc-2.7.2-cdk.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.14/gcc-2.7.2-cdk.tar.gz"
RUN tar xvzf gcc-2.7.2-cdk.tar.gz -C /compilers/ps1/gcc2.7.2-cdk

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/3f4dd438f25de92745ec9fec991263639ce92821.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-3f4dd438f25de92745ec9fec991263639ce92821 /compilers/ps1/gcc2.7.2-cdk/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.7.2-cdk/

RUN chown -R root:root /compilers/ps1/gcc2.7.2-cdk/
RUN chmod +x /compilers/ps1/gcc2.7.2-cdk/*


FROM scratch AS release

COPY --from=base /compilers /compilers
