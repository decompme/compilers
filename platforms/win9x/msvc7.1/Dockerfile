# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win9x/msvc7.1

RUN wget -O msvc7.0.tar.gz "https://github.com/OmniBlade/decomp.me/releases/download/msvcwin9x/msvc7.0.tar.gz"
RUN tar xvzf msvc7.0.tar.gz -C /compilers/win9x/msvc7.1
RUN rm -rf /compilers/win9x/msvc7.1/MFC

RUN chown -R root:root /compilers/win9x/msvc7.1/
RUN chmod +x /compilers/win9x/msvc7.1/*


FROM scratch as release

COPY --from=base /compilers /compilers
