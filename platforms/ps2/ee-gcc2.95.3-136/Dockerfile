# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.95.3-136

RUN wget -O ee-gcc2.95.3-136.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.95.3-136.tar.gz"
RUN tar xvzf ee-gcc2.95.3-136.tar.gz -C /compilers/ps2/ee-gcc2.95.3-136

RUN chown -R root:root /compilers/ps2/ee-gcc2.95.3-136/
RUN chmod +x /compilers/ps2/ee-gcc2.95.3-136/*


FROM scratch as release

COPY --from=base /compilers /compilers
