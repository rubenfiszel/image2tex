import os
from pytex2png import pytex2png

def main():
    #eq = '\\frac{Z \\times 4 + \\frac{\\upsilon}{N} \\times 2}{F} + \\pi - n - \\frac{\\frac{\Sigma}{L}}{9 + \\Omega - t}'
    eq = '\\frac{\\frac{\\Delta}{\\sum \\sum Z} + \\frac{7}{\\Psi}}{\\frac{\\Sigma}{k + g}}'
    pytex2png.convert(eq,"output/FULL.png", -1)


if __name__ == "__main__":
    main()
