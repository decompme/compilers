# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/gba/gcc2.9-arm-000512

RUN wget -O gcc2.9-arm-000512.tar.xz "https://github.com/aplerdal/arm000512/releases/download/Release/gcc2.9-arm-000512.tar.xz"
RUN tar xvJf gcc2.9-arm-000512.tar.xz -C /compilers/gba/gcc2.9-arm-000512

RUN chown -R root:root /compilers/gba/gcc2.9-arm-000512/
RUN chmod +x /compilers/gba/gcc2.9-arm-000512/*


FROM scratch as release

COPY --from=base /compilers /compilers
