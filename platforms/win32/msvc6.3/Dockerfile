# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win32/msvc6.3

RUN wget -O msvc6.3.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/msvcwin9x/msvc6.3.tar.gz"
RUN tar xvzf msvc6.3.tar.gz -C /compilers/win32/msvc6.3
RUN rm -rf /compilers/win32/msvc6.3/MFC

RUN chown -R root:root /compilers/win32/msvc6.3/
RUN chmod +x /compilers/win32/msvc6.3/*


FROM scratch as release

COPY --from=base /compilers /compilers
