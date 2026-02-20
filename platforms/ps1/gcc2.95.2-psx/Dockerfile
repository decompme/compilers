# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/ps1/gcc2.95.2-psx

RUN wget -O gcc-2.95.2-psx.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.12/gcc-2.95.2-psx.tar.gz"
RUN tar xvzf gcc-2.95.2-psx.tar.gz -C /compilers/ps1/gcc2.95.2-psx

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/cae9594f3e8fa76e2255c4624da4584364a37c27.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-cae9594f3e8fa76e2255c4624da4584364a37c27 /compilers/ps1/gcc2.95.2-psx/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.95.2-psx/

RUN chown -R root:root /compilers/ps1/gcc2.95.2-psx/
RUN chmod +x /compilers/ps1/gcc2.95.2-psx/*


FROM scratch AS release

COPY --from=base /compilers /compilers
