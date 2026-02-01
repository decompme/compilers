# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/android_x86/ndk-r8e-gcc-4.7

RUN wget -O android-ndk-r8e-linux-x86_64.tar.bz2 "https://github.com/decompme/compilers/releases/download/compilers/android-ndk-r8e-linux-x86_64.tar.bz2"
RUN tar xvjf android-ndk-r8e-linux-x86_64.tar.bz2 -C /compilers/android_x86/ndk-r8e-gcc-4.7

RUN chown -R root:root /compilers/android_x86/ndk-r8e-gcc-4.7/
RUN chmod +x /compilers/android_x86/ndk-r8e-gcc-4.7/*


FROM scratch as release

COPY --from=base /compilers /compilers
