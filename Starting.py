from lexical import scanner
import os

dir = os.path.dirname(__file__)
# testnum = input("Enter testfile number (1~10) : ")
#fname = os.path.join(dir, 'testfiles/'+'testfile_'+testnum+'.txt')
fname = "lexical_check.txt"
with open(fname, 'r') as txt:
    code = txt.read()

print(code)
scan = scanner(code)
scan.lexical()
token = scan.tokens

for a in token:
    print(a)
