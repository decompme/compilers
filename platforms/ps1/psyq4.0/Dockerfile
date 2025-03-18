# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/psyq4.0

RUN wget -O psyq4.0.tar.gz "https://github.com/mkst/esa/releases/download/psyq-binaries/psyq4.0.tar.gz"
RUN tar xvzf psyq4.0.tar.gz --strip-components=1 -C /compilers/ps1/psyq4.0

RUN wget -O psyq-obj-parser.tar.gz https://github.com/decompme/compilers/releases/download/compilers/psyq-obj-parser.tar.gz?2025-03-18
RUN tar xvzf psyq-obj-parser.tar.gz -C /compilers/ps1/psyq4.0/

RUN chown -R root:root /compilers/ps1/psyq4.0/
RUN chmod +x /compilers/ps1/psyq4.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
