# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O mwccarm.zip "https://github.com/decompme/compilers/releases/download/compilers/mwccarm.zip"
RUN unzip mwccarm.zip

RUN mkdir -p /compilers/nds_arm9/mwcc_30_126

RUN cp -r mwccarm/2.0/sp1p2/* /compilers/nds_arm9/mwcc_30_126

RUN cp */license.dat /compilers/nds_arm9/mwcc_30_126/license.dat
RUN mv /compilers/nds_arm9/mwcc_30_126/lmgr8c.dll /compilers/nds_arm9/mwcc_30_126/LMGR8C.dll

RUN chown -R root:root /compilers/nds_arm9/mwcc_30_126/
RUN chmod +x /compilers/nds_arm9/mwcc_30_126/mwccarm.exe


FROM scratch as release

COPY --from=base /compilers /compilers
