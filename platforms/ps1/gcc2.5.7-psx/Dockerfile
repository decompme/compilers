# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/gcc2.5.7-psx

RUN wget -O gcc-2.5.7-psx.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.8/gcc-2.5.7-psx.tar.gz"
RUN tar xvzf gcc-2.5.7-psx.tar.gz -C /compilers/ps1/gcc2.5.7-psx

ARG MASPSX_HASH=f92df17f5c564b5df9fa07908d50899c291c3c5d

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/${MASPSX_HASH}.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-${MASPSX_HASH} /compilers/ps1/gcc2.5.7-psx/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler --no-macro-inc -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.5.7-psx/

RUN chown -R root:root /compilers/ps1/gcc2.5.7-psx/
RUN chmod +x /compilers/ps1/gcc2.5.7-psx/*


FROM scratch as release

COPY --from=base /compilers /compilers
