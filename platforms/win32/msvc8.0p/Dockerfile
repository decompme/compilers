# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O 52c8293f8b8d6441c594cf096542290c17a4d70e.zip "https://github.com/widberg/msvc8.0/archive/52c8293f8b8d6441c594cf096542290c17a4d70e.zip"
RUN unzip 52c8293f8b8d6441c594cf096542290c17a4d70e.zip

RUN mkdir -p /compilers/win32/msvc8.0p/Bin
RUN mkdir -p /compilers/win32/msvc8.0p/Include

RUN cp -r msvc8.0-*/bin/*     /compilers/win32/msvc8.0p/Bin
RUN cp -r msvc8.0-*/include/* /compilers/win32/msvc8.0p/Include
RUN cp -r msvc8.0-*/PlatformSDK/Include/* /compilers/win32/msvc8.0p/Include

RUN chown -R root:root /compilers/win32/msvc8.0p/
RUN chmod +x /compilers/win32/msvc8.0p/Bin/*


FROM scratch as release

COPY --from=base /compilers /compilers
