def addgene(gfffile, statstable, outputTable):
    genedic = {}
    f1 = open(gfffile)
    f3 = open(outputTable, 'w')
    for i in f1:
        if i.startswith('#'): pass
        else:
            j = i.split()
            if j[2] == 'gene':
                chromosome = j[0]
                start = int(j[3])
                end = int(j[4])
                name = j[8].split('=')[-1]
                genedic[name]=[chromosome,start, end]
    print 'total %s genes'%(len(genedic))
    f1.close()
    f2 = open(statstable)
    firline = f2.readline()
    head = '\t'.join(firline.split()[0:2])
    tail = '\t'.join(firline.split()[2:])
    newfirline = head+'\t'+'Gene'+'\t'+tail
    f3.write(newfirline+'\n')
    for i in f2:
        j = i.split()
        front = '\t'.join(j[0:2])
        behind = '\t'.join(j[2:])
        chr = j[0]
        pos = int(j[1])
        genename = '.'
        for k in genedic:
            if ((chr == genedic[k][0])
and (genedic[k][1]  < pos < genedic[k][2])):
                genename=k
        newline = front+'\t'+genename+'\t'+behind
        f3.write(newline+'\n')
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        addgene(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print 'Usage:\npython step8-add-gff3.py gfffile statsTable'
