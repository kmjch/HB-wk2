"""
Prints out all the melons in our inventory
"""

from melons import melon_seedlessness, melon_prices


def print_melon(filename):
    for name in melon_seedlessness:
        seedless = melon_seedlessness[name]
        price = melon_prices[name]
        print name.upper()
        print "  seedless:", seedless
        print "  price:", price
        print "  flesh_color:", flesh_color
        print "  weight:", weight
        print "  rind_color:", rind_color

print_melon()