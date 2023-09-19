# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/msdos/wcc11.0

RUN wget -O wcc11.0.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/wcc10.5/wcc11.0.tar.gz"
RUN tar xvzf wcc11.0.tar.gz -C /compilers/msdos/wcc11.0

RUN chown -R root:root /compilers/msdos/wcc11.0/
RUN chmod +x /compilers/msdos/wcc11.0/*


FROM scratch as release

COPY --from=base /compilers /compilers
