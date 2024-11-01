##############################
#
# Filter out genes from bed or gtf file
# Usage: python3 genes_from_bed.py bedfile gene_col_index outfile
#
# Alex Lessenger
#
##############################


import sys
import string

def run():
    bed = sys.argv[1]
    gene_col = int(sys.argv[2])
    outfilename = sys.argv[3]

    outfile = open(outfilename, 'w')
    lineslist = open(bed)
    i = 0
    
    for line in lineslist:
        i+=1
        if i % 100000 == 0:
            print(f'{i} annotations processed')
        if line[0]=='#':
            continue
        fields = line.strip().split('\t')
        if fields[gene_col]=='gene':
            outfile.write(line)

    outfile.close()

run()
