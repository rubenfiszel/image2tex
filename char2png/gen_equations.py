
import os
import random

from pytex2png import pytex2png


class Node(object):
    def __init__(self):
        pass

class TerminalNode(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name

    def __str__(self):
        return self.name

class FunctionNode(Node):
    def __init__(self, depth, n):
        Node.__init__(self)
        self.depth = depth
        self.n = n
        self.node_list = []

    def gen_child(self):
        self.node_list = [gen_node(self.depth) for i in xrange(self.n)]
        return self

class Plus(FunctionNode):
    def __init__(self, depth):
        FunctionNode.__init__(self, depth, 2)

    def __str__(self):
        return self.node_list[0].__str__() + " + " + self.node_list[1].__str__()

class Minus(FunctionNode):
    def __init__(self, depth):
        FunctionNode.__init__(self, depth, 2)

    def __str__(self):
        return self.node_list[0].__str__() + " - " + self.node_list[1].__str__()

class Fraction(FunctionNode):
    def __init__(self, depth):
        FunctionNode.__init__(self, depth, 2)

    def __str__(self):
        frac_str = "\\frac{"+self.node_list[0].__str__()+"}{"+self.node_list[1].__str__()+"}"
        return frac_str

class Mult(FunctionNode):
    def __init__(self, depth):
        FunctionNode.__init__(self, depth, 2)

    def __str__(self):
        return self.node_list[0].__str__() + " \\times " + self.node_list[1].__str__()

class Sigma(FunctionNode):
    def __init__(self, depth):
        FunctionNode.__init__(self, depth, 1)

    def __str__(self):
        sigma_str = "\\sum " + self.node_list[0].__str__()
        return sigma_str







term_nodes_txt = []
term_node = []

def fun_node(depth):
    func_list = [Plus(depth)]
    func_list.append(Minus(depth))
    func_list.append(Fraction(depth))
    func_list.append(Mult(depth))
    func_list.append(Sigma(depth))
    return func_list

def pick_fun(depth):
    return random.choice(fun_node(depth))

def pick_term():
    return random.choice(term_node);

def gen_node(depth):
    fl = random.random()
    if not depth > 8 and (fl < 0.6 or depth < 0):
        return pick_term()
    else:
        return pick_fun(depth-1).gen_child()


if __name__ == "__main__":
    char_file = open('characters','r')
    eqmap_file = open('image_to_formula.txt','w')
    chars = char_file.read().replace(" ","").rstrip().split(",")
    for c in chars:
        term_nodes_txt.append(c)

    term_node = [TerminalNode(s) for s in term_nodes_txt]
    print term_nodes_txt

    for i in xrange(200):
        latex_str = str(gen_node(10))
        print 'equation: ', latex_str
        imfile = "eq_images/out_" + str(i) + ".png"
        pytex2png.convert(latex_str, imfile,-1)
        eqmap_file.write(imfile + ' : ' + latex_str)


    char_file.close()
    eqmap_file.close()

#   latex_str = str(gen_node(10))
#   print latex_str
#   pytex2png.convert(latex_str, "eq_images/test.png",-1)

