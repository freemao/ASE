
def findCommonPOS(vcf1, vcf1out, vcf2, vcf2out):
    vcf1POS, vcf2POS = [],[]
    f1 = open(vcf1)
    f2 = open(vcf2)
    f3 = open(vcf1out, 'w')
    f4 = open(vcf2out, 'w')
    for i in f1:
        if i.startswith('#'):
            pass
        else:
            f1pos = ':'.join(i.split()[0:2])
            vcf1POS.append(f1pos)
    for j in f2:
        if j.startswith('#'):
            pass
        else:
            f2pos = ':'.join(j.split()[0:2])
            vcf2POS.append(f2pos)
    commonPos = set(vcf1POS)&set(vcf2POS)
    f1.seek(0,0)
    f2.seek(0,0)
    for i in f1:
        if i.startswith('#'):
            f3.write(i)
        else:
            F1POS = ':'.join(i.split()[0:2])
            if F1POS in commonPos:
                f3.write(i)
    for j in f2:
        if j.startswith('#'):
            f4.write(j)
        else:
            F2POS = ':'.join(j.split()[0:2])
            if F2POS in commonPos:
                f4.write(j)
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 5:
        findCommonPOS(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        print 'Usage:\npython step3-common_POS.py vcf1 vcf1output vcf2 vcf2output'
