# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O compilers_latest.zip "https://files.decomp.dev/compilers_latest.zip?2023-10-26"
RUN unzip compilers_latest.zip

RUN mkdir -p /compilers/gc_wii/mwcc_242_81r

RUN cp -r GC/1.3.2r/* /compilers/gc_wii/mwcc_242_81r

RUN chmod +x /compilers/gc_wii/mwcc_242_81r/mwcceppc.exe
RUN touch /compilers/gc_wii/mwcc_242_81r/license.dat
RUN if [[ -f /compilers/gc_wii/mwcc_242_81r/lmgr326b.dll ]]; then \
    mv /compilers/gc_wii/mwcc_242_81r/lmgr326b.dll /compilers/gc_wii/mwcc_242_81r/LMGR326B.dll; \
  fi
RUN if [[ -f /compilers/gc_wii/mwcc_242_81r/lmgr8c.dll ]]; then \
    mv /compilers/gc_wii/mwcc_242_81r/lmgr8c.dll /compilers/gc_wii/mwcc_242_81r/LMGR8C.dll; \
  fi

RUN chown -R root:root /compilers/gc_wii/mwcc_242_81r/


FROM scratch as release

COPY --from=base /compilers /compilers
