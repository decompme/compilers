# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O compilers_20240702.zip "https://files.decomp.dev/compilers_20240702.zip"
RUN unzip compilers_20240702.zip

RUN mkdir -p /compilers/gc_wii/mwcc_42_127

RUN cp -r Wii/0x4201_127/* /compilers/gc_wii/mwcc_42_127

RUN chmod +x /compilers/gc_wii/mwcc_42_127/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_42_127/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_42_127/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_42_127/lmgr326b.dll /compilers/gc_wii/mwcc_42_127/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_42_127/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_42_127/lmgr8c.dll /compilers/gc_wii/mwcc_42_127/LMGR8C.dll; \
  fi

RUN chown -R root:root /compilers/gc_wii/mwcc_42_127/


FROM scratch as release

COPY --from=base /compilers /compilers
