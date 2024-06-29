# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-991111b/r4

RUN wget -O ee-gcc29-991111b-r4.tar.xz "https://github.com/TheOnlyZac/decomp.me/releases/download/ee-gcc2.9-991111/ee-gcc29-991111b-r4.tar.xz"
RUN tar xvJf ee-gcc29-991111b-r4.tar.xz -C /compilers/ps2/ee-gcc2.9-991111b/r4

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-991111b/r4/
RUN chmod +x /compilers/ps2/ee-gcc2.9-991111b/r4/*


FROM scratch as release

COPY --from=base /compilers /compilers
