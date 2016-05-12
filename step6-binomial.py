from scipy import stats
from scipy.stats import chisquare
import numpy as np

expect_rate = np.array([0.5,0.5])

def Binomial(aList):
    if '.' in aList:
        return '.'
    else:
        theList = [int(i) for i in aList]
        total = np.sum(theList)
        if total <6:return '.'
        else:
            binopvalue = stats.binom.pmf(theList[0], total, 0.5)
            if  binopvalue <= 0.01:
                return 'yes'
            else: return 'no'

def Orientation(aList):
    if int(aList[0])-int(aList[1])>0:
        return 'P1'
    if int(aList[0])-int(aList[1])<0:
        return 'P2'

def doStat(combineTable):
    f1 = open(combineTable)
    header1 = 'Chr\tPOS\t'
    firtlist = f1.readline()
    headertmp = '\t'.join(firtlist.split()[4:])
    header2 = headertmp.replace('_P1COUNT', '_Sign').replace('_P2COUNT','_Orien')
    header = header1 + header2
    print header
    idx = range(4, len(firtlist.split()), 2)
    for i in f1:
        j = i.split()
        info = [j[0], j[1]]
        for m in idx:
            aList = [j[m], j[m+1]]
            sig = Binomial(aList)
            if sig == 'yes':ori = Orientation(aList)
            else:ori = '.'
            info.extend([sig, ori])
        print '\t'.join(info)

if __name__ == '__main__':
    import sys
    if len(sys.argv)==2:
        doStat(sys.argv[1])
    else:
        print 'Usage:\npython step7-chi-binomial.py combinedTable'











