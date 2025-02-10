# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc3.2-030210-beta2

RUN wget -O ee-gcc3.2-030210-beta2.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc3.2-030210-beta2.tar.gz?2025-02-10"
RUN tar xvzf ee-gcc3.2-030210-beta2.tar.gz -C /compilers/ps2/ee-gcc3.2-030210-beta2

RUN chown -R root:root /compilers/ps2/ee-gcc3.2-030210-beta2/
RUN chmod +x /compilers/ps2/ee-gcc3.2-030210-beta2/*


FROM scratch as release

COPY --from=base /compilers /compilers
