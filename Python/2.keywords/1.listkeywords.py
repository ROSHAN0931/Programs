'''keyword module: The keyword is the buil-in module to get the list of keywords. 
Also, this module allows a Python program to determine if a string is a keyword.'''

import keyword
print(keyword.kwlist)

Output

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


'''help() function: Apart from a keyword module, we can use the help() function to get the list of keywords'''

help("keywords")

Output:

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

'''Note:

You cannot use any of the above keywords as identifiers in your programs. If you try to do so, you will get an error. 
An identifier is a name given to an entity, For example, variables name, functions name, or class name.'''
