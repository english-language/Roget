"""
Splitting of raw pg22.txt into formatted individual files

the original of the txt is at: http://www.gutenberg.org/cache/epub/22/pg22.txt

Regular expressions reference pages: https://docs.python.org/3/library/re.html?highlight=regular%20expressions
and HOWTO: https://docs.python.org/3/howto/regex.html#regex-howto
"""

"""
The individual articles have the following format:
#d...dl - #, then one or up to four digits, then an optional letter,
then multiple lines of text, then a blank line.

The hierarchy has 6 classes, numbered with Roman numerals and centered on a page with a blank line before and after:

                              CLASS I
               WORDS EXPRESSING ABSTRACT RELATIONS

It has sections in every class numbered by Roman numerals with % separators before and after;

%
SECTION II. RELATION
...
%

Individual parts of a section are numbered with arabic numerals as follows:

%
2. BEING, IN THE CONCRETE
%

The first part of a section is included in the same %% pair of separators;

There are unnumbered 'parts of parts' that are in %% separators too but don't have a number and all belong to the same part.

The pages are marked as:

<--  p.  9  -->

These marks should probably be removed first.
"""
import re

# the % symbol in the beginning of the line

be = re.compile('%\n')  # beginning or end of a multi-line
                        # title of class, section, part
hd = re.compile('(CLASS|SECTION|THESAURUS)')

tb = re.compile('     ') # starting tab of 5 spaces

me = re.compile('\[.+\]') # everything in brackets

it = re.compile('#\d+\.') # items with a '#', digits and '.'
                          # in front
charref_1 = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

charref_2 = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")

cl = re.compile(r'\bCLASS\b')   # class title

se = re.compile(r'\bSECTION\b') # section title

pt = re.compile('') # part

line: str = ''

lines: list = []

beg = True             # this is the end of the multi-line

with open('pg22.txt', 'tr') as roget:
    while True:
        line = roget.readline()
        if not line: break
        if re.match(be, line):   # the % delimiter
            if re.search()
            pass # do the (compound) header reading
        elif re.search(it, line):
            print(line) # the first line of an item
        else:
            pass # not header not item, who knows what it is.

"""

# the main cycle:
with open('pg22.txt', 'r') as roget:
    while True:
        line = roget.readline()
        if not line: break              # end of the main loop.
        if re.match(be, line) and beg:  # title of a class, section...
            while True:
                line = roget.readline()
                if not line: break
                if not re.match(be, line) and beg:
                    lines.append(line)
                else:
                    print(lines)
                    lines = []
                break                # processing of a title ends here

            beg = False
        elif not beg: beg = True
        if re.search(it, line):
            print(line)
"""
# the symbol at the  beginning of the line is detected best
# by re.match(), that's what should be used for % and <--
#
#

"""

import urllib

for line in urllib.request.urlopen('http://www.gutenberg.org/cache/epub/22/pg22.txt'):
    pass
"""

print('ok')
