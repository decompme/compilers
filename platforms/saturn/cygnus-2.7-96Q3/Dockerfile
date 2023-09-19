# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

WORKDIR /root

RUN wget -O af27f4aa6566c1b0fa5332b488e63d6ffd28bd48.zip "https://github.com/sozud/saturn-compilers/archive/af27f4aa6566c1b0fa5332b488e63d6ffd28bd48.zip"
RUN unzip af27f4aa6566c1b0fa5332b488e63d6ffd28bd48.zip

RUN mkdir -p /compilers/saturn/cygnus-2.7-96Q3

RUN cp -r saturn-compilers-*/cygnus-2.7-96Q3-bin/* /compilers/saturn/cygnus-2.7-96Q3

RUN chown -R root:root /compilers/saturn/cygnus-2.7-96Q3/
RUN chmod +x /compilers/saturn/cygnus-2.7-96Q3/*


FROM scratch as release

COPY --from=base /compilers /compilers
