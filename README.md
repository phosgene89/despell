## Despell
### Spelling Distortion in Python

#### Overview

Despell is a Python package that introduces spelling errors into text strings. The implementation is quite basic, consisting of the following spelling errors:

  * Spatial: typing a key that occurs closeby to the intended key
  * Phonetic: typing characters that sound like another character
  * Deletion: missing a character
  * Duplication: accidentally typing a character twice.
  * Transposition: mixing up the order of two adjacent characters

While this is not comprehensive, the results of Damerau [1] and Pollock & Zamora [2] indicate that these errors make up 80%+ of all spelling errors.

#### Examples

Input:

    from despell.despell import corrupt_text
    text = "Our minds are computers made of meat. - Marvin Minsky"
    
    for i in range(10):
        corrupt_text(text)
    
Output:
    
    Our mminds are compiters madeo f meat. - Marvin Minsky
    Our minds are computers made of meta. - Mqrvin Minskt
    Our minds are computerss mdae of meat.  - Marvin Minscy
    Oru minds are computers made of meat. - Marvin Minsky
    Our minds arw kompuetra made of meat. - Marvin Minsky
    Our minds are co,putere  ade of meta. - Marvin Minsky
    Our minds are computers maade of emat. - Marvin Minsky
    Our minds are computers made of maet. - Ma4vin Minsk
    Our minds are computers made of mea. - Marvin Minky
    Our mynds are computesr made of meat. - Marvin Minsky

#### Requirements
Python 3, numpy

#### Installation
    pip install despell

### References
[1] FJ Damerau, 1964, <i>A technique for computer detection and correction of spelling errors</i>, https://scinapse.io/papers/2066792529

[2] JJ Pollock, A Zamora, 1984, <i>Automatic spelling correction in scientific and scholarly text</i>, https://dl.acm.org/citation.cfm?id=358048
