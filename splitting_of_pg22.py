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

be = re.compile('%\n')   # beginning or end of a multi-line
                        # title of class, section, part

beg = True             # this is the end of the multi-line

roget = open('roget.txt', 'r')

# the main cycle:
for line in roget:
    if re.match(be, line) and beg:
        next = roget.readline()
        print(next)
        beg = False
    elif not beg: beg = True


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