# each rucksack - 2 compartments
# missplaced exactly 1 item per rucksack
# list of all the items - input
# item = a single letter(in lowercase differ from uppercase)
# list of items for each rucksack - > all in one line
# a rucksack always has the same nr of items in each of its 2 compartments
# to prioritize item rearrangement -> priority (lowercase a-z = 1 to 26)
# uppercase (A-Z =27 - 52)
# priority = placement of the letter in the alphabet
# return the sum of the priorities of these items (the repeted items)

import string


def splitStringinTwo(value):
    string1, string2 = value[: len(value) // 2], value[len(value) // 2 :]
    return string1, string2


# print(splitStringinTwo("jNNBMTNzvTqhQLhQLMQL"))


def findMisplacedItem(str):
    # to change this into ASCII
    priority = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }

    # part 1
    # counter = 0
    # for i in str.split("\n"):
    #     left, right = splitStringinTwo(i)
    #     for j in set(left):
    #         for k in set(right):
    #             if j == k:
    #                 counter += priority[j]

    # part2
    counter = 0
    alphabet = string.ascii_letters
    # print(alphabet)
    lines = str.split("\n")
    for i in range(0, len(lines), 3):
        a, b, c = lines[i : i + 3]
        A, B, C = set(a), set(b), set(c)
        for x in alphabet:
            if x in A and x in B and x in C:
                counter += priority[x]

    print(counter)


findMisplacedItem(
    """jNNBMTNzvTqhQLhQLMQL
VCwnVRCGHHJTdsLtrdhrGdsq
wFJZTbRcnJCbpwpFccZCBfBvPzfpgfgzzWvjSzNP
wDWgDfWNTvwvgFfWfddGldJVprrrVdNlrN
nLnmLSnmMVJvSrHqdV
MsmsbLvtzMjFsCPDsfBwwT
WTqSCqWSWqSgVZqJHpHmHrhMMVrRhBnn
PtLGLGddGGMCpprM
jFvLPPlLjvfjjffsclvPqzzJWTbqNSWZsbSTDzCW
lLSSrfmddlNpnmLdfSPddDdbZQTZgZjbZgjcQZHQPjQgZP
MJMnhzBJVJwvGsMRhRhTsHTjZjHFctbtHZcgZj
vzvBWGJMVGwWGGhGqVBnGzVGDfCDmrqNfrrLSdpSfLSpNmNC
qGWLgfbWhqpLgZbJvTRWJTvMWRslMv
FQwPwNPCVFQQdNcFHNcwwsvslRDRTMDMsVTGJGtRTs
wQHnwnQFPNPdjnnPjhphGqBrfpBBBfZf
mpVpmtPhVtPBLLbQTJpBLZ
vzFMlMzvvRZMTbJQJQbf
srqzvRRqdvzFFrDnvqldFVtwCVCHWNqJHNNcHchCPt
CQJJLZCJLqNMMDDgGLVV
RfRFFszTtzbWTFnRtFrRrWvNHghvBVGgMffvmBVDNgGV
znsjWzstnWjbDnDbTZCpwZcjpjZqQCwSPp
jRrzzrPjLnnpQQDsjj
CTVnTlZWHTcqZBcTTTHqWscQsQDQQDsmmQfvfhwDmv
qlWFWWHTZTlqTFWZHtBVFdlTGdNzRnNngbbSrrSNNzPgPGSz
cWjbcjnssMmRPWbGsWcMbfLBFrZBBLLgZwBrlfLQZtCw
vqpvFHNvhvJzdZQZtlgNNwlrrw
JzqVVVVpzhVJqzhSzJhhDVnFjRRMsPnSRcGMRMjWjWmR
NznNGQgSRQffbbsR
jjjCLwdvLcrhqdblFJsFSPfbDP
qrrvwHqjtLmSSggpBtgn
LGPtFtTfTfTfLrrWTSWGPrrsszbsjZHzgdzSwzbHdsglwl
NhHpVpqNNqbdszRRRb
ccBMJVDNCvvhDNpvNDpnNCVCHFPTmfLTGPMQrfLGmMLWWQQL
dRgRhVLRlncZSSrtLp
WJmwvvvjQvWwFBBvFJPHpwvGWTScGsrZtttGTSsrzTsSZt
FFHJjmjjjPMvfHfwpdRqMppghdRCddDg
NDTRFSnNsVVBDVlM
JjLZWqwjHvfrvmHHvjLWWLlhPlnPlChlQhJQnnzPPBCV
mwHvHmpvwpLmjnvpvLvvNGcTTggRbdTGcbNbTTpS
GGhZQMsmGRfMwfpclgdBlbblBBZgJc
tFvFSTSDnDTTLtcFMbWcBgclJrgd
vzDtzMVtnLTTMTSjSDHtppqhsqqfGjmpPhmsRGPG
MfJtWTTMJfzBbVWPZWQbNnDV
FvlgSHSLvmCvZjgcCQQsPQQsjnbVDNVsdn
HLhclRlHRmHvmLmclLZFSFwRRRpJMtwJwfGGrrtrwfpf
scsswLQcGmQmNHCqvrsHqfff
bdnPSMMMClbBBPCdDDnDVMDWWWvfvWFfFJfNqqNVFqFNfr
bDPTlSTPPbSPjnPSbGmQLCcjLjwzRLcmCG
tFFJjMnFhdcMMJlWtdnlFczBSZGNSjGGbBGZLbZZbLGB
QRgqwwvsLssZnGCz
gqfvvnpfHwRmHTFdFcPdJJmJJc
fccTzVVcfSmdThTTFJPFgg
wLsWfppsjBrnnwjCBZnZqJJQGhBdFJddQhFqdQBG
pZrNCWLwLZLjwwWMftmNzttDcVzVvt
rZnVVjVSMcrwsNbc
dLvQLBLFddvBLzpGmddQCqNswzsMjbhgbblbcwshlb
LLCCWjGBFPmCWdmmPWLdWBpLRZDSPRnHSStRfnZnZTnSSTfJ
ddfnQRbpldRlRLgFglqGCLqsGq
BWBVDZWTBTDPvVTZVDBDNMbhcLLHsFqgvHJsLCJCGcHGsJLH
NPZPDMWZMbZrBVMDDWNmBhMVpSSRpzjjfjpwRnSpwzRzdzjr
bvPSBttgGmZwScwShS
NJspjJLdprzHgjrLzLNrnHQCmmcZQWlcQcNQwlwcQCZC
HdRJsJrdHTbqGMDtgDqT
sNVvSdTstDCtdzdzSCwTzCRhRQjfclMflppjGhffjZcN
rgWlrnLLbqbQMfMphpWjjf
BmrnrFPnnBLlqVwDCtCtVPDTzT
mJMqlVlttQlFVmzFQMQMbQMSSDNwwdSddNddwdDswRDVdR
GGZgcfjrvCCZvgCZqvPHSwRBBsBwswcwBNTDTcSR
GZppfGHGrgGprZhLthFJhFqLWWFhtq
WDHHLtRBHgDnVrWFVFBTdzzZLLjZzjjvddLsvv
JlqmMpCMCGMwbwZddTtCtv
cJJqSplpfSGccJGthFVcVHgFBWBgHgDB
tlFwbWtQFLJhlBFlWPbwmsQndTrrqdnggjqdgnTgTT
GCMBDDCvRpDVpRpHrsgdqTjqgdHcsjHd
MDDvCVGzBGfpzBSNMSRRmwbLWlPmzbPmlJlWbFbJ
fzFzFHBfnvpHFbnzbHfBHZggCGgtZCltDGggdCCVtZVD
sLMNSccQLMSrmLcshLvtCGllPtDdGgtJgmlV
cwLMwwNhQhsWSjqTqHnHbjWTvH
NWlqqhNNnGtNvvWQdrVGBBQdVrwRQr
mppCjppMrDTSgDppCDTMQVRwdBbBQVVbQdQsVB
pgzzTFFFrjHqHnqJFWnh
ncQrhQjqjVQhGsGBbhtsstTp
RllWFLRfZrGlBTbg
vFLLmfNRFSNDfSNjcwqJVrVVzQjc
mmGrgwmGDGcVWVjNNW
nDsqfPCHnpntDssfJPDPjWWhjNTTcjjhTTNcqWcc
DfPCJLpbldRrlrdwmw
dJDNbRhNbJdhqCnrWjhsTWvplg
LMHrttLFcMmcMFLmtGplCggpjjnvTpgnTTFT
czZMzrzVZzHZdNdbDDqDVQNR
sbsJgbsmzdgRgWdg
LLLFBzGMLjzzFtVFwwwCPPRCCqQQTnnCMMCMCC
GllfptwjLjlGFVFjGzpFFNbJDmprrNDsDmDvJhmcvp
SccPbfbncpcfsjbRjMBCTTFGMTCQtJtzFFFJ
vvvdgVhlmlwlgZLgmJhWQCWGGbWtWJhzTJ
NbLNDdbLVmqqmfcsrHcrpPqrcH
HcgDBJSHTCzjjnMNJjrW
VppGMwFwllwwbZZrjvnqmzmnzpqjNv
wZlhtPGPLFVFlGZbVtVTQLLBQRRTSHTSMDCgLs
HPMMnhBHlMnMBPBHJHPWfdnBmjvLZvjTvZTZDgTgTmQmZhZZ
SrzrSScrctrwVzCSCmzQjmLTLvGDvTjGbm
CswstFRNpcwVNRrVVSVwpwpHJnnWWBBHfWHlffWfQMnM
mlFMtqjvMdqjmMCCJZsRQBnszlZz
HcNgcPLcHLwtcfZBTsnsHJBJTzCQ
LGGNhbNtNLDfcgcwfbgthfwFrqqVdFMqMMhMmvShFqmvVv
NbvbBGNvhNhnhpbgpGfBvNgmRjCdPCPCCRCQmmpRdTmTPR
qqFSSqWrtSSccjMdQMHFMBjPMj
SBDSBZZZwGGZNJJg
qTdHSLSFRZRHHZVgpzhbJszchsnsLg
tDvflvrGttDCjlQfmCGvtCftczhbzwJczcJgznNmzJNhwgsp
tQlDCDtrfrtlGrjlQBHFHPVHbBbZqTZdVZBF
MTwvsQJMvvHwVMMJMQNNJRPWWjCllrlWGFlSFCpjgFVSWr
zhcmnRZmqmWjCSFrFqCW
ZbmhZcdZznZfndtwDtMMsRQTTQNRQw
ZhhVqQTvZvVhSmQZcClRCLPCgTGGLbgl
dJWHwndMHswswlGbCmclmLHbbP
dnwwNJnjBjwwdddnjndfWvmvSNZQNrVVmZvZFvvQQv
trlrlrZzsjRjdFhlpwdpnpdp
QqLvvLQmLfQTLbLTfHmqHHLqQgFBdCJBBgggCJdhgJwCggBF
DPDvqLqffqfhSVjVPSPtsj
gsnVdcBcjMMntGMh
RQZLRZlZDRJDCzCjblJSDjQZWWTWPCThMTFGNPTNttGwCFMh
pDlQbSlzpQsjVpjHVfgs
zgqtCtJltdGttJgVGPPJCtJvQFsFFbTFssNDNDsHLbTQbssP
rRcwBnnpcmBqpbLHDspTbFsb
mwRqrqrmWrZnfWmBmnRZlgClgJCJlGJzClGMtG
jlzHllmPnpHlHZBWZJJDWMBNVH
bQrhDbcLgsQrtdVCJWfCCBMMVWrJ
QhGdGcLGwwwtcDzznppPpPwlpnSS
qbpqvWFHbFHHsWwPqPpsVWZTlDcLDddddDrmrcVZDrmT
MCgSSJMCztdmcLzlrlDl
QCRMRSnNtRSqqRjsjLPPvp
ZnZrTfsWWvhVSRmzqqnn
pLGBLBgLCpgGpbdLbgMClJTmmhShSRShqSBDQSRRmQVV
dpJPldgMMbglFdrNWWjHZNccTjZP
CCZCQzwwdmMGDWMmhCMJgpnrnwsTrFNLgnpNgg
jfStHtcjqDPbPtvqvgLNpppnHsrsFgnFNp
fcqqPPPtPSfRVBBRPRPbvQzzhQWGZQVQQZDQMMzGQM
VVlDNDgppgtNltlrJPbjSzPPzjsMsjBBMWMM
LmGRmfmwCqQqbsQBMqJj
cHRcCFfmfmGLJLGFcJLFwfdlhDgptthhHpVrNVdhlvhl
vSSdnBVpscwZcBZB
mLHzqtGtNfGHHFNHMhJMthsbcJtctZTw
GHqHHGzNDNFCfqllCFqVDdPSDQnddvcpPQjdjg
CMWcwGTrvzDWzrDccDCGzTTTplZgSjggjSpSljSjBpSmgmWB
nssRttdsnhsdbFhtVFhNpgwNpBBgHHBBBBZSjNSl
PnVPVPLFtvPvTwwrQq
tlQlqlJCCJWgFrprPjpGVpQzvp
SDbwShHbBZZbhcBdDBDSTrsVpPrzzzHVzNllzGlVNv
BTbbScwRhwZLnLtfJFLFJgWl
VDfPVHfDVMMfHSPSMTVfqgFthFcFrtcdhrhDQdDmdcdt
bWGGHCplWnJNpJCCnlnNwdcwQhmmdmtwddBNcc
HpGCnZGllzlzJWjnCbbnCnRvfvsSTVVSgVLqSsLsLzPPLV
fQqcfqfSDzDWffDZ
NcCLCtPCPMtNBwdthpLhPwzsHrszsZssTsWrDrDVTNNH
twMPBtCpLBCtwMPpJcMBSjjnngqSjQQJbQjjmgmn
vQwVQQVqcJvVJvCpQBCLpdgSFCdjjWWnMSgnSjgjbj
hszPRDTVDWWWRnjWWj
TtDDZsszlPllhPzmPVGssTPpQLcpvpBpZpcfpvrvQvBQLv
sRmGqqzzzgCtRrttCP
cffSwNDddTdfGWtgNCrtGMPP
GGcTwHwHvjqLLjLvlJ
JSdjLJMBdMSrfwwLpWgzWmvDhggzWvfmgD
VsRtVllstHHNllsQsHQRzchcnDmvmvnRvvvcnZ
tGVGCTTTtTFVbsTTNTHsTTqBqBLrBCjqBwqJwqBzLqzw
MhjTJjlSDrplQvFQ
RHttqbNGGmbbLmLmdqbgnFQwrZswQrwDpFpppdwfvQ
gCNmDHHRCLHnWWSCjhWPShPz
BvzpbBwBmsDrmGVgZFDm
TnNRdtlRlCdFFGTLffrrGf
jltNtRCPSlPNtcpwpGzjMBpvbhps
hflJphNDmmbpfnfplbcvLsHVLsrsZsVvCb
FgTFWqTBfFPfFqQqTwHsHccVVLQCZZZCVH
BSSRTGWBgFggBWgBGStTGpzNztmjjzhhzDfNnMjnph
mDDFjjFmVlTZJttffD
hhRvNNCvdNMRLzhSzpptwslNTfNQntsJQZZTlN
WCdMzdMzhMdvRvLhCRLPvjgHmggmbmbblgWcGmcbcG
cScMdhsDhDDdvGzZptzGcnGtpB
NPWjJqrjJWwrSFWRJlrlNWJLtZznLBBzZznLqnpqnpnznV
NWNQwNPjCSQTQhTd
fVVCVccppZMZMMCBzJTNJHWZTWZzNF
QrmmPhDqPhsPRhrlbgRDbbPDJNJTnJzmzzfNNTNHNJNWmnvF
DgbPLbPsQsrbsqLbgllsQQptfwSjwtVLfwdcpCjVwwSp
ZlsmlrZZJcQmhBhlNrsrJRRbRCRggRbzGCRHgRCDGB
fMFvdfVTTdjWTTTfvSjVjpjzcCbFHGPHPDbPHRCFGGRHHG
cdvfSWjfjpdVqSwSvMdLrlrmhqZhhrrLLJQhNr
sWVVmDJsNWNjcSNJZcNcZWWsHTGHTChhHGtHsFFbbsfHhH
nqPRwQRgpQRPQQgMQgQLQqBhvTRtfdfvfCbFtTFFFTtvff
qgrPMLLPpVlbDrVrWD
VcGjcCHcVHPrGnjQDQgDgQDFtdglRtlQ
bWWhfzJhvZWJzNpmRTtsDLDgRTsNddFT
MhJMhJbMmSZbJZwSCtjqcGrrnGjC
FCvpgDsZNsCbvvvpVwcDrjcrmVMwVwHJ
fhfWdPhhhhRQQqzdLSRHRHJjBTTmcrTMrMrwmczcwwTz
qndhdQWndftfhWStfLQQfWgFNsgFpHCtgCNbGZZlZCll
mqTCNhTNmGTLwLNfLrSrgZHDvfPDPv
cjsMQppsFnFslnRQQGMDHGZHSgzHPDZDSf
stWFjcFFsJlQcQtwtbVwCmCthmBTGb
fmsffcqhmqPsnTCnCcQpzjSSNpBWBTQpVSSD
vHbgLRvvvzdgjVVjWg
WltLWvWlqcChrhlf
CtwjffWrdznRtzCwLsmGLlLMsMmMGb
cZFFbgPgJZDchMMPVsmlPGmG
SpNFJBJccNgDcTJJTdbStbnntrCdSrjWnb
qWzgNFqzqHNTBzFNCZCGPpPlHmdPblls
rfSJRJnhhnJDjrfvRStCmpdGsdlDpZZZPbPCmW
cffRvfnnVRjFTWVTLQMFWN
VcHhVrVCQQWhffzcRZznnZFf
dDSCGSsSblwDdmLqvnFZzNZplfpfRZfBnl
tCCwGmSqbqtwsVPjVJWtJHHhQV
fvvTcWzGcCJrJGJvvHMbZTmRQTbpMdQQsR
SgFhVgllLgjLgwlwljFqVFSFdjmBHmZdRMdZpbjpmpjBsHdM
LNqFnlDgVqllwLFLnVSgLFZtCzzzzvCGGccCCDCfvJrv
FczpzmSjVVpSQrzzcRpRcrwqMtJqwtvtLHvQwtLtnJMw
TvbGGbNfGCBBLHtJBHDZDMqD
shgdNTGgvNsflspcPjzVdmppczrV
JHLPLTsSllgSSPPSPLTRTdjCZGZDGGgCdqZtZCZdZt
mhFpnpFwqdGbdFDt
prpWcvnmhmpccBBJMJJlPWLHMDSDWW
GcMcjDbDMMjqHBHVlHvv
rLCrwNJCnwrZNLWQQwzQpRqQPlBRVVBRvvtHqf
zhnrnzdrCwLJCwzwCMGcbdFTscTmgcFlgc
cnwlFrdMsggblgsrMbncwrsWzjGBTjznBzWNzPzTzfjTzf
vvVVHSpQvvRQDJGGLWGfTLTBLQMN
hCmJqVvMSpqqChCJHDZrFsdhrtgFhttZZhts
sfDNqLNpqpzCzLsDqzbCVWRhjTNhShTjHmmjjhStBmvT
wZrlwJwFJGlFMTjhBBZTSTRSbv
wrQrgnPwMsnLbfffVc
hDcwwGWhMMssTcdM
NQmLbNSZHQSHSNpbvfdqfRsZMqssjqdd
LNVtLSSHLSgLNrgwJgJGnBwFMBzD
CRDfCbfjcnRCBVfjVMfMjZpPptplPWtppStpSlBqlq
HdTFLGsdLrzNWtvqPTcpgPZl
JLGmmHrwJGwhjmfMcbDjQC
VShGpPbWjcPCcTLcPN
HqfqDfDFFJDvZRJvqZRRqHZdNcwjllwvQQLQlllccwclCMCT
FddsFmJjjrgGmbSSpS
NRFFLtFtqFLGsdnGbQSs
ljMfMBDlJHgBVHgVflfnwdsSQQbddsSsqnqGfs
PlzDzjljzqRzWzZW
dtzZZbctPzwdlzRwlcdfRgtQJmFmhPSmmSsQQFhsmqSFvm
nDjHnNjjjMnfjNTMWhHQWJSqSSQmhqhm
CDpVCfrjLnnfwtBcpdcbcBZt
sssZSZtDfHbbdtBTCRBzRDFJCBLp
jwWgmWlNQNLlcjWhgQlrQQWrCCJJzFCMVMTzpBMMCVCMTwpT
ggLgrqljLlGvHqttftbP
cSGBFsFcSRZSQGsgBNgVMwMhDQDVfqPjMhwwVq
vnCTLlrpPlHzzjbMfqpbww
rJCnlmClvWvLrTmtTlZcZWSSWPGGdNcFGgcR
lfDDvZZSvLtDtCQZltCqVBWVBCbHJjRdNqWq
pGGhhzMRcqMBqMdVBN
mzgwGrrwhThFGPmGPcFGpwStTfltfDftStDsQRsflDQl
LjnSjLZLBcbBdDqzND
rrfhfMRmpsghfrhGhgQrcPNtZcqNCqdCqPzcNZMM
ZTTgvRpmfffpfgRRhWnVSJJLLWnvJHFlFH
lstcGcttdczzsWVCvQVLCHHnQHWL
rjmJrmfmJMqvQTLvqfGG
JbNrjGjGrMDRJghZggcchhDhzc
tftJQwCgSjpdWHjbRJ
DcwvlZBmGvHjdbczcRpb
sqwDlsBvGNSMQTCNfCTC
DwDrtvMHtBCvcpDcjCMFtBCblJfJGJbZlfzrRlJdbRdZld
sPLPmqhSnLQQSWqlbzRRhfJCJfNJhZ
mVCnWCsQqqLTPWmnDVMFVtHFtMBFpjwM
scChGddJztdNswNsdDsthvmpVmRVcZjmvVvRSMZVSZ
lQLCWgWHCWbFPbbbHqLnLPHHVMpVRgSMmZVSBZBjZVSjRBZp
QrTlTHbPnTsJGtsDdGCr
fMjgFqtFWMhtjcNQSDMmNlCCDMQN
sVHdHdJHwPGPGwwbpJGTbGTvClldmvRSnvlDlLLSlvRnQl
pJbHPHJGVbBswpTcfrBtrhmtrFczzq
SDGSDGVPqqqQPGrTQVTQDrSrJfHJgqhgJqzhJJmWfHpWpzmg
twCdCWMLwbtLLjBddgfcJgRHfRRpfcpRHM
FZdbvFFbVvsWsQsW
rzrRgqGrwgjRVqJCHLzCCWhtDbCC
dTZnNpvBvnJdBpBnsJPvsSCbthLtLbbQShQQLHtSST
BlplPmdlFsslfJmmRfwfwMjw
PPHSrmfHTnmHnHBzRhbFgfbFwzQg
LcsVsGtVLtLqpzwBvgzQRgTTTp
TjLJGTTJWJZZWWZS
tHcshJcJRhLsQscVtccJLRHfvlPjZFSvmvSbvfLFfFFbGZ
drwdTNlwwBTpCdCdwGPrrmjjmjmbSjFPrF
wglnzCDpJtQcztMR
bbMjTbBvgjZNSqldTlVt
wwrcFwsrsnnCQzrCsLnRsQZcNlpJVZHdttZVttSZqJZd
GwLnrsmFCCzqzhvPbPmWmvvfjj
dcnwQdcdrJdSwSFBBqfBfwMqfBfzsh
RgmZpWlCClRlTgBZbhHJJsZjfBHZ
DlNVWgWpgDCCNRDJFcrtQGrrVnrcFPtc
sWSHsdSrHWHsbdsddBsbjmfwffmJDJwcfDQgfvwJDj
ZNGPhRqCCRNGNwSDvmmwwgDhgf
lGlTLTGTSVVFqVTqsFHWntbWBsBsnBHb
QRRgRvDwWDVjmSbDnbTDlDnbqS
rHCPPHrcLFJcllqbTlpq
CldFrNFsgVhhhWgN
qSfMgNqfpmSmlQrRFG
cbBczbtbZTcPWzcrTrmRrLGFTQQFmJ
PBZChtzzcWPcZtBvPjtzBBCfHMMNdDgDpMfVfVpHMqNR
LJPPCHtgtLDfFfvTLwfv
pVGWGGjjjplhpGGVjWnldsvrrMFvfDMTWBdFrfFF
cjlhShjchhjGGmNVjplcQgmTPtHPPJmQgQHgtqgZ"""
)
