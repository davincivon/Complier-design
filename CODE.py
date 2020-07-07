# compiler designed for following hypothetical language
'''

int main()
begin
int Arr_name[size];
for i= num to expression do
var = Arr-name[var];
End

'''
import sys

# list of tokens in the language
tokens = ['int', 'main', '(', ')', 'begin', 'end', ';', '[', ']', 'for', '=', 'to', 'do', '+', '-', '*', '/' ]
print(tokens)

# reference parsing table
parse_table = {
    '0': {'int': 'S 2', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': '1', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '1': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'A', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '2': {'int': 'NA', 'main': 'S 3', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '3': {'int': 'NA', 'main': 'NA', '(': 'S 4', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '4': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'S 5', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '5': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'S 6', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '6': {'int': 'S 9', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'R 4', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': '7', 'DEC': '8', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '7': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'S 10', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '8': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'R 2', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'S 12', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': '11', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '9': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 14',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': '13', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '10': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'R 1', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '11': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'R 3', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '12': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 15',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '13': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'S 16', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '14': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'S 17', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '15': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'S 18', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '16': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'R 5', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'R 5', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '17': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           '[': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '19',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '18': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'S 22', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '19': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'S 23', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
     ,

    '20': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'R 7', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 7', '+': 'R 7', '-': 'R 7',
           '*': 'R 7', '/': 'R 7', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}

    ,

      '21':{'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'R 8', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 8', '+': 'R 8', '-': 'R 8',
           '*': 'R 8', '/': 'R 8', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}

      ,

    '22': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'S 24', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,

    '23': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'R 6', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}

    ,
    '24': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           '[': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '27',
           'FORL': 'NA', 'E': '25', 'T': '26', 'STMT': 'NA'}

     ,
    '25': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'S 28', '+': 'S 29', '-': 'S 30',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '26': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 13', '+': 'R 13', '-': 'R 13',
           '*': 'S 31', '/': 'S 32', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '27': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 16', '+': 'R 16',
           '-': 'R 16', '*': 'R 16', '/': 'R 16', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '28': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 34',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA',
           '-': 'NA', '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA',
           'F': 'NA', 'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': '33'}
    ,
    '29': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           'osb': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '27',
           'FORL': 'NA', 'E': 'NA', 'T': '35', 'STMT': 'NA'}
    ,
    '30': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           '[': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '27',
           'FORL': 'NA', 'E': 'NA', 'T': '36', 'STMT': 'NA'}
    ,
    '31': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           '[': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '37',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '32': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 21',
           '[': 'NA', ']': 'NA', 'num': 'S 20', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': '38',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '33': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'S 39', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '34': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'S 40', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '35': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 11', '+': 'R 11', '-': 'R 11',
           '*': 'S 31', '/': 'S 32', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '36': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 12', '+': 'R 12', '-': 'R 12',
           '*': 'S 31', '/': 'S 32', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '37': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', 'eq': 'NA', 'to': 'NA', 'do': 'R 14', '+': 'R 14',
           '-': 'R 14', '*': 'R 14', '/': 'R 14', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA',
           'F': 'NA', 'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '38': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'R 15', '+': 'R 15',
           '-': 'R 15', '*': 'R 15', '/': 'R 15', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA',
           'F': 'NA', 'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '39': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'R 9', ';': 'NA', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA',
           '-': 'NA', '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA',
           'F': 'NA', 'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '40': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'NA', 'id': 'S 14',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA',
           '-': 'NA', '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': '41',
           'F': 'NA', 'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}
    ,
    '41': {'int': 'NA', 'main': 'NA', '(': 'NA', ')': 'NA', 'begin': 'NA', 'end': 'NA', ';': 'R 10', 'id': 'NA',
           '[': 'NA', ']': 'NA', 'num': 'NA', 'for': 'NA', '=': 'NA', 'to': 'NA', 'do': 'NA', '+': 'NA', '-': 'NA',
           '*': 'NA', '/': 'NA', '$': 'NA', 'S': 'NA', 'CODE': 'NA', 'DEC': 'NA', 'ARRAY': 'NA', 'F': 'NA',
           'FORL': 'NA', 'E': 'NA', 'T': 'NA', 'STMT': 'NA'}

 }

# 2 * (number of elements in the grammar)
no_ele = {'1': 14, '2': 2, '3': 4, '4': 0, '5': 6, '6': 8, '7': 2, '8': 2, '9': 18, '10': 6, '11': 6, '12': 6,
          '13': 2, '14': 6, '15': 6, '16': 2}

# grammar head (non-terminal)
gram_name = {'1': 'S', '2': 'CODE', '3': 'CODE', '4': 'CODE', '5': 'DEC', '6': 'ARRAY', '7': 'F',
             '8': 'F', '9': 'FORL', '10': 'STMT', '11': 'E', '12': 'E', '13': 'E', '14': 'T', '15': 'T', '16': 'T'}


pointer_dict = []


# error handler
def get_line_no(pointer, program_string):
    x = 0
    for k in range(0, pointer + 1):
        if program_string[k] == '\n':
            x += 1
    return x


# tokenizer method
def tokenizer(program_string):
    program_string += '$'
    pointer = 0
    lis = []
    while program_string[pointer] != "$":
        current_string = ""
        if program_string[pointer].isalpha():
            current_string += program_string[pointer]
            pointer += 1
            while program_string[pointer].isalnum() or program_string[pointer] == "_":
                current_string += program_string[pointer]
                pointer += 1
            if current_string in tokens:
                lis.append(tokens[tokens.index(current_string)])
                x = get_line_no(pointer, program_string)
                if(x==0):
                    x=x+1
                pointer_dict.append([current_string, x])

            else:
                lis.append('id')
                x = get_line_no(pointer, program_string)
                if (x == 0):
                    x = x + 1
                pointer_dict.append([current_string, x])
        elif program_string[pointer].isnumeric():
            current_string += program_string[pointer]
            pointer += 1
            dot_count = 0
            while program_string[pointer].isnumeric() or program_string[pointer] == ".":
                if program_string[pointer] == ".":
                    dot_count += 1
                current_string += program_string[pointer]
                pointer += 1
            if dot_count > 1:
                x = get_line_no(pointer, program_string)
                if (x == 0):
                    x = x + 1
                print('Error in Tokenizer Line No. : ' + str(x) + ' unidentified token ' + current_string)
                exit()
            else:
                if program_string[pointer] == ' ' or program_string[pointer] == ']' or program_string[pointer] == '+' or \
                        program_string[pointer] == '-' or program_string[pointer] == '*' or program_string[
                    pointer] == '/':
                    lis.append('num')
                    x = get_line_no(pointer, program_string)
                    if (x == 0):
                        x = x + 1
                    pointer_dict.append([current_string, x])
                else:
                    x = get_line_no(pointer, program_string)
                    if (x == 0):
                        x = x + 1
                    current_string += program_string[pointer]
                    print('Error in Tokenizer Line No. : ' + str(x) + ' unidentified token ' + current_string)
                    exit()

        else:
            if program_string[pointer] != " " and program_string[pointer] != "\n":
                lis.append(tokens[tokens.index(program_string[pointer])])
                x = get_line_no(pointer, program_string)
                if (x == 0):
                    x = x + 1
                pointer_dict.append([current_string, x])
                pointer += 1
            else:
                pointer += 1

    return lis


# syntax analyzer method
def syntax_analyser(token_list):
    top = 0
    stack_token = ['0']
    j = len(token_list)
    i = 0
    while (i < j):
        x = parse_table[stack_token[top]][token_list[i]].split()
        if (x[0] == 'S'):
            print('shift')
            stack_token.append(token_list[i])
            stack_token.append(x[1])
            top += 2
            i += 1
            print(stack_token)
        elif (x[0] == 'R'):
            print('reduce')
            stack_token = stack_token[:(top - no_ele[x[1]]) + 1]
            top -= no_ele[x[1]]
            stack_token.append(gram_name[x[1]])
            top += 1
            stack_token.append(parse_table[stack_token[top - 1]][stack_token[top]])
            top += 1
            print(stack_token)
        elif (x[0] == 'NA'):
            print('\nError Near line no :' + str(pointer_dict[i][1]) + '\nNot a valid syntax near or not a valid keyword:' + pointer_dict[i][0])
            exit()
        elif (x[0] == 'A'):
            print("accepted..!\n")
            exit()
        else:
            break


def main():
    program_string = open("prgm", 'r').read()
    print("\nProgram\n")
    print(program_string)
    token_list = tokenizer(program_string)
    print("\nTokens\n")
    print(token_list)
    token_list.append('$')
    print("analysing syntax for the obtained tokens...")
    syntax_analyser(token_list)

main()