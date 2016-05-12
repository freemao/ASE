import vcf

def filterHomo(input_vcffil,output, PList):
    '''e.g. PList=[L14-1, L14-2, L14-3]'''
    inputvcf = open(input_vcffil, 'r')
    invcf = vcf.Reader(inputvcf)
    out = open(output, 'w')
    for i in invcf:
        PGT = set()
        PGTlist = []
        for m in PList:
            PGT.add(i.genotype(m)['GT'])
            PGTlist.append(i.genotype(m)['GT'])
        if PGT != set(['0/0']) and None not in PGT and '0/2' not in PGT:
            out.write('\t'.join(PGTlist).replace('0/0','A').replace('0/1','X').replace('1/1','B')+'\n')
    inputvcf.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        Plist = sys.argv[3].split(',')
        filterHomo(sys.argv[1],sys.argv[2],Plist)
    else:
        print 'Usage:\npython filter_9311_Ch1073.py input_vcffile output p1,p2,p3'



