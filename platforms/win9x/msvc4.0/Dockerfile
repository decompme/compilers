# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O 821e942fd95bd16d01649401de7943ef87ae9f54.zip "https://github.com/itsmattkc/MSVC400/archive/821e942fd95bd16d01649401de7943ef87ae9f54.zip"
RUN unzip 821e942fd95bd16d01649401de7943ef87ae9f54.zip

RUN mkdir -p /compilers/win9x/msvc4.0/Bin
RUN mkdir -p /compilers/win9x/msvc4.0/Include

RUN cp -r MSVC400-*/BIN/*     /compilers/win9x/msvc4.0/Bin
RUN cp -r MSVC400-*/INCLUDE/* /compilers/win9x/msvc4.0/Include

RUN chown -R root:root /compilers/win9x/msvc4.0/
RUN chmod +x /compilers/win9x/msvc4.0/Bin/*


FROM scratch as release

COPY --from=base /compilers /compilers
