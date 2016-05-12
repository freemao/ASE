def divide2snp_indel(vcf, snpfile, indelfile):
    f = open(vcf)
    f1 = open(snpfile, 'w')
    f2 = open(indelfile, 'w')
    for i in f:
        if i.startswith('#'):pass
        else:
            REF = len(i.split()[3])
            ALT = len(i.split()[4])
            if REF == ALT == 1:
                f1.write(i)
            elif REF != ALT:
                f2.write(i)
            else:
                print i
    f.close()
    f1.close()
    f2.close()
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4:
        divide2snp_indel(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print 'Usage:\npython step4-divide2_snp_del.py vcf snp.vcf indel.vcf'
