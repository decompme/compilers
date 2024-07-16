# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O mwccarm.zip "https://github.com/decompme/compilers/releases/download/compilers/mwccarm.zip"
RUN unzip mwccarm.zip

RUN mkdir -p /compilers/nds_arm9/mwcc_40_1036

RUN cp -r mwccarm/dsi/1.3p1/* /compilers/nds_arm9/mwcc_40_1036

RUN cp */license.dat /compilers/nds_arm9/mwcc_40_1036/license.dat
RUN mv /compilers/nds_arm9/mwcc_40_1036/lmgr8c.dll /compilers/nds_arm9/mwcc_40_1036/LMGR8C.dll

RUN chown -R root:root /compilers/nds_arm9/mwcc_40_1036/
RUN chmod +x /compilers/nds_arm9/mwcc_40_1036/mwccarm.exe


FROM scratch as release

COPY --from=base /compilers /compilers
