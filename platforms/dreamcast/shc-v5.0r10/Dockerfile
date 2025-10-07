# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/dreamcast/shc-v5.0r10

RUN wget -O shc-v5.0r10.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/shc-v5.0r10.tar.gz"
RUN tar xvzf shc-v5.0r10.tar.gz -C /compilers/dreamcast/shc-v5.0r10

RUN chown -R root:root /compilers/dreamcast/shc-v5.0r10/
RUN chmod +x /compilers/dreamcast/shc-v5.0r10/*


FROM scratch as release

COPY --from=base /compilers /compilers
