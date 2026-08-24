# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/ps1/gcc2.6.0-mipsel

RUN wget -O gcc-2.6.0.tar.gz "https://github.com/decompals/old-gcc/releases/download/0.7/gcc-2.6.0.tar.gz"
RUN tar xvzf gcc-2.6.0.tar.gz -C /compilers/ps1/gcc2.6.0-mipsel

RUN wget -O maspsx.zip https://github.com/mkst/maspsx/archive/025620f1e61248ad4a775c2929ec86f754973597.zip
RUN unzip maspsx.zip
RUN cp -r maspsx-025620f1e61248ad4a775c2929ec86f754973597 /compilers/ps1/gcc2.6.0-mipsel/maspsx

RUN echo '#!/bin/bash' >> as
RUN echo 'python3 $(dirname -- $0)/maspsx/maspsx.py --run-assembler -I${COMPILER_DIR} $@' >> as
RUN cp as /compilers/ps1/gcc2.6.0-mipsel/

RUN chown -R root:root /compilers/ps1/gcc2.6.0-mipsel/
RUN chmod +x /compilers/ps1/gcc2.6.0-mipsel/*


FROM scratch AS release

COPY --from=base /compilers /compilers
