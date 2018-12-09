from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from builtins import chr  # pylint: disable=redefined-builtin


def subscriptify(x):
    """Create a a subscript unicode representation of an integer single-digit
    number.

    Subscript digits range from U+2080 to U+2089 in Unicode.
    """
    return chr(ord(u'\u2080') + x)
