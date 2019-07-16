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
    
    our minds are compute4s madee of meat. - marvin misnky
    our minds are computers made of meat. - marvin minsky
    our minds are computers made of meeat. - marvin minsky
    our minnds are computers made of meat. - marvin minsky
    our minsd are computers made of meat. - marvij minsky
    our minds are computrrs madde of meat. - marvin minsky
    our minds are computers made of emat. - marvin minsky
    ourm inds are komputers made of meat. - marvin minsky
    our minds qre cmooputers made of meeat. - marvin minsky
    our minds are vomputers made of meat.  -marvin minsky

#### Requirements
Python 3, numpy

#### Installation
    pip install despell

### References
[1] FJ Damerau, 1964, <i>A technique for computer detection and correction of spelling errors</i>, https://scinapse.io/papers/2066792529

[2] JJ Pollock, A Zamora, 1984, <i>Automatic spelling correction in scientific and scholarly text</i>, https://dl.acm.org/citation.cfm?id=358048
