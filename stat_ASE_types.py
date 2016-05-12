def drawbars(statsGeneTable):
    Total_gene = 42189
    f = open(statsGeneTable)
    firline = f.readline()
    SMinfo = firline.split()[3:]
    SMname = [SMinfo[i].split('_')[0] for i in range(0,len(SMinfo),2)]
    Mylist = map(list, zip(*[i.split() for i in f]))
    gene_info = Mylist[2]
    SMlist = Mylist[3:]
    SMorien = [SMlist[i+1] for i in range(0,len(SMlist),2)]
    for i,j in zip(SMorien,SMname):
        ASESNP = len(i)
        print 'Sample name: %s'%j
        geneLS = []
        genedic = dict()
        for m,n in zip(gene_info, i):
            if m != '.':
                if m not in geneLS:
                    geneLS.append(m)
                    if n == '.':
                        genedic[m] = set()
                    elif n == 'P1':
                        genedic[m] = set(['P1'])
                    elif n == 'P2':
                        genedic[m] = set(['P2'])
                    else:
                        print 'check!'
                elif m in geneLS:
                    if n == '.':
                        pass
                    elif n == 'P1':
                        genedic[m].add('P1')
                    elif n == 'P2':
                        genedic[m].add('P2')
                    else:
                        print 'check!'
        ASEgenes = 0
        P1ASE = 0
        P2ASE = 0
        P1P2ASE = 0
        f1 = open('%s_P1_ASEgenes.txt'%j, 'w')
        f2 = open('%s_P2_ASEgenes.txt'%j, 'w')
        f3 = open('%s_P1_P2_ASEgenes.txt'%j, 'w')
        for i in geneLS:
            if len(genedic[i]) > 0: ASEgenes+=1
            if genedic[i] == set(['P1','P2']):
                P1P2ASE += 1
                f3.write(i+'\n')
            if genedic[i] == set(['P1']):
                P1ASE += 1
                f1.write(i+'\n')
            if genedic[i] == set(['P2']):
                P2ASE += 1
                f2.write(i+'\n')
        f1.close()
        f2.close()
        f3.close()
        print 'Total genes: 42189'
        print 'Total ASE SNP: %s'%ASESNP
        print 'Genes covered ASE SNP: %s. %s of Total genes.'\
%(len(geneLS),len(geneLS)/float(42189))
        print 'Genes with ASE: %s. %s of Total genes.'\
%(ASEgenes, ASEgenes/float(42189))
        print '\tP1 ASE genes: %s. %s of ASE genes.'\
%(P1ASE, P1ASE/float(ASEgenes))
        print '\tP2 ASE genes: %s. %s of ASE genes.'\
%(P2ASE, P2ASE/float(ASEgenes))
        print '\tP1P2 ASE genes: %s. %s of ASE genes.\n'\
%(P1P2ASE, P1P2ASE/float(ASEgenes))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        drawbars(sys.argv[1])
    else:
        print 'Usage:python stat_ASE_types.py statsGeneTable'

