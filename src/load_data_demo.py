import matplotlib.pyplot as plt
from torchvision import datasets, transforms


# Step 1: Convert images into tensors
transform = transforms.ToTensor()


# Step 2: Download/load MNIST training data
train_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform
)


# Step 3: Download/load MNIST testing data
test_data = datasets.MNIST(
    root="data",
    train=False,
    download=True,
    transform=transform
)


# Step 4: Print basic dataset info
print("Training samples:", len(train_data))
print("Testing samples:", len(test_data))


# Step 5: Get one image and label
image, label = train_data[0]

print("Image tensor shape:", image.shape)
print("Label:", label)


# Step 6: Display the image
plt.imshow(image.squeeze(), cmap="gray")
plt.title(f"Label: {label}")
plt.axis("off")
plt.show()