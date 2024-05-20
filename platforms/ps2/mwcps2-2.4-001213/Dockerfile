# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/mwcps2-2.4-001213

RUN wget -O mwcps2-2.4-001213.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwcps2-2.4-001213.tar.gz"
RUN tar xvzf mwcps2-2.4-001213.tar.gz -C /compilers/ps2/mwcps2-2.4-001213

RUN chown -R root:root /compilers/ps2/mwcps2-2.4-001213/
RUN chmod +x /compilers/ps2/mwcps2-2.4-001213/*


FROM scratch as release

COPY --from=base /compilers /compilers
