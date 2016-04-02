from scipy import stats
from scipy.stats import chisquare
import numpy as np

expect_rate = np.array([0.5,0.5])

def ChiBinomial(aList):
    if '.' in aList:
        return '.'
    else:
        theList = [int(i) for i in aList]
        total = np.sum(theList)
        if total <6:return '.'
        else:
            observed=np.array(theList)
            cvalue, chipvalue = chisquare(observed, expect_rate*total)
            if chipvalue <= 0.05:
                return 'yes'
            else: return 'no'
def ZhengOri(aList):
    if int(aList[0])-int(aList[1])>0:
        return 'M'
    if int(aList[0])-int(aList[1])<0:
        return 'P'

def FanOri(aList):
    if int(aList[0])-int(aList[1])>0:
        return 'P'
    if int(aList[0])-int(aList[1])<0:
        return 'M'

def doStat(combineTable):
    f1 = open(combineTable)
    print'Chr.\tPos.\t3-1_Sign.\t3-1_Orien.\t3-2_Sign.\t3-2_Orien.\t3-3_Sign.\t3-3_Orien.\
\t9-1_Sign.\t9-1_Orien.\t9-2_Sign.\t9-2_Orien.\t'
    f1.readline()
    for i in f1:
        j = i.split()
        info = [j[0], j[1]]
        test31 = j[4:6]
        sig1 = ChiBinomial(test31)
        if sig1 == 'yes':ori1 = FanOri(test31)
        else:
            ori1 = '.'
        info.extend([sig1, ori1])

        test32 = j[6:8]
        sig2 = ChiBinomial(test32)
        if sig2 == 'yes':ori2 = FanOri(test32)
        else:
            ori2 = '.'
        info.extend([sig2, ori2])

        test33 = j[8:10]
        sig3 = ChiBinomial(test33)
        if sig3 == 'yes':ori3 = FanOri(test33)
        else:
            ori3 = '.'
        info.extend([sig3, ori3])

        test91 = j[10:12]
        sig4 = ChiBinomial(test91)
        if sig4 == 'yes':ori4 = ZhengOri(test91)
        else:
            ori4 = '.'
        info.extend([sig4, ori4])

        test92 = j[12:14]
        sig5 = ChiBinomial(test92)
        if sig5 == 'yes':ori5 = ZhengOri(test92)
        else:
            ori5 = '.'
        info.extend([sig5, ori5])
        print '\t'.join(info)

if __name__ == '__main__':
    import sys
    if len(sys.argv)==2:
        doStat(sys.argv[1])
    else:
        print 'Usage:\npython step7-chi-binomial.py combinedTable'











