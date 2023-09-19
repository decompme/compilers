# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-990721

RUN wget -O ee-gcc2.9-990721.tar.xz "https://cdn.discordapp.com/attachments/1067192766918037536/1067306679806464060/ee-gcc2.9-990721.tar.xz"
RUN tar xvJf ee-gcc2.9-990721.tar.xz -C /compilers/ps2/ee-gcc2.9-990721

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-990721/
RUN chmod +x /compilers/ps2/ee-gcc2.9-990721/*


FROM scratch as release

COPY --from=base /compilers /compilers
