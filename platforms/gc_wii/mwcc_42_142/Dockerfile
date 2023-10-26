# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O compilers_latest.zip "https://files.decomp.dev/compilers_latest.zip?2023-10-26"
RUN unzip compilers_latest.zip

RUN mkdir -p /compilers/gc_wii/mwcc_42_142

RUN cp -r Wii/1.0/* /compilers/gc_wii/mwcc_42_142

RUN chmod +x /compilers/gc_wii/mwcc_42_142/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_42_142/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_42_142/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_42_142/lmgr326b.dll /compilers/gc_wii/mwcc_42_142/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_42_142/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_42_142/lmgr8c.dll /compilers/gc_wii/mwcc_42_142/LMGR8C.dll; \
  fi

RUN chown -R root:root /compilers/gc_wii/mwcc_42_142/


FROM scratch as release

COPY --from=base /compilers /compilers
