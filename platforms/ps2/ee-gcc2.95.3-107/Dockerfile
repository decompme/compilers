# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download xz first to allow for Docker caching

WORKDIR /root

RUN wget -O ps2_compilers.tar.xz "https://cdn.discordapp.com/attachments/1067192766918037536/1120445708516995118/ps2_compilers.tar.xz"
RUN tar xvJf ps2_compilers.tar.xz

RUN mkdir -p /compilers/ps2/ee-gcc2.95.3-107

RUN cp -r ee-gcc2.95.3-107/* /compilers/ps2/ee-gcc2.95.3-107

RUN chown -R root:root /compilers/ps2/ee-gcc2.95.3-107/
RUN chmod +x /compilers/ps2/ee-gcc2.95.3-107/*


FROM scratch as release

COPY --from=base /compilers /compilers
