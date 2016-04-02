def drawbars(statsGeneTable):
    f = open(statsGeneTable)
    f.readline()
    Mylist = map(list, zip(*[i.split() for i in f]))

    Total_gene = 42189
    threeone_SNV = Mylist[3].count('no')+Mylist[3].count('yes')
    print 'threeone_SNV:%s'%threeone_SNV
    threeone_SNV_ASE = Mylist[3].count('yes')
    print 'threeone_SNV_ASE:%s'%threeone_SNV_ASE
    threeone_SNV_ASE_M = Mylist[4].count('M')
    print 'threeone_SNV_ASE_M:%s'%threeone_SNV_ASE_M
    threeone_SNV_ASE_P = Mylist[4].count('P')
    print 'threeone_SNV_ASE_P:%s'%threeone_SNV_ASE_P
    threeone_gene = set()
    threeone_gene_ASE = set()
    threeone_gene_ASE_P = set()
    threeone_gene_ASE_M = set()
    for i,j,m in zip(Mylist[2],Mylist[3],Mylist[4]):
        if (j == 'yes' or j == 'no'):threeone_gene.add(i)
        if j == 'yes':threeone_gene_ASE.add(i)
        if m == 'P':threeone_gene_ASE_P.add(i)
        if m == 'M':threeone_gene_ASE_M.add(i)
    print 'threeone_gene:%s'%len(threeone_gene)
    print 'threeone_gene_ASE:%s'%len(threeone_gene_ASE)
    threeone_gene_ASE_only_P = \
threeone_gene_ASE_P - (threeone_gene_ASE_P&threeone_gene_ASE_M)
    threeone_gene_ASE_only_M = \
threeone_gene_ASE_M - (threeone_gene_ASE_P&threeone_gene_ASE_M)
    threeone_gene_ASE_MP = threeone_gene_ASE_P&threeone_gene_ASE_M
    print 'threeone_gene_ASE_only_M:%s'%len(threeone_gene_ASE_only_M)
    print 'threeone_gene_ASE_only_P:%s'%len(threeone_gene_ASE_only_P)
    print 'threeone_gene_ASE_MP:%s'%len(threeone_gene_ASE_MP)

    threetwo_SNV = Mylist[5].count('no')+Mylist[5].count('yes')
    print 'threetwo_SNV:%s'%threetwo_SNV
    threetwo_SNV_ASE = Mylist[5].count('yes')
    print 'threetwo_SNV_ASE:%s'%threetwo_SNV_ASE
    threetwo_SNV_ASE_M = Mylist[6].count('M')
    print 'threetwo_SNV_ASE_M:%s'%threetwo_SNV_ASE_M
    threetwo_SNV_ASE_P = Mylist[6].count('P')
    print 'threetwo_SNV_ASE_P:%s'%threetwo_SNV_ASE_P
    threetwo_gene = set()
    threetwo_gene_ASE = set()
    threetwo_gene_ASE_P = set()
    threetwo_gene_ASE_M = set()
    for i,j,m in zip(Mylist[2],Mylist[5],Mylist[6]):
        if (j == 'yes' or j == 'no'):threetwo_gene.add(i)
        if j == 'yes':threetwo_gene_ASE.add(i)
        if m == 'P':threetwo_gene_ASE_P.add(i)
        if m == 'M':threetwo_gene_ASE_M.add(i)
    print 'threetwo_gene:%s'%len(threetwo_gene)
    print 'threetwo_gene_ASE:%s'%len(threetwo_gene_ASE)
    threetwo_gene_ASE_only_P = \
threetwo_gene_ASE_P - (threetwo_gene_ASE_P&threetwo_gene_ASE_M)
    threetwo_gene_ASE_only_M = \
threetwo_gene_ASE_M - (threetwo_gene_ASE_P&threetwo_gene_ASE_M)
    threetwo_gene_ASE_MP = threetwo_gene_ASE_P&threetwo_gene_ASE_M
    print 'threetwo_gene_ASE_only_M:%s'%len(threetwo_gene_ASE_only_M)
    print 'threetwo_gene_ASE_only_P:%s'%len(threetwo_gene_ASE_only_P)
    print 'threetwo_gene_ASE_MP:%s'%len(threetwo_gene_ASE_MP)

    threethree_SNV = Mylist[7].count('no')+Mylist[7].count('yes')
    print 'threethree_SNV:%s'%threethree_SNV
    threethree_SNV_ASE = Mylist[7].count('yes')
    print 'threethree_SNV_ASE:%s'%threethree_SNV_ASE
    threethree_SNV_ASE_M = Mylist[8].count('M')
    print 'threethree_SNV_ASE_M:%s'%threethree_SNV_ASE_M
    threethree_SNV_ASE_P = Mylist[8].count('P')
    print 'threethree_SNV_ASE_P:%s'%threethree_SNV_ASE_P
    threethree_gene = set()
    threethree_gene_ASE = set()
    threethree_gene_ASE_P = set()
    threethree_gene_ASE_M = set()
    for i,j,m in zip(Mylist[2],Mylist[7],Mylist[8]):
        if (j == 'yes' or j == 'no'):threethree_gene.add(i)
        if j == 'yes':threethree_gene_ASE.add(i)
        if m == 'P':threethree_gene_ASE_P.add(i)
        if m == 'M':threethree_gene_ASE_M.add(i)
    print 'threethree_gene:%s'%len(threethree_gene)
    print 'threethree_gene_ASE:%s'%len(threethree_gene_ASE)
    threethree_gene_ASE_only_P = \
threethree_gene_ASE_P - (threethree_gene_ASE_P&threethree_gene_ASE_M)
    threethree_gene_ASE_only_M = \
threethree_gene_ASE_M - (threethree_gene_ASE_P&threethree_gene_ASE_M)
    threethree_gene_ASE_MP = threethree_gene_ASE_P&threethree_gene_ASE_M
    print 'threethree_gene_ASE_only_M:%s'%len(threethree_gene_ASE_only_M)
    print 'threethree_gene_ASE_only_P:%s'%len(threethree_gene_ASE_only_P)
    print 'threethree_gene_ASE_MP:%s'%len(threethree_gene_ASE_MP)

    nineone_SNV = Mylist[9].count('no')+Mylist[9].count('yes')
    print 'nineone_SNV:%s'%nineone_SNV
    nineone_SNV_ASE = Mylist[9].count('yes')
    print 'nineone_SNV_ASE:%s'%nineone_SNV_ASE
    nineone_SNV_ASE_M = Mylist[10].count('M')
    print 'nineone_SNV_ASE_M:%s'%nineone_SNV_ASE_M
    nineone_SNV_ASE_P = Mylist[10].count('P')
    print 'nineone_SNV_ASE_P:%s'%nineone_SNV_ASE_P
    nineone_gene = set()
    nineone_gene_ASE = set()
    nineone_gene_ASE_P = set()
    nineone_gene_ASE_M = set()
    for i,j,m in zip(Mylist[2],Mylist[9],Mylist[10]):
        if (j == 'yes' or j == 'no'):nineone_gene.add(i)
        if j == 'yes':nineone_gene_ASE.add(i)
        if m == 'P':nineone_gene_ASE_P.add(i)
        if m == 'M':nineone_gene_ASE_M.add(i)
    print 'nineone_gene:%s'%len(nineone_gene)
    print 'nineone_gene_ASE:%s'%len(nineone_gene_ASE)
    nineone_gene_ASE_only_P = \
nineone_gene_ASE_P - (nineone_gene_ASE_P&nineone_gene_ASE_M)
    nineone_gene_ASE_only_M = \
nineone_gene_ASE_M - (nineone_gene_ASE_P&nineone_gene_ASE_M)
    nineone_gene_ASE_MP = nineone_gene_ASE_P&nineone_gene_ASE_M
    print 'nineone_gene_ASE_only_M:%s'%len(nineone_gene_ASE_only_M)
    print 'nineone_gene_ASE_only_P:%s'%len(nineone_gene_ASE_only_P)
    print 'nineone_gene_ASE_MP:%s'%len(nineone_gene_ASE_MP)

    ninetwo_SNV = Mylist[11].count('no')+Mylist[11].count('yes')
    print 'ninetwo_SNV:%s'%ninetwo_SNV
    ninetwo_SNV_ASE = Mylist[11].count('yes')
    print 'ninetwo_SNV_ASE:%s'%ninetwo_SNV_ASE
    ninetwo_SNV_ASE_M = Mylist[12].count('M')
    print 'ninetwo_SNV_ASE_M:%s'%ninetwo_SNV_ASE_M
    ninetwo_SNV_ASE_P = Mylist[12].count('P')
    print 'ninetwo_SNV_ASE_P:%s'%ninetwo_SNV_ASE_P
    ninetwo_gene = set()
    ninetwo_gene_ASE = set()
    ninetwo_gene_ASE_P = set()
    ninetwo_gene_ASE_M = set()
    for i,j,m in zip(Mylist[2],Mylist[11],Mylist[12]):
        if (j == 'yes' or j == 'no'):ninetwo_gene.add(i)
        if j == 'yes':ninetwo_gene_ASE.add(i)
        if m == 'P':ninetwo_gene_ASE_P.add(i)
        if m == 'M':ninetwo_gene_ASE_M.add(i)
    print 'ninetwo_gene:%s'%len(ninetwo_gene)
    print 'ninetwo_gene_ASE:%s'%len(ninetwo_gene_ASE)
    ninetwo_gene_ASE_only_P = \
ninetwo_gene_ASE_P - (ninetwo_gene_ASE_P&ninetwo_gene_ASE_M)
    ninetwo_gene_ASE_only_M = \
ninetwo_gene_ASE_M - (ninetwo_gene_ASE_P&ninetwo_gene_ASE_M)
    ninetwo_gene_ASE_MP = ninetwo_gene_ASE_P&ninetwo_gene_ASE_M
    print 'ninetwo_gene_ASE_only_M:%s'%len(ninetwo_gene_ASE_only_M)
    print 'ninetwo_gene_ASE_only_P:%s'%len(ninetwo_gene_ASE_only_P)
    print 'ninetwo_gene_ASE_MP:%s'%len(ninetwo_gene_ASE_MP)


    tSNVgene = threeone_gene&threetwo_gene&threethree_gene
    tSNVgeneASE = threeone_gene_ASE&threetwo_gene_ASE&threethree_gene_ASE
    tSNVgeneASEP = \
threeone_gene_ASE_only_P&threetwo_gene_ASE_only_P&threethree_gene_ASE_only_P
    tSNVgeneASEM = \
threeone_gene_ASE_only_M&threetwo_gene_ASE_only_M&threethree_gene_ASE_only_M
    tSNVgeneASEMP = threeone_gene_ASE_MP&threetwo_gene_ASE_MP&threethree_gene_ASE_MP
    print 'tSNVgene:%s'%len(tSNVgene)
    print 'tSNVgeneASE:%s'%len(tSNVgeneASE)
    print 'tSNVgeneASEM:%s'%len(tSNVgeneASEM)
    print 'tSNVgeneASEP:%s'%len(tSNVgeneASEP)
    print 'tSNVgeneASEMP:%s'%len(tSNVgeneASEMP)

    nSNVgene = nineone_gene&ninetwo_gene
    nSNVgeneASE = nineone_gene_ASE&ninetwo_gene_ASE
    nSNVgeneASEP = \
nineone_gene_ASE_only_P&ninetwo_gene_ASE_only_P
    nSNVgeneASEM = \
nineone_gene_ASE_only_M&ninetwo_gene_ASE_only_M
    nSNVgeneASEMP = nineone_gene_ASE_MP&ninetwo_gene_ASE_MP
    print 'nSNVgene:%s'%len(nSNVgene)
    print 'nSNVgeneASE:%s'%len(nSNVgeneASE)
    print 'nSNVgeneASEM:%s'%len(nSNVgeneASEM)
    print 'nSNVgeneASEP:%s'%len(nSNVgeneASEP)
    print 'nSNVgeneASEMP:%s'%len(nSNVgeneASEMP)

    only9311 = threeone_gene_ASE_only_P&\
    threetwo_gene_ASE_only_P&\
    threethree_gene_ASE_only_P&\
    nineone_gene_ASE_only_M&\
    ninetwo_gene_ASE_only_M
    print 'only9311:%s'%len(only9311)

    onlych1073 = threeone_gene_ASE_only_M&\
    threetwo_gene_ASE_only_M&\
    threethree_gene_ASE_only_M&\
    nineone_gene_ASE_only_P&\
    ninetwo_gene_ASE_only_P
    print 'onlych1073:%s'%(len(onlych1073))

    Z9311Fch1073 = nineone_gene_ASE_only_M&\
    ninetwo_gene_ASE_only_M&\
    threeone_gene_ASE_only_M&\
    threetwo_gene_ASE_only_M&\
    threethree_gene_ASE_only_M
    print 'Maternal-Z9311Fch1073:%s'%(len(Z9311Fch1073))
    print Z9311Fch1073

    Zch1073F9311 = nineone_gene_ASE_only_P&\
    ninetwo_gene_ASE_only_P&\
    threeone_gene_ASE_only_P&\
    threetwo_gene_ASE_only_P&\
    threethree_gene_ASE_only_P
    print 'Paternal-Zch1073F9311:%s'%len(Zch1073F9311)
    print Zch1073F9311


tone = [11856,4523,2315,1883,325]
ttwo = [11358,4431,2257,1864,310]
tthr = [11864,4436,2281,1828,327]
tcom = [10904,1671,649,447,32]


none = [12018,4732,2547,1854,331]
ntwo = [12071,4664,2474,1860,330]
ncom = [11697,2677,1193,778,53]

uniq9311 = [171]
uniqch1073 = [275]
expressM = [35]
expressP = [22]



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        drawbars(sys.argv[1])
    else:
        print 'Usage:python step9_draw.py statsGeneTable'
