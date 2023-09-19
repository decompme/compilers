# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/msdos/wcc10.5

RUN wget -O wcc10.5.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/wcc10.5/wcc10.5.tar.gz"
RUN tar xvzf wcc10.5.tar.gz -C /compilers/msdos/wcc10.5

RUN chown -R root:root /compilers/msdos/wcc10.5/
RUN chmod +x /compilers/msdos/wcc10.5/*


FROM scratch as release

COPY --from=base /compilers /compilers
