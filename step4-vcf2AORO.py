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
    P2 = [L18-1, L18-2, L18-3]
    F1 = [L4-1, L4-2, L4-3, L10-1, L10-2]'''
    inputvcf = open(input_vcffil, 'r')
    invcf = vcf.Reader(inputvcf)
    header1 = 'Chr\tPOS\t%s_Base\t%s_Base\t'%(P1[0].split('-')[0],\
P2[0].split('-')[0])
    headtail = []
    for i,j in zip(F1, F1):
        headtail.append(i+'_P1COUNT')
        headtail.append(j+'_P2COUNT')
    header2 = '\t'.join(headtail)
    header = header1+header2
    print header
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
    if len(sys.argv) == 5:
        p1list = sys.argv[2].split(',')
        p2list = sys.argv[3].split(',')
        f1list = sys.argv[4].split(',')
        filterHomo(sys.argv[1], p1list, p2list, f1list)
    else:
        print 'Usage:\npython step5-vcf2AORO.py input_vcffil P1 P2 F1'



