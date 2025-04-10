# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-991111-01-dtls13010

RUN wget -O ee-gcc2.9-991111-01-dtls13010.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.9-991111-01-dtls13010.tar.gz"
RUN tar xvzf ee-gcc2.9-991111-01-dtls13010.tar.gz -C /compilers/ps2/ee-gcc2.9-991111-01-dtls13010

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-991111-01-dtls13010/
RUN chmod +x /compilers/ps2/ee-gcc2.9-991111-01-dtls13010/*


FROM scratch as release

COPY --from=base /compilers /compilers
