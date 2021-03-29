#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    """Check for successful party"""
    success = True
    if (is_weekend and walnuts < 40) or (not is_weekend and walnuts not in range(40, 61)):
        return False
    return success
