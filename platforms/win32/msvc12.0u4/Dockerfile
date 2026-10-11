# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 AS base

# download zip first to allow for Docker caching

RUN wget -O msvc12.zip "https://github.com/heinermann/compilers/releases/download/msvc12/msvc12.zip"
RUN unzip msvc12.zip

RUN mkdir -p /compilers/win32/msvc12.0u4/Bin
RUN mkdir -p /compilers/win32/msvc12.0u4/Include

RUN cp -r msvc12/bin/*     /compilers/win32/msvc12.0u4/Bin
RUN cp -r msvc12/include/* /compilers/win32/msvc12.0u4/Include
RUN cp -r msvc12/PlatformSDK/Include/* /compilers/win32/msvc12.0u4/Include

RUN chown -R root:root /compilers/win32/msvc12.0u4/
RUN chmod +x /compilers/win32/msvc12.0u4/Bin/*


FROM scratch AS release

COPY --from=base /compilers /compilers
