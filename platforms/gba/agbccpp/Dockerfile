# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gba/agbccpp

RUN wget -O agbcc.tar.gz "https://github.com/notyourav/agbcc/releases/download/cp/agbcc.tar.gz"
RUN tar xvzf agbcc.tar.gz -C /compilers/gba/agbccpp

RUN chown -R root:root /compilers/gba/agbccpp/
RUN chmod +x /compilers/gba/agbccpp/*


FROM scratch as release

COPY --from=base /compilers /compilers
