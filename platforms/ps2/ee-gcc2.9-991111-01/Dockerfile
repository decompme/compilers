# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/ps2/ee-gcc2.9-991111-01

RUN wget -O ee-gcc2.9-991111-01.tar.xz "https://cdn.discordapp.com/attachments/1067192766918037536/1119832299400331314/ee-gcc2.9-991111-01.tar.xz"
RUN tar xvJf ee-gcc2.9-991111-01.tar.xz -C /compilers/ps2/ee-gcc2.9-991111-01

RUN chown -R root:root /compilers/ps2/ee-gcc2.9-991111-01/
RUN chmod +x /compilers/ps2/ee-gcc2.9-991111-01/*


FROM scratch as release

COPY --from=base /compilers /compilers
