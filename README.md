# Handwritten Digit Recognition

A beginner-friendly machine learning project that trains a neural network to recognize handwritten digits using the MNIST dataset.

This project is being built step-by-step to understand the complete machine learning workflow: data loading, preprocessing, batching, model building, training, evaluation, and prediction.

---

## Project Objective

The goal of this project is to build a handwritten digit recognition system that can classify digits from `0` to `9`.

The project starts with the MNIST dataset and gradually builds toward a complete neural network pipeline.

---

## Current Status

Completed:

- Project setup
- Git and GitHub setup
- Python virtual environment setup
- MNIST dataset loading
- Image-to-tensor conversion
- Single image visualization
- DataLoader creation
- Batch inspection
- 4x4 batch image visualization

Next:

- Build the first neural network model
- Understand flattening, linear layers, weights, biases, and activation functions
- Pass a batch through the model
- Train the model on MNIST

---

## Tech Stack

- Python
- PyTorch
- Torchvision
- Matplotlib
- NumPy
- tqdm
- Git
- GitHub
- Linux

---

## Project Structure

```text
handwritten-digit-recognition/
│
├── data/                  # MNIST dataset files, ignored by Git
├── logs/                  # Learning logs
│   └── day_01.md
│
├── models/                # Saved trained models
├── notebooks/             # Future experiments and notebooks
├── src/                   # Source code
│   ├── load_data_demo.py
│   └── dataloader_demo.py
│
├── .gitignore
├── README.md
└── requirements.txt
