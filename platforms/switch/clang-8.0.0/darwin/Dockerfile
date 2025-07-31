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

RUN apk add patch

ARG PATCH_REPO=https://github.com/GRAnimated/switch-clang-patches
ARG PATCH_BRANCH=main

RUN wget -O patches.zip "${PATCH_REPO}/archive/refs/heads/${PATCH_BRANCH}.zip"
RUN unzip patches.zip -d /tmp
RUN mv /tmp/switch-clang-patches-${PATCH_BRANCH} /tmp/patches

# apply patches to clang
RUN patch_dir="/tmp/patches/clang-8.0.0" && \
    find "$patch_dir" -type f -name '*.diff' -print0 | while IFS= read -r -d '' patch; do \
        echo "Applying patch: $patch"; \
        patch -d "/compilers/switch/clang-8.0.0" -p0 < "$patch"; \
    done;

RUN chown -R root:root /compilers/switch/clang-8.0.0/


FROM scratch as release

COPY --from=base /compilers /compilers
