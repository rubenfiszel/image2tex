import numpy as np
from scipy.misc import imresize
from resizeimage import resizeimage

def regularize_image(bitmap, resized_shape=(28, 28), extra_padding=10):
    shape = bitmap.shape
    max_dim = max(*shape)

    bitmap = bitmap[:,:,0]

    padded = np.pad(
        bitmap,
        ((max_dim - shape[0]) + extra_padding,(max_dim - shape[1]) + extra_padding),
        mode='constant'
    )


    return padded
