# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/dreamcast/shc-v5.1r11

RUN wget -O shc-v5.1r11.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/shc-v5.1r11.tar.gz"
RUN tar xvzf shc-v5.1r11.tar.gz -C /compilers/dreamcast/shc-v5.1r11
RUN wget -O /compilers/dreamcast/shc-v5.1r11/rof2elf.py "https://gist.githubusercontent.com/masonc15/cb2354b439e35f1400c71edfca7171ca/raw/2556b4f781d49b167be0952b4420fadd2b5a313f/rof2elf.py"

RUN chown -R root:root /compilers/dreamcast/shc-v5.1r11/
RUN chmod +x /compilers/dreamcast/shc-v5.1r11/*


FROM scratch AS release

COPY --from=base /compilers /compilers
