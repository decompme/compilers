# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/psp/psp-gcc-1.3.1

RUN wget -O psp-gcc-1.3.1.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/psp-gcc-1.3.1.tar.gz?2024-04-25"
RUN tar xvzf psp-gcc-1.3.1.tar.gz -C /compilers/psp/psp-gcc-1.3.1

RUN chown -R root:root /compilers/psp/psp-gcc-1.3.1/
RUN chmod +x /compilers/psp/psp-gcc-1.3.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
