"""
Splitting of raw pg22.txt into formatted individual files

the original of the txt is at: http://www.gutenberg.org/cache/epub/22/pg22.txt

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

for line in open('http://www.gutenberg.org/cache/epub/22/pg22.txt'):
    pass

print('ok')