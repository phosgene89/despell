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

#### Requirements
Python 3, numpy

#### Installation
    pip install despell

### References
[1] FJ Damerau, 1964, <i>A technique for computer detection and correction of spelling errors</i>, https://scinapse.io/papers/2066792529

[2] JJ Pollock, A Zamora, 1984, <i>Automatic spelling correction in scientific and scholarly text</i>, https://dl.acm.org/citation.cfm?id=358048
