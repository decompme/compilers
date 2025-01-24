# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/ido5.3

RUN wget -O ido-5.3-recomp-linux.tar.gz "https://github.com/decompals/ido-static-recomp/releases/download/v1.2/ido-5.3-recomp-linux.tar.gz"
RUN tar xvzf ido-5.3-recomp-linux.tar.gz -C /compilers/n64/ido5.3

RUN chown -R root:root /compilers/n64/ido5.3/
RUN chmod +x /compilers/n64/ido5.3/*


FROM scratch as release

COPY --from=base /compilers /compilers
