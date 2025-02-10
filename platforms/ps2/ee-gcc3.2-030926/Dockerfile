# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc3.2-030926

RUN wget -O ee-gcc3.2-030926.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc3.2-030926.tar.gz"
RUN tar xvzf ee-gcc3.2-030926.tar.gz -C /compilers/ps2/ee-gcc3.2-030926

RUN chown -R root:root /compilers/ps2/ee-gcc3.2-030926/
RUN chmod +x /compilers/ps2/ee-gcc3.2-030926/*


FROM scratch as release

COPY --from=base /compilers /compilers
