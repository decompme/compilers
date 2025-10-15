# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/dreamcast/shc-v5.1r13

RUN wget -O shc-v5.1r13.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/shc-v5.1r13.tar.gz"
RUN tar xvzf shc-v5.1r13.tar.gz -C /compilers/dreamcast/shc-v5.1r13

RUN chown -R root:root /compilers/dreamcast/shc-v5.1r13/
RUN chmod +x /compilers/dreamcast/shc-v5.1r13/*


FROM scratch as release

COPY --from=base /compilers /compilers
