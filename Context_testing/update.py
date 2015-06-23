count = 2000
file1 = 'ToBeLabeling_4Above_backup.txt'
file2 = 'ToBeLabeling_4Above.txt'
file3 = 'ToBeLabeling_4Above_copy.txt'

bags = {}
tagSet = {1,2,3,4,5}
with open(file1, 'r', encoding = 'utf-8') as fp1:
        with open(file2, 'w', encoding = 'utf-8') as fp2:
                with open(file3, 'r', encoding = 'utf-8') as fp3:
                        for lines in fp1:
                                line = lines[:-1]
                                tag = line.split('@@@@', 1)[0]
                                if (len(line.split('@@@@')) != 5):
                                        print("illegal cases!!!")
                                        print(line)
                                if tag:
                                        tag = int(tag)
                                        if tag not in tagSet:
                                                print("illegal cases!!!")
                                                print(sentence)
                                        sentence = line.split(' ', 1)[1]
                                        if sentence in bags:
                                                tag1 = bags[sentence]
                                                if tag1 != tag:
                                                        print("Error, tag not equal!!!")
                                                        print(sentence)
                                                        print(tag1)
                                                        print(tag)
                                        else:
                                                bags[sentence] = tag
                        for lines in fp3:
                                line = lines[:-1]
                                tag = line.split('@@@@', 1)[0]
                                if (len(line.split('@@@@')) != 5):
                                        print("illegal cases!!!")
                                        print(line)
                                if not tag:
                                        # num = int(tag)
                                        # if num not in tagSet:
                                        #         print("illegal cases!!!")
                                        #         print(line)
                                        print('weird!!!')
                                        print(line)
                                        sentence = line.split(' ', 1)[1]
                                        if sentence in bags:
                                                tag = str(bags[sentence])
                                                fp2.write(tag + line + '\n')
                                        else:
                                                fp2.write(line + '\n')
                                else:
                                        num = int(tag)
                                        if num not in tagSet:
                                                print("illegal cases!!!")
                                                print(line)
                                        fp2.write(line + '\n')