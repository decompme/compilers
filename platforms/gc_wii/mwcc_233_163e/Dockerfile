# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O GC_WII_COMPILERS.zip "https://cdn.discordapp.com/attachments/727918646525165659/1129759991696457728/GC_WII_COMPILERS.zip"
RUN unzip GC_WII_COMPILERS.zip

RUN mkdir -p /compilers/gc_wii/mwcc_233_163e

RUN cp -r GC/1.2.5e/* /compilers/gc_wii/mwcc_233_163e

RUN chmod +x /compilers/gc_wii/mwcc_233_163e/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_233_163e/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_233_163e/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_233_163e/lmgr326b.dll /compilers/gc_wii/mwcc_233_163e/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_233_163e/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_233_163e/lmgr8c.dll /compilers/gc_wii/mwcc_233_163e/LMGR8C.dll; \
  fi
ARG FRANK_HASH=d19668657d2a5efa42cdffb801090d05734b9dbd

RUN wget -O /compilers/gc_wii/mwcc_233_163e/frank.py https://raw.githubusercontent.com/doldecomp/melee/${FRANK_HASH}/tools/frank.py
RUN cp -r GC/1.2.5/mwcceppc.exe /compilers/gc_wii/mwcc_233_163e/mwcceppc.125.exe
RUN chmod +x /compilers/gc_wii/mwcc_233_163e/mwcceppc.125.exe

RUN chown -R root:root /compilers/gc_wii/mwcc_233_163e/


FROM scratch as release

COPY --from=base /compilers /compilers
