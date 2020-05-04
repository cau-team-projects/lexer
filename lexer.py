import sys
from lexer.table import table
from lexer.tokens import tokens

def lex(infile):
    state = 0
    for line in infile:
        for char in line:
            while True:
                print('char', char)
                print('cur state', state)
                # if able to proceed
                if char in table[state]: 
                    state = table[state][char]
                    print('next state', state)
                # if state is final state and unable to proceed
                elif state in tokens:
                    print('token', tokens[state])
                    state = 0
                    continue
                # if state is not final state and unable to proceed
                else: 
                    print('failed to lex')
                    return False
                break

    if state in tokens:
        print('token', tokens[state])
        return True
    else:
        print('failed to lex')
        return False

with open(sys.argv[1], 'r') as infile:
    lex(infile)
