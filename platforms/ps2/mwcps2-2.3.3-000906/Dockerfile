# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/mwcps2-2.3.3-000906

RUN wget -O mwcps2-2.3.3-000906.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwcps2-2.3.3-000906.tar.gz"
RUN tar xvzf mwcps2-2.3.3-000906.tar.gz -C /compilers/ps2/mwcps2-2.3.3-000906

RUN chown -R root:root /compilers/ps2/mwcps2-2.3.3-000906/
RUN chmod +x /compilers/ps2/mwcps2-2.3.3-000906/*


FROM scratch as release

COPY --from=base /compilers /compilers
