# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/mips_pro_744

RUN wget -O mipspro7.4.4.tar.xz "https://github.com/LLONSIT/qemu-irix-helpers/raw/n/qemu/mipspro7.4.4.tar.xz"
RUN tar xvJf mipspro7.4.4.tar.xz -C /compilers/n64/mips_pro_744

RUN chown -R root:root /compilers/n64/mips_pro_744/
RUN chmod +x /compilers/n64/mips_pro_744/*


FROM scratch as release

COPY --from=base /compilers /compilers
