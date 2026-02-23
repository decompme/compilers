# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win32/msvc9.0sp1

RUN wget -O msvc9.0sp1-fulltree.tar.gz "https://github.com/RogueValleyInformationSecurity/compilers/releases/download/msvc9.0sp1-20260223/msvc9.0sp1-fulltree.tar.gz"
RUN tar xvzf msvc9.0sp1-fulltree.tar.gz -C /compilers/win32/msvc9.0sp1

RUN chown -R root:root /compilers/win32/msvc9.0sp1/
RUN chmod +x /compilers/win32/msvc9.0sp1/*


FROM scratch as release

COPY --from=base /compilers /compilers
