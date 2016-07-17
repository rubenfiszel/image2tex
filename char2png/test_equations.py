
from pytex2png import pytex2png
from equations import *

if __name__ == "__main__":

    terminal_nodes = []

    F = open('characters','r')
    chars = F.read().replace(" ","").rstrip().split(",")
    for c in chars:
        terminal_nodes.append(c)

    print "Parsed terminal nodes:", terminal_nodes

#       for i in xrange(200):
#           latex_str = str(gen_node(10))
#           print 'equation: ', latex_str
#           imfile = "eq_images/out_" + str(i) + ".png"
#           pytex2png.convert(latex_str, imfile,-1)
#

    latex_str = str(gen_node(10,terminal_nodes))
    print 'equation: ', latex_str

