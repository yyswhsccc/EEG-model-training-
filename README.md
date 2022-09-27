# EEG-model-training
## using Convolutional neural network 
### What is Convolutional neural network?
CNN is a representative algorithm of deep learning, which is a class of feedforward neural networks that includes convolutional computation and has a deep structure.
A typical CNN is composed of 3 parts：
  * **Convolutional layers**  
  Responsible for extracting local features in the image
  
  ![](https://easyai.tech/wp-content/uploads/2022/08/f144f-2019-06-19-juanji.gif). 
  
  This process could be understood as using a filter (the ll) to filter individual small regions of the image, and get the feature values of these           small regions.
  
 * **Pooling layers**  
 Greatly reduce the dimension of images to avoid over-fitting and reduce time complexity
 
 ![](https://easyai.tech/wp-content/uploads/2022/08/3fd53-2019-06-19-chihua.gif). 
 
 In the above image, we can see that the original image is 20×20, and we decimate it with a sampling window of 10×10, eventually downsampling it into a feature map of 2×2 size.
 
 * **Fully connected layers**
 The data processed by the convolutional and pooling layers are fed to the fully connected layer to get the final desired result
 
 ![](https://easyai.tech/wp-content/uploads/2022/08/a8f0b-2019-06-19-lenet.png.webp)
 
### Why use Convolutional neural network?
CNN is the best at image processing, it can:
  1. effectively downscale data volume
  2. effectively retain image features, in line with the principle of image processing (similar to human vision perception)
  
  ![](https://editor.analyticsvidhya.com/uploads/25366Convolutional_Neural_Network_to_identify_the_image_of_a_bird.png)

## code
* [Try to build a CNN based model](https://github.com/yyswhsccc/EEG-model-training-/blob/main/code/samplemodel.py)
