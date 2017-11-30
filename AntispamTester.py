from __future__ import print_function
import os
import sys
import subprocess

SpamFolderName = 'spam'
HamFolderName = 'ham'

Dirs = os.listdir(os.curdir + '/Tests')

SpamCount = 0
HamCount = 0
SpamAccepted = []
HamRejected = []
HamFailed = []
SpamFailed = []


for TestFolder in sorted(Dirs):
    SpamList = os.listdir(os.curdir + '/Tests/' + TestFolder + '/' + SpamFolderName)
    HamList = os.listdir(os.curdir + '/Tests/' + TestFolder + '/' + HamFolderName)

    SpamCount += len(SpamList)
    HamCount += len(HamList)

    SpamList = [w.replace(' ', '\ ') for w in SpamList]
    HamList = [w.replace(' ', '\ ') for w in HamList]

    # prepend location to every e-mail filename
    SpamList = ['./Tests/' + TestFolder + '/' + SpamFolderName + '/{0}'.format(i) for i in SpamList]
    HamList = ['./Tests/' + TestFolder + '/' + HamFolderName + '/{0}'.format(i) for i in HamList]

    SpamOutput = b""
    HamOutput = b""

    IterationCount = len(SpamList) if len(SpamList) > len(HamList) else len(HamList)
    IterationCount /= 1000

    # split to prevent "too many arguments" error
    for i in range(int(IterationCount) + 1):
        SpamOutput += subprocess.check_output('./antispam ' + " ".join(SpamList[i * 1000 : (i+1) * 1000]), shell=True)
        HamOutput += subprocess.check_output('./antispam ' + " ".join(HamList[i * 1000 : (i+1) * 1000]), shell=True)

    SpamOutput = SpamOutput.split(b'\n')
    HamOutput = HamOutput.split(b'\n')

    for line in SpamOutput:
        if b'OK' in line:
            SpamAccepted.append(line[:line.find(b'OK')])
        elif b'FAIL' in line:
            SpamFailed.append(line[:line.find(b'FAIL')])

    for line in HamOutput:
        if b'SPAM' in line:
            HamRejected.append(line[:line.find(b'SPAM')])
        elif b'FAIL' in line:
            HamFailed.append(line[:line.find(b'FAIL')])

# write result summarization to terminal
sys.stdout.write("TOTAL SPAM TESTED:\t\t" + str(SpamCount) + "\n")
sys.stdout.write("\tSPAM MARKED AS SPAM:\t" + "\033[0;32m" + str(SpamCount - (len(SpamAccepted) + len(SpamFailed))) + "\t" + str((SpamCount - (len(SpamAccepted) + len(SpamFailed)))/SpamCount) + " %\033[0;0m" + "\n")
sys.stdout.write("\tSPAM MARKED AS HAM:\t" + "\033[1;31m" + str(len(SpamAccepted)) + "\t" + str(len(SpamAccepted)/SpamCount)  + " %\033[0;0m" + "\n")
sys.stdout.write("\tSPAM FAILED:\t\t" + "\033[1;31m" + str(len(SpamFailed)) + "\t" + str(len(SpamFailed)/SpamCount)  + " %\033[0;0m" + "\n\n")

sys.stdout.write("TOTAL HAM TESTED:\t\t" + str(HamCount) + "\n")
sys.stdout.write("\tHAM MARKED AS HAM:\t" + "\033[0;32m" + str(HamCount - (len(HamRejected) + len(HamFailed))) + "\t" + str((HamCount - (len(HamRejected) + len(HamFailed)))/HamCount)  + " %\033[0;0m" + "\n")
sys.stdout.write("\tHAM MARKED AS SPAM:\t" + "\033[1;31m" + str(len(HamRejected)) + "\t" + str(len(HamRejected)/HamCount)   + " %\033[0;0m" + "\n")
sys.stdout.write("\tHAM FAILED:\t\t" + "\033[1;31m" + str(len(HamFailed)) + "\t" + str(len(HamFailed)/HamCount)   + " %\033[0;0m" + "\n")

# write result details to files SpamResults.txt and HamResults.txt
SpamResults = open("SpamResults.txt", "w")
SpamResults.write("Accepted:\n" + str(SpamAccepted))
SpamResults.write("\n\nFailed:" + str(SpamFailed))
SpamResults.close()

HamResults = open("HamResults.txt", "w")
HamResults.write("Rejected:\n" + str(HamRejected))
HamResults.write("\n\nFailed:" + str(HamFailed))
HamResults.close()
