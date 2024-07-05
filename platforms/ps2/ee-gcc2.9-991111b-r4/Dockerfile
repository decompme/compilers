# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-991111b-r4

RUN wget -O ee-gcc2.9-991111.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.9-991111.tar.gz"
RUN tar xvzf ee-gcc2.9-991111.tar.gz -C /compilers/ps2/ee-gcc2.9-991111b-r4

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-991111b-r4/
RUN chmod +x /compilers/ps2/ee-gcc2.9-991111b-r4/*


FROM scratch as release

COPY --from=base /compilers /compilers
