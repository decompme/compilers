# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/ps1/gcc2.7.2.1-mipsel

RUN wget -O gcc-2.7.2.1.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.7/gcc-2.7.2.1.tar.gz"
RUN tar xvzf gcc-2.7.2.1.tar.gz -C /compilers/ps1/gcc2.7.2.1-mipsel

ARG MASPSX_HASH=9e4733d051c4d22a6848358e269017efabed9c8b

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.7.2.1-mipsel/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.7.2.1-mipsel/

RUN chown -R root:root /compilers/ps1/gcc2.7.2.1-mipsel/
RUN chmod +x /compilers/ps1/gcc2.7.2.1-mipsel/*


FROM scratch AS release

COPY --from=base /compilers /compilers
