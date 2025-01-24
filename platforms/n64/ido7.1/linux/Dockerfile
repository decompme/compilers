# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/ido7.1

RUN wget -O ido-7.1-recomp-linux.tar.gz "https://github.com/decompals/ido-static-recomp/releases/download/v1.2/ido-7.1-recomp-linux.tar.gz"
RUN tar xvzf ido-7.1-recomp-linux.tar.gz -C /compilers/n64/ido7.1

RUN chown -R root:root /compilers/n64/ido7.1/
RUN chmod +x /compilers/n64/ido7.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
