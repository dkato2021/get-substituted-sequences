import os, sys, csv, argparse
import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq

def get_args():
    parser = argparse.ArgumentParser(description='dkato. January, 2021') 
    parser.add_argument('-r', dest='rough', help='rough_sequences', required=True) 
    parser.add_argument('-a', '--accurate', help='accurate_sequences', required=True) 
    parser.add_argument('-o', '--output_dir', help='output_dir', default='./') 
    return parser.parse_args()

class MySubstitute(object):        
    def __init__(self, long_seq=None, short_seq=None, output_path=None):
        self.long_seq  = long_seq
        self.short_seq = short_seq
        self.output_path = output_path
        self.df=[]
        
    def nucmer(self):
        os.system(f'nucmer --prefix=test {self.long_seq} {self.short_seq}')
        os.system("delta-filter -q -r test.delta > filtered.delta")
        os.system("show-coords -rclT filtered.delta > filtered.coords")
        
        with open("filtered.coords") as f:
            reader = csv.reader(f.readlines()[3:], delimiter='\t')

        for i, row in enumerate(reader):
            if i==0:
                row.append('[QUEid]')
            self.df.append(row)

        self.df=pd.DataFrame(self.df, columns=self.df[0]).drop(0)\
                            .sort_values('[S1]', ascending=True).reset_index(drop=True)
        
    def main(self):
        self.longs = list(SeqIO.parse(self.long_seq, "fasta")) ;longs_id=[long.id for long in self.longs]
        self.new_longs_id=[long_id+'_Substituted' for long_id in longs_id]
        self.shorts = list(SeqIO.parse(self.short_seq, "fasta")) ;shorts_id=[short.id for short in self.shorts]

        for i in range(len(self.df)):
            REFid = longs_id.index(self.df.iloc[i,11])
            QUEid = shorts_id.index(self.df.iloc[i,12])
            REFsub = self.longs[REFid].seq[int(self.df.iloc[i,0])-1:int(self.df.iloc[i,1])]
            if int(self.df.iloc[i,2]) <= int(self.df.iloc[i,3]):
                QUEsub = self.shorts[QUEid].seq[int(self.df.iloc[i,2])-1:int(self.df.iloc[i,3])]
            else:
                QUEsub = self.shorts[QUEid].seq[int(self.df.iloc[i,3])-1:int(self.df.iloc[i,2])].reverse_complement()
            self.longs[REFid].seq = Seq(str(self.longs[REFid].seq).replace(str(REFsub), str(QUEsub)))

            dif=int(self.df.iloc[i,4])-int(self.df.iloc[i,5])#REF-QUE
            index=self.df.index[self.df.iloc[:,11]==self.df.iloc[i,11]]
            self.df.iloc[index,0:2] = self.df.iloc[index,0:2].astype(int) - dif
    
    def output(self):
        for i in range(len(self.longs)):
            self.longs[i].id=self.new_longs_id[i]
            self.longs[i].name=self.new_longs_id[i]
            self.longs[i].description=self.new_longs_id[i]
    
        SeqIO.write(self.longs, os.path.join('substituted_sequences.fasta'), "fasta")
        os.system("rm test.delta filtered.delta filtered.coords")

if __name__ == "__main__":
    args = get_args()
    instance = MySubstitute(long_seq=args.rough, short_seq=args.accurate, output_path=args.output_dir)
    instance.nucmer() ;instance.main() ;instance.output() ;print('5: SUBSTITUTIONS HAS BEEN DONE')
