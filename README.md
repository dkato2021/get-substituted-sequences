# get_substituted_sequences
**MiSeqなどで得られた正確な配列を、Nanoporeなどで得られた配列へマッピングし、置換するスクリプト**

## Usage
```
python substitute.py rough_sequences.fasta accurate_sequences.fasta substituted_sequences.fasta
```
- rough_sequences.fasta; Nanoporeで得られた配列など
- accurate_sequences.fasta; MiSeqで得られた配列など
