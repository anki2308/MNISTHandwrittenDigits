# MNISTHandwrittenDigits

- Handwritten digit recognition is the process to provide the ability to machines to recognize human handwritten digits. It is not an easy task for the machine 
because handwritten digits are not perfect, vary from person-to-person, and can be made with many different flavors.
- The MNIST dataset for the implementation of a handwritten digit recognition app. To implement this we will use a special type of deep neural network called 
Convolutional Neural Networks. 

<img width="401" alt="demo hand" src="https://user-images.githubusercontent.com/101788326/186685358-537b01ba-9e06-4d90-96c8-22525227efad.png">


# The MNIST dataset

- Among thousands of datasets available in the market, MNIST is the most popular dataset for enthusiasts of machine learning and deep learning. Above 60,000 plus training images of handwritten digits from zero to nine and more than 10,000 images for testing are present in the MNIST dataset. So, 10 different classes are in the MNIST dataset. The images of handwritten digits are shown as a matrix of 28×28 where every cell consists of a grayscale pixel value.

![image](https://user-images.githubusercontent.com/101788326/186684077-e7a00d34-d5ea-48f4-896f-7f38aa464299.png)

- Preprocess the data
The image data cannot be fed directly into the model so we need to perform some operations and process the data to make it ready for our neural network. The dimension of the training data is (60000,28,28). The CNN model will require one more dimension so we reshape the matrix to shape (60000,28,28,1).
# Model Building and Evaluation:
- Used CNN for building different models. A CNN model generally consists of convolutional and pooling layers. It works better for data that are represented as grid structures, this is the reason why CNN works well for image classification problems. The dropout layer is used to deactivate some of the neurons and while training, it reduces offer fitting of the model. We compiled the model with the Adamoptimizer.
- The model.fit() function of Keras will start the training of the model. It takes the training data, validation data, epochs, and batch size.

![hwal](https://user-images.githubusercontent.com/101788326/186682622-5554abed-289f-4ebc-8e5d-da88412dedfb.jpg)
