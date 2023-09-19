# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/egcs_1.1.2-4

RUN wget -O egcs_1.1.2-4.tar.gz "https://github.com/AngheloAlf/egcs_1.1.2-4/releases/download/latest/egcs_1.1.2-4.tar.gz"
RUN tar xvzf egcs_1.1.2-4.tar.gz -C /compilers/n64/egcs_1.1.2-4

RUN chown -R root:root /compilers/n64/egcs_1.1.2-4/
RUN chmod +x /compilers/n64/egcs_1.1.2-4/*


FROM scratch as release

COPY --from=base /compilers /compilers
