# Lexical Analyzer for Simple Arithmetic Expressions
import string

# Global Declarations
charClass = None
lexeme = []
nextChar = ''
lexLen = 0
token = None
nextToken = None

# Token Codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

# Character Classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Function Declarations
def addChar():
    global lexeme, lexLen, nextChar
    if lexLen <= 98:
        lexeme.append(nextChar)
        lexLen += 1
    else:
        print("Error - lexeme is too long")
        
def getChar(in_fp):
    global nextChar, charClass
    nextChar = in_fp.read(1)
    if nextChar == '':
        charClass = EOF
    elif nextChar in string.ascii_letters:
        charClass = LETTER
    elif nextChar in string.digits:
        charClass = DIGIT
    else:
        charClass = UNKNOWN

def getNonBlank(in_fp):
    while nextChar.isspace():
        getChar(in_fp)

def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken

def lex(in_fp):
    global lexeme, lexLen, charClass, nextToken
    lexeme = []
    lexLen = 0
    getNonBlank(in_fp)

    if charClass == LETTER:
        addChar()
        getChar(in_fp)
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar(in_fp)
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar(in_fp)
        while charClass == DIGIT:
            addChar()
            getChar(in_fp)
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar(in_fp)
    elif charClass == EOF:
        nextToken = EOF
        lexeme = ['E', 'O', 'F']
    
    print(f"Next token is: {nextToken}, Next lexeme is {''.join(lexeme)}")
    return nextToken


# Main function to drive the lexical analyzer
def main():
    try:
        in_fp = open("C:\\Users\\musta\\source\\repos\\PythonApplication6\\front.in", "r")
    except FileNotFoundError:
        print("ERROR - cannot open front.in")
        return
    
    getChar(in_fp)
    while nextToken != EOF:
        lex(in_fp)

if __name__ == "__main__":
    main()
