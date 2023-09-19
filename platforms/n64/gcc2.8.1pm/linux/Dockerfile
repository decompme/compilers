# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/n64/gcc2.8.1pm

RUN wget -O linux.tar.gz "https://github.com/pmret/gcc-papermario/releases/download/master/linux.tar.gz"
RUN tar xvzf linux.tar.gz -C /compilers/n64/gcc2.8.1pm
RUN wget -O linux.tar.gz "https://github.com/pmret/binutils-papermario/releases/download/master/linux.tar.gz"
RUN tar xvzf linux.tar.gz -C /compilers/n64/gcc2.8.1pm

RUN chown -R root:root /compilers/n64/gcc2.8.1pm/
RUN chmod +x /compilers/n64/gcc2.8.1pm/*


FROM scratch as release

COPY --from=base /compilers /compilers
