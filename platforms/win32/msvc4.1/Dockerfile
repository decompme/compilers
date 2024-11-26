# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win32/msvc4.1

RUN wget -O msvc4.1.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/msvc4.1.tar.gz"
RUN tar xvzf msvc4.1.tar.gz -C /compilers/win32/msvc4.1

RUN chown -R root:root /compilers/win32/msvc4.1/
RUN chmod +x /compilers/win32/msvc4.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
