import gzip

def write_fastq(filename, reads):
    with gzip.open(filename, 'wt') as f:
        for i, (seq, qual) in enumerate(reads):
            f.write(f"@read{i}\n{seq}\n+\n{qual}\n")

# Generate 5 dummy reads of 75 bp each
reads_R1 = [("A" * 75, "I" * 75) for _ in range(5)]
reads_R2 = [("T" * 75, "I" * 75) for _ in range(5)]

# Write to gzipped FASTQ files
write_fastq("sample1_R1.fastq.gz", reads_R1)
write_fastq("sample1_R2.fastq.gz", reads_R2)

print("Synthetic FASTQ files generated:")
print("- sample1_R1.fastq.gz")
print("- sample1_R2.fastq.gz")

