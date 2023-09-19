# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O mwccarm.zip "https://cdn.discordapp.com/attachments/698589325620936736/845499146982129684/mwccarm.zip"
RUN unzip mwccarm.zip

RUN mkdir -p /compilers/nds_arm9/mwcc_40_1034

RUN cp -r mwccarm/dsi/1.3/* /compilers/nds_arm9/mwcc_40_1034

RUN cp */license.dat /compilers/nds_arm9/mwcc_40_1034/license.dat
RUN mv /compilers/nds_arm9/mwcc_40_1034/lmgr8c.dll /compilers/nds_arm9/mwcc_40_1034/LMGR8C.dll

RUN chown -R root:root /compilers/nds_arm9/mwcc_40_1034/
RUN chmod +x /compilers/nds_arm9/mwcc_40_1034/mwccarm.exe


FROM scratch as release

COPY --from=base /compilers /compilers
