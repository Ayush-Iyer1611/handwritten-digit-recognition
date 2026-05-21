# Day 1 - Project Setup, MNIST Loading, and DataLoader Basics

## What I did today

- Created the `handwritten-digit-recognition` project folder
- Initialized a Git repository
- Connected the local repository to GitHub using SSH
- Created a Python virtual environment
- Installed required libraries:
  - PyTorch
  - Torchvision
  - Matplotlib
  - NumPy
  - tqdm
- Created the basic project structure:
  - `src/`
  - `data/`
  - `models/`
  - `logs/`
  - `notebooks/`
- Loaded the MNIST dataset using Torchvision
- Converted MNIST images into PyTorch tensors
- Displayed one handwritten digit image
- Created a PyTorch DataLoader
- Used a batch size of 64
- Printed image and label batch shapes
- Displayed 16 handwritten digits in a 4x4 grid

## What I learned

- A virtual environment keeps project dependencies isolated
- Git tracks changes in the project
- GitHub stores the project online
- SSH makes pushing to GitHub easier and cleaner
- MNIST is a dataset of handwritten digits from 0 to 9
- Each MNIST image is 28x28 pixels
- One MNIST image has shape `[1, 28, 28]`
- The first dimension represents the grayscale channel
- `transforms.ToTensor()` converts images into PyTorch tensors
- `ToTensor()` also scales pixel values from `0-255` to `0-1`
- `train=True` loads the training dataset
- `train=False` loads the testing dataset
- A dataset returns samples in the form `(image, label)`
- A DataLoader gives data to the model in batches
- A batch is a group of samples processed together
- A batch of 64 MNIST images has shape `[64, 1, 28, 28]`
- Labels have shape `[64]` because each image has one label
- `shuffle=True` randomizes the order of training data
- `squeeze()` removes the extra channel dimension for visualization
- `.item()` converts a single tensor value into a normal Python number
- One epoch means one full pass through the training dataset

## Questions I had today

- What exactly is a tensor?
- Why do neural networks need tensors?
- What is the difference between training and testing data?
- What is a batch?
- How does a neural network use a batch?
- What are weights and biases?
- What is a loss function?
- How does the model learn from wrong predictions?

## Current project pipeline

```text
MNIST dataset
↓
Transform image to tensor
↓
Load individual samples
↓
Create DataLoader
↓
Generate batches
↓
Visualize batch images
