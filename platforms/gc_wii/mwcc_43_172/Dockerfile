# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O compilers_20250520.zip "https://files.decomp.dev/compilers_20250520.zip"
RUN unzip compilers_20250520.zip

RUN mkdir -p /compilers/gc_wii/mwcc_43_172

RUN cp -r Wii/1.3/* /compilers/gc_wii/mwcc_43_172

RUN chmod +x /compilers/gc_wii/mwcc_43_172/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_43_172/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_43_172/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_43_172/lmgr326b.dll /compilers/gc_wii/mwcc_43_172/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_43_172/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_43_172/lmgr8c.dll /compilers/gc_wii/mwcc_43_172/LMGR8C.dll; \
  fi

RUN chown -R root:root /compilers/gc_wii/mwcc_43_172/


FROM scratch as release

COPY --from=base /compilers /compilers
