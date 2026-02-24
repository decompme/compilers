# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/win32/msvc9.0rtm

RUN wget -O msvc9.0rtm-fulltree.tar.gz "https://github.com/RogueValleyInformationSecurity/compilers/releases/download/msvc9.0rtm-20260223/msvc9.0rtm-fulltree.tar.gz"
RUN tar xvzf msvc9.0rtm-fulltree.tar.gz -C /compilers/win32/msvc9.0rtm

RUN chown -R root:root /compilers/win32/msvc9.0rtm/
RUN chmod +x /compilers/win32/msvc9.0rtm/*


FROM scratch as release

COPY --from=base /compilers /compilers
