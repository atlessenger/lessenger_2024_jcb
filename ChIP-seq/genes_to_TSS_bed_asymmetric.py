import sys

def run():
    if len(sys.argv) < 5:
        print('usage: python3 %s input_bed chrom_sizes output_bed us_radius ds_radius strand_col % sys.argv[0]')
        sys.exit(1)
        
    inbedname = sys.argv[1]
    chrom_sizes = sys.argv[2]
    outbedname = sys.argv[3]
    us_radius = int(sys.argv[4])
    ds_radius = int(sys.argv[5])
    strand_col = int(sys.argv[6])
    
    ## get chromosome sizes to set maximum position on chromosome
    chrom_info_dict = {}
    linelist = open(chrom_sizes)
    for line in linelist:
        fields = line.strip().split('\t')
        chr = fields[0]
        end = int(fields[1])
        chrom_info_dict[chr] = end
    
    ## convert bed file of gene bodies to range of TSS-us_radius to TSS+ds_radius
    listoflines = open(inbedname)
    lineslist = listoflines.readlines()
    outbed = open(outbedname, 'w')
    
    for line in lineslist:
        outline_fields = []
        
        fields = line.strip().split('\t')
        Chr = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        strand = fields[strand_col]
        
        if strand == '+':
            outline_fields = [Chr, str(max(start-us_radius, 0)), str(start+ds_radius), fields[3], fields[4] , strand]  
        else:
            chrom_max = chrom_info_dict[Chr]
            outline_fields = [Chr, str(end-ds_radius), str(min(end+us_radius, chrom_max)), fields[3], fields[4], strand]
        if len(fields) > 6:
            outline_fields.extend(str(i) for i in fields[6:])

        outline = '\t'.join(outline_fields)
        outbed.write(outline + '\n')

run()
