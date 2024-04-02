# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/gcc2.5.7-mipsel

RUN wget -O gcc-2.5.7.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.7/gcc-2.5.7.tar.gz"
RUN tar xvzf gcc-2.5.7.tar.gz -C /compilers/ps1/gcc2.5.7-mipsel

ARG MASPSX_HASH=d2d75a1686f397b549216f1f09d7b16265394281

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.5.7-mipsel/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.5.7-mipsel/

RUN chown -R root:root /compilers/ps1/gcc2.5.7-mipsel/
RUN chmod +x /compilers/ps1/gcc2.5.7-mipsel/*


FROM scratch as release

COPY --from=base /compilers /compilers
