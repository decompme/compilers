# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/psp/mwccpsp_3.0.1_210

RUN wget -O mwccpsp_3.0.1_210.tar.gz "https://github.com/decompme/compilers/releases/download/compilers/mwccpsp_3.0.1_210.tar.gz"
RUN tar xvzf mwccpsp_3.0.1_210.tar.gz -C /compilers/psp/mwccpsp_3.0.1_210

RUN chown -R root:root /compilers/psp/mwccpsp_3.0.1_210/
RUN chmod +x /compilers/psp/mwccpsp_3.0.1_210/*


FROM scratch as release

COPY --from=base /compilers /compilers
