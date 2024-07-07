# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O compilers_20240706.zip "https://files.decomp.dev/compilers_20240706.zip"
RUN unzip compilers_20240706.zip

RUN mkdir -p /compilers/gc_wii/mwcc_247_92

RUN cp -r GC/2.0/* /compilers/gc_wii/mwcc_247_92

RUN chmod +x /compilers/gc_wii/mwcc_247_92/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_247_92/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_247_92/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_247_92/lmgr326b.dll /compilers/gc_wii/mwcc_247_92/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_247_92/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_247_92/lmgr8c.dll /compilers/gc_wii/mwcc_247_92/LMGR8C.dll; \
  fi

RUN chown -R root:root /compilers/gc_wii/mwcc_247_92/


FROM scratch as release

COPY --from=base /compilers /compilers
