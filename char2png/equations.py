
import os
import random

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

def fun_node(depth):
    func_list = [Plus(depth)]
    func_list.append(Minus(depth))
    func_list.append(Fraction(depth))
    func_list.append(Mult(depth))
    func_list.append(Sigma(depth))
    return func_list

def pick_fun(depth):
    return random.choice(fun_node(depth))

def pick_term(term_node):
    return random.choice(term_node);


def gen_node(depth,term_nodes_txt):
    print 'term_nodes_txt:', term_nodes_txt
    term_node = [TerminalNode(s) for s in term_nodes_txt]
    fl = random.random()
    if not depth > 8 and (fl < 0.6 or depth < 0):
        return pick_term(term_node)
    else:
        return pick_fun(depth-1).gen_child()

