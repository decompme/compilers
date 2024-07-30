# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O d6c4aa208c8345c78a9f68ba6ef911ee94c6a6e1.zip "https://github.com/widberg/msvc8.0/archive/d6c4aa208c8345c78a9f68ba6ef911ee94c6a6e1.zip"
RUN unzip d6c4aa208c8345c78a9f68ba6ef911ee94c6a6e1.zip

RUN mkdir -p /compilers/win32/msvc8.0/Bin
RUN mkdir -p /compilers/win32/msvc8.0/Include

RUN cp -r msvc8.0-*/bin/*     /compilers/win32/msvc8.0/Bin
RUN cp -r msvc8.0-*/include/* /compilers/win32/msvc8.0/Include

RUN chown -R root:root /compilers/win32/msvc8.0/
RUN chmod +x /compilers/win32/msvc8.0/Bin/*


FROM scratch as release

COPY --from=base /compilers /compilers
