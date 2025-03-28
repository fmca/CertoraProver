FROM ubuntu:22.04

ARG SOLC_VERSION="0.8.29"
ARG CVC5_VERSION="1.2.1"
ARG Z3_VERSION="4.14.1"

RUN apt update

# Base dependencies
RUN apt install -y curl wget openjdk-11-jdk llvm unzip xz-utils git python3 python3-pip jq psmisc

#z3
RUN curl --silent "https://api.github.com/repos/Z3Prover/z3/releases/tags/z3-${Z3_VERSION}" | jq -r '.assets[] | select(.name | test("x64-glib")) | .browser_download_url' | wget -qi - -O z3.zip \
    && unzip -p z3.zip '*bin/z3' > /usr/local/bin/z3 \
    && chmod a+x /usr/local/bin/z3

#CVC5
RUN wget -qi - -O cvc5.zip https://github.com/cvc5/cvc5/releases/download/cvc5-${CVC5_VERSION}/cvc5-Linux-x86_64-static.zip \
    && unzip -p cvc5.zip '*bin/cvc5' > /usr/local/bin/cvc5 \
    && chmod a+x /usr/local/bin/cvc5

# Rust
RUN mkdir -p /tmp/rust && cd /tmp/rust && \  
    curl -fsSL https://static.rust-lang.org/dist/rust-1.85.1-x86_64-unknown-linux-gnu.tar.xz \  
    | tar -xJ --strip-components=1 && \  
    ./install.sh --prefix=/usr/local && \  
    rm -rf /tmp/rust  

ENV CERTORA="/opt/CertoraProver"
ENV PATH="$CERTORA:$PATH"

WORKDIR /opt
# Avoid ssh auth in git, clone certora
RUN git clone https://github.com/Certora/CertoraProver.git

# rewrite hardcoded ssh gitmodules from submodules and Cargo.toml files
WORKDIR /opt/CertoraProver
RUN git config --global url."https://github.com/".insteadOf "git@github.com:"
RUN git submodule update --init --recursive
RUN find . -type f -name "Cargo.toml" -exec sed -i 's|ssh://git@github.com/|https://github.com/|' {} +



RUN pip3 install solc-select
RUN solc-select install ${SOLC_VERSION}
RUN solc-select use ${SOLC_VERSION}
RUN ./gradlew assemble
RUN pip3 install -r scripts/certora_cli_requirements.txt