# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/ps1/gcc2.6.0-psx

RUN wget -O gcc-2.6.0-psx.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.12/gcc-2.6.0-psx.tar.gz"
RUN tar xvzf gcc-2.6.0-psx.tar.gz -C /compilers/ps1/gcc2.6.0-psx

ARG MASPSX_HASH=9e4733d051c4d22a6848358e269017efabed9c8b

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/b0f897d1267bd78530a1501320ca989e7bc2483e.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-b0f897d1267bd78530a1501320ca989e7bc2483e /compilers/ps1/gcc2.6.0-psx/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.6.0-psx/

RUN chown -R root:root /compilers/ps1/gcc2.6.0-psx/
RUN chmod +x /compilers/ps1/gcc2.6.0-psx/*


FROM scratch AS release

COPY --from=base /compilers /compilers
