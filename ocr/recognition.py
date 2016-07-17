from read_img import read_img
from sys import argv
from regularize_image import regularize_image

def nn_reco(im_list):
    return ["A" for im in im_list]

def parse_with_dep(info_list):
    return 1

def process_image_to_symbol_map(path_to_image):
    (im_list, sp_list) = read_img(path_to_image)
    regularized = [
        regularize_image(im)
        for im in im_list
    ]
   
    recognized = nn_reco(regularized)
    nn_input = zip(recognized, sp_list)
    tree = parse_with_dep(nn_input)
    print nn_input

if __name__ == "__main__":
    if len(argv) == 2:
        process_image_to_symbol_map(argv[1])
    else:
        print "Using default image"
        process_image_to_symbol_map('example_text.png')