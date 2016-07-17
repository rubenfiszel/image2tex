import unittest
from regularize_image import regularize_image
import numpy as np


class ImageTestCase(unittest.TestCase):
    def test_basic(self):
        image = np.array([
            [[1,1,1], [1,1,1], [1,1,1]],
            [[4,4,4], [4,4,4], [4,4,4]],
            [[7,7,7], [7,7,7], [7,7,7]]
        ])
        resized = regularize_image(image, (5, 5), 1)

        self.assertEqual(resized.shape, (5, 5))



if __name__ == '__main__':
    unittest.main()
