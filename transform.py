import numpy as np
import matplotlib.pyplot as plot

im = plot.imread('animal.jpeg')

# Convert to grayscale using the correct formula
grey_image = np.dot(im[...,:3], [0.2989, 0.5870, 0.1140])

def scaling(im, x_factor, y_factor):

    image_height, image_width = im.shape[:2]
    
    after_height = int(image_height * y_factor)
    after_width = int(image_width * x_factor)
    
    #creating a new array for the scalling image of the same magnitude
    after_image = np.zeros((after_height, after_width), dtype=im.dtype)
    
    for i in range(image_height):
        for j in range(image_width):

            new_x = int(j * x_factor)
            new_y = int(i * y_factor)
            
          # within the magnitude check
            if new_x < after_width and new_y < after_height:
                after_image[new_y, new_x] = im[i, j]
    
    return after_image


# Scaling factors
x_factor = 1.0
y_factor = 1.5


product = scaling(grey_image, x_factor, y_factor)


fig, axes = plot.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(grey_image, cmap='gray')
axes[0].set_title('Original Grayscale Image')
axes[0].axis('off')

axes[1].imshow(product, cmap='gray')
axes[1].set_title('Scaled Image')
axes[1].axis('off')

plot.show()
