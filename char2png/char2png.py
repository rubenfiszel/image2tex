import os
from pytex2png import pytex2png

def main():
        fil = open("characters", "r+")
        characters = fil.read().replace(" ", "").split(",")
        for c in characters:
            stri = c.replace("\\", "__")
	    pytex2png.convert(c,"output/"+stri+".png", 28)


if __name__ == "__main__":
    main()
