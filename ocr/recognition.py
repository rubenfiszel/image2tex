from read_img import read_img

def regulize(im_list):
    return [im for im in im_list]

def nn_reco(im_list):
    return ["A" for im in im_list]

def parse_with_dep(info_list):
    return 1

def main():
    (im_list, sp_list) = read_img('example_text.png')
    regulized = regulize(im_list)
    recognized = nn_reco(regulized)
    nn_input = zip(recognized, sp_list)
    tree = parse_with_dep(nn_input)
    print nn_input

if __name__ == "__main__":
    main()
