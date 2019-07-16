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

    text = "Our minds are computers made of meat. - Marvin Minsky"
    
    for i in range(10):
        corrupt_text(text)
    
Output:
    
    oru minds are computers made of miat. - marvin minsy
    our minds ar ecomuters madee of meat. - marvin minsky
    our minds are copmuters made of meat. - mqrvin minsky
    our minds ar ecomputers made of meat. - mavin minsky
    our miinds are computers made of meat.. - marvin minsky
    our minds aree compute4s made of meta. - marvin minsky
    our mins are computers made of emat. = marvin minsky
    our minds are computers made of meat. - marvin minsky
    ou rminds are computers madeof meat. - marvin minsky
    our minds are computers ad of meat. - marvin minsky

#### Requirements
Python 3, numpy

#### Installation
    pip install despell

### References
[1] FJ Damerau, 1964, <i>A technique for computer detection and correction of spelling errors</i>, https://scinapse.io/papers/2066792529

[2] JJ Pollock, A Zamora, 1984, <i>Automatic spelling correction in scientific and scholarly text</i>, https://dl.acm.org/citation.cfm?id=358048
