#!/usr/bin/env python3

import sys
import pandas as pd
from Bio import SeqIO

#==============================================================================
# Input
#==============================================================================
input1 = sys.argv[1] # input_csv from igvtool wigs
input2 = sys.argv[2]# ref fasta

input_csv = input1 # columns = position, A, C, G, T
refseq = input2
output_filename = input2 + '_call.csv'

#==============================================================================
# Calculation
#==============================================================================
base = [list(i.seq) for i in SeqIO.parse(refseq,'fasta')]
refpos = base[0]

output, poslist = [],[]
min_read_depth  = 1
count = 0

with open(input_csv) as f:
    for num,row in enumerate(f):
        if num >2: # get rid of titles
            count += 1
            readrow = [int(float(x)) for x in row.split()[:5]]
            position = readrow[0]
            ref = refpos[position-1].upper() # -1 for python 0-index
            
            rowdic = {'A': readrow[1], 'C':readrow[2],'G':readrow[3],'T':readrow[4]}
            sumall = sum((rowdic.values()))
            
            poslist.append(position)

# no read depth

            if position != count:
                out = {'Position': str(poslist[-2]) + ' to ' +str(position),
                       'Mutation': 'Read Depth = 0',
                       'Ref Base Rate':  '0',
                       'Read Base Rate': '0',
                       'Read Depth': '0'}
                output.append(out)
                count = position
                
            elif sumall == 0:
                out = {'Position': position,
                       'Mutation': 'Read Depth = 0',
                       'Ref Base Rate':  '0',
                       'Read Base Rate': '0',
                       'Read Depth': sumall}
                output.append(out)

# read depth more than 0
            
            else:           
                base = max(rowdic.keys(), key = (lambda key: rowdic[key]))             
                depth_ref = rowdic[ref]
                depth_base = rowdic[base]              
                try: 
                    percentage_base = depth_base/sumall
                except ZeroDivisionError:
                    percentage_base = 0                    
                try:
                    percentage_ref = depth_ref/sumall
                except ZeroDivisionError:
                    percentage_ref = 0

# low read depth
                    
                if sumall < min_read_depth: 
                    out = {'Position': position,
                           'Mutation': 'Read Depth <' + str(min_read_depth),
                           'Ref Base Rate':  ref + ' = ' + str(round(percentage_ref,2)),
                           'Read Base Rate': base + ' = ' + str(round(percentage_base,2)),
                           'Read Depth': sumall}
                    output.append(out)

# sufficient read depth, recode max base and mutation
                    
                elif ref != base:
                    mut = ref + ' to ' + base
                    out = {'Position': position,
                           'Mutation': mut,
                           'Ref Base Rate':  ref + ' = ' + str(round(percentage_ref,2)),
                           'Read Base Rate': base + ' = ' + str(round(percentage_base,2)),
                           'Read Depth': sumall}
                    output.append(out)

df = pd.DataFrame.from_dict(output)
df = df[['Position','Mutation','Ref Base Rate', 'Read Base Rate','Read Depth']]
df.to_csv(output_filename)

            
