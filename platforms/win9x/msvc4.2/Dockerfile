# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

# download zip first to allow for Docker caching

RUN wget -O df2c13aad74c094988c6c7e784234c2e778a0e91.zip "https://github.com/itsmattkc/MSVC420/archive/df2c13aad74c094988c6c7e784234c2e778a0e91.zip"
RUN unzip df2c13aad74c094988c6c7e784234c2e778a0e91.zip

RUN mkdir -p /compilers/win9x/msvc4.2/Bin
RUN mkdir -p /compilers/win9x/msvc4.2/Include

RUN cp -r MSVC420-*/bin/*     /compilers/win9x/msvc4.2/Bin
RUN cp -r MSVC420-*/include/* /compilers/win9x/msvc4.2/Include

RUN chown -R root:root /compilers/win9x/msvc4.2/
RUN chmod +x /compilers/win9x/msvc4.2/Bin/*


FROM scratch as release

COPY --from=base /compilers /compilers
