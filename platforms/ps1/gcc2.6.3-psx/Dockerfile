# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/gcc2.6.3-psx

RUN wget -O gcc-2.6.3-psx.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.12/gcc-2.6.3-psx.tar.gz"
RUN tar xvzf gcc-2.6.3-psx.tar.gz -C /compilers/ps1/gcc2.6.3-psx

ARG MASPSX_HASH=fc6d220e1baf4bc4d52efcd3710cc44e445c5ca8

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.6.3-psx/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.6.3-psx/

RUN chown -R root:root /compilers/ps1/gcc2.6.3-psx/
RUN chmod +x /compilers/ps1/gcc2.6.3-psx/*


FROM scratch as release

COPY --from=base /compilers /compilers
