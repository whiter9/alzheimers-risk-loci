# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:38:43 2021

@author: whiter9
"""

import pandas as pd
from Bio import SeqIO
from Bio.SeqIO import read 


#data columns
name = []
length = []
sequence_version = []
description = []
comment = []
organism = []
molecule_type = []
topology = []
date = []
ref_count = []


id_list = ["AGRN","TNIP1","HAVCR2","GRN"]


#################################################################
# PARSE RESULTS
#################################################################

for item in id_list:
    seq_record = read(open('{}.gb'.format(item)),'genbank')
    
    name.append(seq_record.name)
    length.append(len(seq_record.seq))
    sequence_version.append(seq_record.annotations['sequence_version'])
    description.append(seq_record.description)
    comment.append(seq_record.annotations['comment'])
    organism.append(seq_record.annotations['organism'])
    molecule_type.append(seq_record.annotations['molecule_type'])
    topology.append(seq_record.annotations['topology'])
    date.append(seq_record.annotations['date'])
    if "references" in list(seq_record.annotations.keys()):
        ref_count.append(len(seq_record.annotations['references']))
    else:
        ref_count.append(0)
  

final_res = {}
final_res['name'] = id_list
final_res['id'] = name
final_res['length'] = length
final_res['sequence_version'] = sequence_version
final_res['description'] = description
final_res['comment'] = comment
final_res['organism'] = organism
final_res['molecule_type'] = molecule_type
final_res['topology'] = topology
final_res['date'] = date
final_res['ref_count'] = ref_count

res = pd.DataFrame(data=final_res)
print(res)

res.to_csv('genbank_data.csv',index=False)
        
    