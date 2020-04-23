import nltk
import re

f = open('InputProgForPythonCode.c', 'r')
program = f.read()
count = 0

Identifiers_Output = []
Keywords_Output = []
Symbols_Output = []
Operators_Output = []
Numerals_Output = []
Headers_Output = []

def remove_Spaces(program):
    scanned_Program = []
    for line in prog:
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program


def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed



RE_Keywords = "auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|include"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"


program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')


scanned_Prog = remove_Spaces(prog)

scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])



scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0


Source_Code=[]
for line in scanned_Program_lines:
        Source_Code.append(line)


display_counter = 0
for line in Source_Code:
    count = count + 1
    if(line.startswith("#include")):
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if(re.findall(RE_Keywords, token)):
            Keywords_Output.append(token)
        elif(re.findall(RE_Headers,token)):
            Headers_Output.append(token)
        elif(re.findall(RE_Operators, token)):
            Operators_Output.append(token)
        elif(re.findall(RE_Numerals,token)):
            Numerals_Output.append(token)
        elif (re.findall(RE_Special_Characters, token)):
            Symbols_Output.append(token)
        elif (re.findall(RE_Identifiers, token)):
            Identifiers_Output.append(token)


print("There Are ",len(Keywords_Output),"Keywords: ",Keywords_Output)
print("\n")
print("There Are ",len(Identifiers_Output),"Identifiers: ",Identifiers_Output)
print("\n")
print("There Are ",len(Headers_Output),"Header Files: ",Headers_Output)
print("\n")
print("There Are",len(Symbols_Output),"Symbols:",Symbols_Output)
print("\n")
print("There Are ",len(Numerals_Output),"Numerals:",Numerals_Output)
print("\n")