# get_substituted_sequences
**1.MiSeqなどで得られた配列を、Nanoporeなどで得られた配列へマッピング
2.該当箇所が置換された後者の配列を出力**

## Usage
```
python substitute.py rough_sequences.fasta accurate_sequences.fasta <output_dir>
```
- rough_sequences.fasta; Nanoporeで得られた配列など
- accurate_sequences.fasta; MiSeqで得られた配列など
