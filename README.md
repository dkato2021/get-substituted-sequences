# get substituted sequences
**1.信用度の高い配列Aを信用度の低い配列Bへマッピング**

**2.配列Bについてマッピング該当箇所を配列Aで置換してB'を出力する**

```
## Usage
```
$ python substitute.py -r rough_sequences.fasta -a accurate_sequences.fasta -o <output_dir>
```
- rough_sequences.fasta; Nanopore由来contigsなど、信用度の低い配列
- accurate_sequences.fasta; MiSeq由来contigsなど、信用度の高い配列

## 検証
置換前と置換後の2配列をアライメントした結果を可視化する(追記予定)
