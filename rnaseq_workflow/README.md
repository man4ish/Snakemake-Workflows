# RNA-seq Analysis Pipeline (Snakemake + Docker)

This repository contains a Snakemake implementation of an RNA-seq data analysis. The pipeline performs read trimming, quantification with Kallisto, alignment with STAR, sorting/indexing with Samtools, and summary metrics generation using Picard.

---

## Features

- Full RNA-seq preprocessing and quantification pipeline
- Uses Docker container: [`man4ish/rnaseq`](https://hub.docker.com/r/man4ish/rnaseq)
- Modular and reproducible with Snakemake
- Requires minimal setup

---

## Requirements

- [Snakemake](https://snakemake.readthedocs.io/en/stable/)
- [Docker](https://www.docker.com/)

---

## Directory Structure

```
.
├── Snakefile                  # Main Snakemake pipeline
├── config.yaml               # Configuration file with all input paths and parameters
├── README.md
├── data/                     # Folder to store input FASTQ files
├── resources/                # Contains index, annotation, reference files
└── results/                  # Output directory for all generated files
```

---

## Input Files

You must prepare the following:

- Paired-end FASTQ files (e.g. `sample_R1.fastq.gz`, `sample_R2.fastq.gz`)
- Adapter file (e.g. `adapters.fa`)
- Kallisto index (`.idx`) and GTF file
- STAR genome reference tarball
- Picard annotation files: `ref_flat.txt`, `rRNA.interval_list`, `reference.fa`

Specify all paths in `config.yaml`.

---

## Building the Docker Image

You can use the prebuilt image `man4ish/rnaseq`, or build your own if needed:

---

### Build the Image

```bash
docker build -t myuser/rnaseq:latest .
```

### Push to Docker Hub (optional)

```bash
docker push myuser/rnaseq:latest
```

Update the `Snakefile` to use your own image if desired:

```python
container: "docker.io/myuser/rnaseq:latest"
```

---

## Configuration (`config.yaml`)

```yaml
prefix: "sample"
fastq1: "data/sample_R1.fastq.gz"
fastq2: "data/sample_R2.fastq.gz"
adapters: "resources/adapters.fa"
skewer_threads: 4
minimum_read_length: 30
idx: "resources/kallisto_index.idx"
gtf: "resources/transcripts.gtf"
kallisto_threads: 4
bootstrap_samples: 100
ref_tar: "resources/star_reference.tar.gz"
STAR_threads: 8
ref_flat: "resources/ref_flat.txt"
ribosomal_interval: "resources/rRNA.interval_list"
ref_seq: "resources/reference.fa"
```

---

## Running the Pipeline

To run the full workflow:

```bash
snakemake --use-docker --cores 8
```

To run a specific rule (e.g., `align`):

```bash
snakemake results/sample_sample.bam --use-docker --cores 4
```

Docker ensures reproducibility and removes the need to install tools manually.

---

## Output Files

- Trimmed FASTQ files
- Kallisto expression tarball
- BAM files (aligned, sorted, indexed)
- RNA-seq summary report (`*.rna.summary`)
- Coverage plots (`*.plot.pdf`)

---

## Cleaning Up

To remove all output:

```bash
snakemake --delete-all-output
```

---
