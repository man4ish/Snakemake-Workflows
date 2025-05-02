FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    skewer \
    samtools \
    openjdk-11-jre \
    wget \
    unzip \
    python3 \
    python3-pip

# Install STAR
RUN wget https://github.com/alexdobin/STAR/archive/2.7.10a.tar.gz && \
    tar -xzf 2.7.10a.tar.gz && \
    cd STAR-2.7.10a/source && make STAR && cp STAR /usr/local/bin/

# Install Picard
RUN wget https://github.com/broadinstitute/picard/releases/download/2.27.5/picard.jar -P /software/utils/

# Install kallisto
RUN wget https://github.com/pachterlab/kallisto/releases/download/v0.48.0/kallisto_linux-v0.48.0.tar.gz && \
    tar -xzf kallisto_linux-v0.48.0.tar.gz && \
    mv kallisto/* /usr/local/bin/

ENV PATH="/software/utils:$PATH"
