# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download xz first to allow for Docker caching

WORKDIR /root

RUN wget -O ps2_compilers.tar.xz "https://github.com/decompme/compilers/releases/download/compilers/ps2_compilers.tar.xz"
RUN tar xvJf ps2_compilers.tar.xz

RUN mkdir -p /compilers/ps2/ee-gcc2.95.3-114

RUN cp -r ee-gcc2.95.3-114/* /compilers/ps2/ee-gcc2.95.3-114

RUN chown -R root:root /compilers/ps2/ee-gcc2.95.3-114/
RUN chmod +x /compilers/ps2/ee-gcc2.95.3-114/*


FROM scratch as release

COPY --from=base /compilers /compilers
