# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/switch/clang-8.0.0

RUN wget -O clang+llvm-8.0.0-x86_64-apple-darwin.tar.xz "https://releases.llvm.org/8.0.0/clang+llvm-8.0.0-x86_64-apple-darwin.tar.xz"
RUN tar xvJf clang+llvm-8.0.0-x86_64-apple-darwin.tar.xz --strip-components=1 -C /compilers/switch/clang-8.0.0

# we only need the clang-x.y.z binary
RUN mv /compilers/switch/clang-8.0.0/bin /compilers/switch/clang-8.0.0/_bin
RUN mkdir /compilers/switch/clang-8.0.0/bin
RUN mv /compilers/switch/clang-8.0.0/_bin/clang-8 /compilers/switch/clang-8.0.0/bin
RUN mv /compilers/switch/clang-8.0.0/_bin/clang++ /compilers/switch/clang-8.0.0/bin
RUN mv /compilers/switch/clang-8.0.0/_bin/clang /compilers/switch/clang-8.0.0/bin
RUN rm -rf /compilers/switch/clang-8.0.0/_bin/

RUN rm -rf /compilers/switch/clang-8.0.0/libexec
RUN rm -rf /compilers/switch/clang-8.0.0/share

ARG MUSL_HASH=25ed8669943bee65a650700d340e451eda2a26ba

RUN wget -O musl.zip https://github.com/open-ead/botw-lib-musl/archive/${MUSL_HASH}.zip
RUN unzip musl.zip
RUN cp -r botw-lib-musl-${MUSL_HASH} /compilers/switch/clang-8.0.0/

RUN chown -R root:root /compilers/switch/clang-8.0.0/


FROM scratch as release

COPY --from=base /compilers /compilers
