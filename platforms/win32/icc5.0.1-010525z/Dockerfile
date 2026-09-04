# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

RUN mkdir -p /compilers/win32/icc5.0.1-010525z

RUN wget -O msvc6.0.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/msvcwin9x/msvc6.0.tar.gz"
RUN tar xvzf msvc6.0.tar.gz -C /compilers/win32/icc5.0.1-010525z
RUN wget -O icc5.0.1-010525z.tar.gz "https://github.com/bwrsandman/icc5.0.1.010525Z/releases/download/v1/icc5.0.1-010525z.tar.gz"
RUN tar xvzf icc5.0.1-010525z.tar.gz -C /compilers/win32/icc5.0.1-010525z
RUN rm -rf /compilers/win32/icc5.0.1-010525z/MFC

RUN chown -R root:root /compilers/win32/icc5.0.1-010525z/
RUN chmod +x /compilers/win32/icc5.0.1-010525z/*


FROM scratch AS release

COPY --from=base /compilers /compilers
