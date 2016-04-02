import vcf

def judgeParentsGT(P1GTlist, P2GTlist, ref, alt):
    P1GTset = set([i for i in P1GTlist if i])
    P2GTset = set([i for i in P2GTlist if i])
    if P1GTset == set(['1/1']) and P2GTset == set(['0/0']):
        return alt, ref
    elif P1GTset == set(['0/0']) and P2GTset == set(['1/1']):
        return ref, alt
    else:
        print 'check!!!'

def judgeF1Count(P1base,P2base,ref,refcount,alt,altcout):
    if ref == P1base and alt == P2base:
        return refcount, altcout
    elif ref == P2base and alt == P1base:
        return altcout, refcount
    else:
        print 'check!!!'


def filterHomo(input_vcffil, P1,P2,F1):
    '''e.g. P1=[L14-1, L14-2, L14-3]
    P2 = [L17-1, L17-2, L17-3]
    ZH = [L9-1, L9-2, L9-3]
    FA = [L3-1, L3-2, L3-3]'''
    inputvcf = open(input_vcffil, 'r')
    invcf = vcf.Reader(inputvcf)
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'%\
('Chr.','Pos.','14_base','17_base','3-1_14count','3-1_17count','3-2_14count','3-2_17count','3-3_14count','3-3_17count',\
'9-1_14count','9-1_17count','9-2_14count','9-2_17count','9-3_14count','9-3_17count')
    for i in invcf:
        info = []
        ref = i.REF
        alt = i.ALT[0].sequence
        chromosome = i.CHROM
        position = str(i.POS)
        info.extend([chromosome, position])
        P1GT, P2GT = [], []
        for m,n in zip(P1, P2):
            P1GT.append(i.genotype(m)['GT'])
            P2GT.append(i.genotype(n)['GT'])
        P1base, P2base = judgeParentsGT(P1GT, P2GT, ref, alt)
        info.extend([P1base, P2base])
        for k in F1:
            q = i.genotype(k)
            refcount = q['RO']
            altcout = q['AO']
            P1count, P2count = judgeF1Count(P1base,P2base,ref,refcount,alt,altcout)
            info.extend([str(P1count), str(P2count)])
        newinfo = ['.' if x == 'None' else x for x in info]
        print '\t'.join(newinfo)
    inputvcf.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 14:
        p1list = [sys.argv[2], sys.argv[3], sys.argv[4]]
        p2list = [sys.argv[5], sys.argv[6], sys.argv[7]]
        f1list = \
[sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13]]
        filterHomo(sys.argv[1], p1list, p2list, f1list)
    else:
        print 'Usage:\npython filter_9311_Ch1073.py input_vcffile output_vcffile P1-1 P1-2 P1-3 P2-1 P2-2 P2-3'



