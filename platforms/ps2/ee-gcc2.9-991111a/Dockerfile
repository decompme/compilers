# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-991111a

RUN wget -O ee-gcc2.9-991111a.tar.xz "https://github.com/decompme/compilers/releases/download/compilers/ee-gcc2.9-991111a.tar.xz"
RUN tar xvJf ee-gcc2.9-991111a.tar.xz -C /compilers/ps2/ee-gcc2.9-991111a

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-991111a/
RUN chmod +x /compilers/ps2/ee-gcc2.9-991111a/*


FROM scratch as release

COPY --from=base /compilers /compilers
