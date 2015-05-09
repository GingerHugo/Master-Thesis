PolarSet = {'positive', 'negative'}

def Readin(fp, Lexicon):
        for line in fp:
                Lexicon.add(line[:-1].split()[0])

def Filter(fp, Lexicon, Candidate):
        for element in Candidate:
                if element not in Lexicon:
                        fp.write(element + '\n')

def Refining(fp, Lexicon):
        for element in Lexicon:
                fp.write(element + '\n')

for polar in PolarSet:
        GFile = 'voc_final_' + polar + '_groundtruth.txt'
        DFile = 'voc_final_' + polar + '_deleted.txt'
        Lexicon = set()
        Candidate = set()
        with open(GFile, 'r', encoding = 'utf-8') as fp:
                Readin(fp, Lexicon)
        with open(DFile, 'r', encoding = 'utf-8') as fp:
                Readin(fp, Candidate)
        with open(GFile, 'w', encoding = 'utf-8') as fp:
                Refining(fp, Lexicon)
        with open(DFile, 'w', encoding = 'utf-8') as fp:
                Filter(fp, Lexicon, Candidate)