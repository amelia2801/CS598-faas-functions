# CS598-faas-functions
CS598 Group Project - Function Definitions for FaaS Function Chaining

Here we define 2 functions that will be chained in a Function as a Service platform.
The functions will be deployed using OpenFaaS.

Each function has its own folder that contains:
- `handler.py`: the function code
- `requirements.txt`: any required dependencies

Each function also has a `yaml` file that describes a Docker container. To build the function, run:

`faas-cli build -f ./<function-name>.yml`

## Function 1
The first function does image processing, which is to resize an input image to a specified size.
The images used here are from [ImageNet-1k](https://huggingface.co/datasets/imagenet-1k/tree/main/data) datasets.
- Input: image URL from external storage (S3)
- Output: image

## Function 2
The second function runs an image classification on the input image based on the [ResNet50](https://huggingface.co/microsoft/resnet-50) model.
- Input: updated image URL from external storage (S3)
- Output: strings representing image classification label.
