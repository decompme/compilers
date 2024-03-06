# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/gcc2.6.3-mipsel

RUN wget -O gcc-2.6.3.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.7/gcc-2.6.3.tar.gz"
RUN tar xvzf gcc-2.6.3.tar.gz -C /compilers/ps1/gcc2.6.3-mipsel

ARG MASPSX_HASH=2c8fc98ab30f2b7a9e6a642cfb76c8c0e610d3f9

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.6.3-mipsel/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler --no-macro-inc -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.6.3-mipsel/

RUN chown -R root:root /compilers/ps1/gcc2.6.3-mipsel/
RUN chmod +x /compilers/ps1/gcc2.6.3-mipsel/*


FROM scratch as release

COPY --from=base /compilers /compilers
