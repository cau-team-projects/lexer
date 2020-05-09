#!/usr/bin/python3
import sys
import lexer.table
import lexer.tokens

class Lexer:
    def __init__(self, debug=False):
        self.debug = debug
        self.state = 0
        self.tokenval = []
        self.table = lexer.table.table
        self.tokens = lexer.tokens.tokens
    def prtoken(self):
        print('<%s, %s>' % (self.tokens[self.state], ''.join(self.tokenval[:-1])))
    def lex(self, infile):
        linenum = 0
        for line in infile:
            linenum += 1
            if self.debug:
                print('line', linenum)
            for char in line:
                self.tokenval.append(char)
                while True:
                    if self.debug:
                        print('-' * 10)
                        print('cur state', self.state)
                        print('new char', char)
                    # if able to proceed
                    if char in self.table[self.state]: 
                        self.state = self.table[self.state][char]
                        if self.debug:
                            print('next state', self.state)
                    # if state is final state and unable to proceed
                    elif self.state in self.tokens:
                        self.prtoken()
                        self.state = 0
                        self.tokenval = self.tokenval[-1:]
                        continue
                    # if state is not final state and unable to proceed
                    else: 
                        print('failed to lex at char [%s] at line %d[%s]' % (char, linenum, line))
                        return False
                    break
        if self.state in self.tokens:
            self.prtoken()
            return True
        else:
            print('failed to lex')
            return False

with open(sys.argv[1], 'r') as infile:
    sys.stdout = open(sys.argv[1] + '.out', 'w')
    lexer = Lexer()
    lexer.lex(infile)
