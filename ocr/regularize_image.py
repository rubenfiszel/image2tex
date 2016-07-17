import numpy as np
from cv2 import resize, imshow, waitKey, imwrite

def pad_image(bitmap, extra_padding_percentage=10):

    shape = bitmap.shape
    max_dim = max(*shape)

    extra_padding = int(max_dim * extra_padding_percentage / float(100))

    resize_dimension  = ((max_dim - shape[0]) + extra_padding, (max_dim - shape[1]) + extra_padding)
    print resize_dimension

    padded = np.pad(
        bitmap,
        ((resize_dimension[0], resize_dimension[0]), (resize_dimension[1], resize_dimension[1])),
        mode='constant',
        constant_values=255
    )
    return padded


def regularize_image(bitmap):

	show(bitmap)
	padded = pad_image(bitmap)
	print padded.shape
	show(padded)
	resized = resize(padded, (28, 28))
	print resized.shape
	show(resized)
	return resized


i = 0
def show(img):
	global i
	imshow("image", resize(img (img.shape[0] * 20, img.shape[1] * 20)))
	waitKey()
	i += 1
	imwrite(str(i) + ".png", img)
