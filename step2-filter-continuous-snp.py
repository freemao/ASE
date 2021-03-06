import re
def parent_filter(myvcf):
    f = open(myvcf)
    for i in f:
        if i.startswith('#'):
            print i.rstrip()
        else:
            REF = i.split()[3]
            ALT = i.split()[4]
            POS = int(i.split()[1])
            if len(REF) == len(ALT) > 1:
                startInfo = i.split()[0]
                middleInfo = i.split()[2]
                end = '\t'.join(i.split()[5:])
                cigar = re.findall('CIGAR=....',end)[0]
                endInfo = end.replace(cigar, 'CIGAR=1X')
                idx = range(len(REF))
                for m,n,k in zip(REF, ALT, idx):
                    if m == n: pass
                    else:
                        line = startInfo+'\t'+str(POS+k)+'\t'+middleInfo+'\t'+m+'\t'+n+'\t'+endInfo
                        print line
            else: print i.rstrip()
    f.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        parent_filter(sys.argv[1])
    else:
        print 'Usage: python parents_filter.py vcf_file'
