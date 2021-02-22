# get substituted sequences
**1.MiSeqなどで得られた配列を、Nanoporeなどで得られた配列へマッピング**

**2.後者の配列について、マッピング該当箇所を前者の配列で置換して、出力する**

## installation
```
$ pip install -r requirements.txt #condaでのinstallも可
```
## Usage
```
$ python substitute.py rough_sequences.fasta accurate_sequences.fasta <output_dir>
```
- rough_sequences.fasta; Nanoporeで得られた配列など
- accurate_sequences.fasta; MiSeqで得られた配列など

## 検証
置換前と置換後の2配列をアライメントして、結果を可視化する(追記予定)
