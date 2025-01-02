# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/egcs_1.1.2-4c

RUN wget -O mips-binutils-egcs-2.9.5-macos.tar.gz "https://github.com/decompals/mips-binutils-egcs-2.9.5/releases/download/0.6/mips-binutils-egcs-2.9.5-macos.tar.gz"
RUN tar xvzf mips-binutils-egcs-2.9.5-macos.tar.gz -C /compilers/n64/egcs_1.1.2-4c
RUN wget -O mips-gcc-egcs-2.91.66-macos.tar.gz "https://github.com/decompals/mips-gcc-egcs-2.91.66/releases/download/0.7/mips-gcc-egcs-2.91.66-macos.tar.gz"
RUN tar xvzf mips-gcc-egcs-2.91.66-macos.tar.gz -C /compilers/n64/egcs_1.1.2-4c

RUN chown -R root:root /compilers/n64/egcs_1.1.2-4c/
RUN chmod +x /compilers/n64/egcs_1.1.2-4c/*


FROM scratch as release

COPY --from=base /compilers /compilers
