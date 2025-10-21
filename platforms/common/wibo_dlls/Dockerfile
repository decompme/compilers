# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/common/wibo_dlls

RUN wget -O msvcrt_20251015.zip "https://files.decomp.dev/msvcrt_20251015.zip"
RUN unzip msvcrt_20251015.zip -d /compilers/common/wibo_dlls

RUN chown -R root:root /compilers/common/wibo_dlls/
RUN chmod +x /compilers/common/wibo_dlls/*


FROM scratch as release

COPY --from=base /compilers /compilers
