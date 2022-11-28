tokens = {"keywords": ["ako", "dok", "vrati", "funkcija", "ispis", "kraj"],
          "separators": ["\n", " ", "\t"],
          "operators": ["+", "-", "=", "*", "/", "<", ">", "!", "==", "<=", ">="],
          "literals": ["istina", "laz","%"],
          "comments": ["$$"]
          }

numberOf = {"identificators": [],
            "keywords": [],
          "separators": [],
          "operators": [],
          "literals": [],
          "comments": []
          }


def countToken(element, category):
    items = numberOf[category]
    
    for item in items:
        if item[0] == element:
            item[1] +=1
            return
        
    items.append([element, 1])
    
def isIdentificator(element):
    return len(element) <= 6 and element[0].isalpha()  

def getTokenCategory(element):
    for key, value in tokens.items():
        if element in value:
            countToken(element, key)
            return key[:-1]
        
    if isIdentificator(element):
        countToken(element, "identificators")
        return "identificator"
    
    else:
        if element.isnumeric() or element[0] == "%" and element[0] == "%":
            countToken(element, "literals")
            return "literal"
        
    return "Lexical error: Token category not found."

def lexicalAnalysis(line, printer):
    elements = line.split(" ")
    for i in range(len(elements)):
        category = getTokenCategory(elements[i])
        outputFile.write("('{}', {})".format(elements[i], category) + "\n")
        
        if i != len(elements) - 1:
            outputFile.write("('{}', {})".format(" ", getTokenCategory(" ")) + "\n")
            
        
codeFile = open("code.txt", "r")
code = codeFile.read().lower()
outputFile = open("output.txt", "w")
lines = code.split("\n")
printer = ""

for i in range(len(lines)):
    line = lines[i]
    if "$$" in line:
        countToken(line[line.index("$$"):], "comments")
        line = line[:line.index("$$") - 1]
        
    outputFile.write("Line " + str(i + 1) + ": " + line + "\n")
    lexicalAnalysis(line, printer)
    
    if i != len(lines):
        outputFile.write("------------------------------\n\n")
        
outputFile.write(printer + "\n")

for key, value in numberOf.items():
    total = 0
    tokensForPrint = []
    
    for i in range(len(value)):
        if value[i][0] == "%":
            value[i][1] *=2
            
        tokensForPrint.append("'{}'[{}]".format(value[i][0], value[i][1]))
        total += value[i][1]

        
    printLine = "-{} [{}]: ".format(key, total)
    outputFile.write(printLine + ", ".join(tokensForPrint) + "\n")

codeFile.close()
outputFile.close()
