# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/gba/agbcc-fe8j

RUN wget -O agbcc.tar.gz "https://github.com/laqieer/agbcc/releases/download/fe8j-v1/agbcc.tar.gz"
RUN tar xvzf agbcc.tar.gz -C /compilers/gba/agbcc-fe8j

RUN chown -R root:root /compilers/gba/agbcc-fe8j/
RUN chmod +x /compilers/gba/agbcc-fe8j/*


FROM scratch AS release

COPY --from=base /compilers /compilers
