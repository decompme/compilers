# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win32/msvc7.0

RUN wget -O msvc7.0.tar.gz "https://github.com/roblabla/MSVC-7.0-Portable/releases/download/release/msvc7.0.tar.gz"
RUN tar xvzf msvc7.0.tar.gz -C /compilers/win32/msvc7.0

RUN chown -R root:root /compilers/win32/msvc7.0/
RUN chmod +x /compilers/win32/msvc7.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
