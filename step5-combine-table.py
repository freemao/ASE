def combinCounts(T1countlist, T2countlist):
    newlist = []
    for i,j in zip(T1countlist, T2countlist):
        if i=='.' and j!='.':
            newlist.append(j)
        elif i!='.' and j=='.':
            newlist.append(i)
        else:
            if i == j:newlist.append(i)
            elif int(i)<int(j): newlist.append(str(j))
            elif int(i)>int(j): newlist.append(str(i))
            else:print 'Check!'
    return newlist


def combineTables(table1, table2, finaltable):
    f1 = open(table1)
    f2 = open(table2)
    f3 = open(finaltable, 'w')
    T1firline = f1.readline()
    T2firline = f2.readline()
    if T1firline == T2firline:
        f3.write(T1firline)
    else:
        print 'The first lines in two table are different!'
    for i,j in zip(f1,f2):
        T1base = '\t'.join(i.split()[0:4])
        T2base = '\t'.join(j.split()[0:4])
        if T1base == T2base:
            T1counts = i.split()[4:]
            T2counts = j.split()[4:]
            NewCounts = combinCounts(T1counts, T2counts)
            newline = '%s\t%s'%(T1base,'\t'.join(NewCounts))
            f3.write(newline+'\n')
        else:
            print "parents' bases are different at %s"%\
(i.split()[0]+'-'+i.split()[1])
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        combineTables(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print 'Usage:\npython step6-combine-table.py table1 table2 outtable'



