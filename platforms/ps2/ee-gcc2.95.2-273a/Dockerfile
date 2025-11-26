# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.95.2-273a

RUN wget -O ee-gcc2.95.2-273a.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.95.2-273a.tar.gz"
RUN tar xvzf ee-gcc2.95.2-273a.tar.gz -C /compilers/ps2/ee-gcc2.95.2-273a

RUN chown -R root:root /compilers/ps2/ee-gcc2.95.2-273a/
RUN chmod +x /compilers/ps2/ee-gcc2.95.2-273a/*


FROM scratch as release

COPY --from=base /compilers /compilers
