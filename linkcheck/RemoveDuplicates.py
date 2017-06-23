__author__ = 'Moriarty'

inFile = open('b.csv','r')

outFile = open('c.csv','w')

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()
