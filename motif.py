#!/usr/bin/env python

import fasta

#A1: I or V
#A2: L, I, M, T, V
#A3: L, V, I, A, G, M, P
#A4: D or E;
#A5: W, F, or Y;
#A6: G, L, I, A, V, T, S;
#A7: M or L;
#A8: E, D, G, I, L, A;
#A9: V, L, I, A, C, T;

allowed_aa=list()

t=set(['I', 'V'])
allowed_aa.append(t)
t=set(['L', 'I', 'M', 'T', 'V'])
allowed_aa.append(t)
t=set(['L', 'V', 'I', 'A', 'G', 'M', 'P'])
allowed_aa.append(t)
t=set(['D', 'E'])
allowed_aa.append(t)
t=set(['W', 'F', 'Y'])
allowed_aa.append(t)
t=set(['G', 'L', 'I', 'A', 'V', 'T', 'S'])
allowed_aa.append(t)
t=set(['M', 'L'])
allowed_aa.append(t)
t=set(['E', 'D', 'G', 'I', 'L', 'A'])
allowed_aa.append(t)
t=set(['V', 'L', 'I', 'A', 'C', 'T'])
allowed_aa.append(t)

plen=9
n=0
with open('/Users/sliang/CCNE1/Reviewd_Human_Database.fasta') as uniprot:
    for id, prot in fasta.fasta_record(uniprot):
        for i in range(len(prot)-plen):
            peptide=prot[i:i+plen]
            mismatch=0
            for j in [0, 3, 6, 4, 1, 7, 8, 2, 5]:
                if peptide[j] not in allowed_aa[j]:
                    mismatch+=1
                    if j==1 or j==8 or mismatch > 1:
                        break
            else:
                print peptide, id, i
