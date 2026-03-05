# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/dreamcast/shc-v5.1r11

RUN wget -O shc-v5.1r11.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/shc-v5.1r11.tar.gz"
RUN tar xvzf shc-v5.1r11.tar.gz -C /compilers/dreamcast/shc-v5.1r11
RUN wget -O /compilers/dreamcast/shc-v5.1r11/rof2elf.py "https://gist.githubusercontent.com/Mc-muffin/c2d3f30e50c5c5749f994973441c503a/raw/18fbf1a19bd720d02774ed634b00b0508eaf474c/rof2elf.py"

RUN chown -R root:root /compilers/dreamcast/shc-v5.1r11/
RUN chmod +x /compilers/dreamcast/shc-v5.1r11/*


FROM scratch as release

COPY --from=base /compilers /compilers
