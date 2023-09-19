# NOTE: This file is generated automatically via template.py. Do not edit manually!


FROM alpine:3.18 as base

RUN mkdir -p /compilers/macosx/gcc-5370

RUN wget -O gcc-5370.tar.gz "https://github.com/ChrisNonyminus/powerpc-darwin-cross/releases/download/initial/gcc-5370.tar.gz"
RUN tar xvzf gcc-5370.tar.gz -C /compilers/macosx/gcc-5370
RUN wget -O /compilers/macosx/gcc-5370/convert_gas_syntax.py "https://gist.githubusercontent.com/ChrisNonyminus/ec53837b151a65e4233fa53604de4549/raw/d7c6fc639310b938fa519e68a8f8d4909acba2ad/convert_gas_syntax.py"

RUN chown -R root:root /compilers/macosx/gcc-5370/
RUN chmod +x /compilers/macosx/gcc-5370/*


FROM scratch as release

COPY --from=base /compilers /compilers
