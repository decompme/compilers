# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download xz first to allow for Docker caching

WORKDIR /root

RUN wget -O mwcps2-3.0b38-030307.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwcps2-3.0b38-030307.tar.gz"
RUN tar xvJf mwcps2-3.0b38-030307.tar.gz

RUN mkdir -p /compilers/ps2/mwcps2-3.0b38-030307

RUN cp -r mwcps2-3.0b38-030307/* /compilers/ps2/mwcps2-3.0b38-030307

RUN chown -R root:root /compilers/ps2/mwcps2-3.0b38-030307/
RUN chmod +x /compilers/ps2/mwcps2-3.0b38-030307/*


FROM scratch as release

COPY --from=base /compilers /compilers
