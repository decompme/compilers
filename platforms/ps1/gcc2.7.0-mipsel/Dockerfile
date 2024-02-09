# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/gcc2.7.0-mipsel

RUN wget -O gcc-2.7.0.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.7/gcc-2.7.0.tar.gz"
RUN tar xvzf gcc-2.7.0.tar.gz -C /compilers/ps1/gcc2.7.0-mipsel

ARG MASPSX_HASH=7c1efd5d0cd597a170a6c5dbf3d17576d99bc45c

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.7.0-mipsel/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler --no-macro-inc -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.7.0-mipsel/

RUN chown -R root:root /compilers/ps1/gcc2.7.0-mipsel/
RUN chmod +x /compilers/ps1/gcc2.7.0-mipsel/*


FROM scratch as release

COPY --from=base /compilers /compilers
