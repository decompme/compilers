# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win9x/msvc6.5

RUN wget -O msvc6.5.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/msvcwin9x/msvc6.5.tar.gz"
RUN tar xvzf msvc6.5.tar.gz -C /compilers/win9x/msvc6.5
RUN rm -rf /compilers/win9x/msvc6.5/MFC

RUN chown -R root:root /compilers/win9x/msvc6.5/
RUN chmod +x /compilers/win9x/msvc6.5/*


FROM scratch as release

COPY --from=base /compilers /compilers
