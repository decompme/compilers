# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps1/psyq4.6

RUN wget -O psyq4.6.tar.gz "https://github.com/mkst/esa/releases/download/psyq-binaries/psyq4.6.tar.gz"
RUN tar xvzf psyq4.6.tar.gz --strip-components=1 -C /compilers/ps1/psyq4.6

RUN wget -O psyq-obj-parser.tar.gz https://github.com/mkst/esa/releases/download/psyq-binaries/psyq-obj-parser.tar.gz
RUN tar xvzf psyq-obj-parser.tar.gz -C /compilers/ps1/psyq4.6/

RUN chown -R root:root /compilers/ps1/psyq4.6/
RUN chmod +x /compilers/ps1/psyq4.6/*


FROM scratch as release

COPY --from=base /compilers /compilers
