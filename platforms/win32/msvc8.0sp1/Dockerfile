# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

# download zip first to allow for Docker caching

RUN wget -O 0d6f444cfc120e4e62a092726844fa310c74b1bc.zip "https://github.com/Drahsid/ffxiv_msvc8.0sp1/archive/0d6f444cfc120e4e62a092726844fa310c74b1bc.zip"
RUN unzip 0d6f444cfc120e4e62a092726844fa310c74b1bc.zip

RUN mkdir -p /compilers/win32/msvc8.0sp1/Bin
RUN mkdir -p /compilers/win32/msvc8.0sp1/Include

RUN cp -r ffxiv_msvc8.0sp1-*/bin/*     /compilers/win32/msvc8.0sp1/Bin
RUN cp -r ffxiv_msvc8.0sp1-*/include/* /compilers/win32/msvc8.0sp1/Include
RUN cp -r ffxiv_msvc8.0sp1-*/PlatformSDK/Include/* /compilers/win32/msvc8.0sp1/Include

RUN chown -R root:root /compilers/win32/msvc8.0sp1/
RUN chmod +x /compilers/win32/msvc8.0sp1/Bin/*


FROM scratch AS release

COPY --from=base /compilers /compilers
