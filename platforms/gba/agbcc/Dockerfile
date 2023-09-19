# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gba/agbcc

RUN wget -O agbcc.tar.gz "https://github.com/pret/agbcc/releases/download/release/agbcc.tar.gz"
RUN tar xvzf agbcc.tar.gz -C /compilers/gba/agbcc

RUN chown -R root:root /compilers/gba/agbcc/
RUN chmod +x /compilers/gba/agbcc/*


FROM scratch as release

COPY --from=base /compilers /compilers
