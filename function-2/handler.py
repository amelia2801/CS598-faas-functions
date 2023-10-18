from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from datasets import load_dataset

def handle(req):
    # req: the image URL (from S3)
    urllib.request.urlretrieve(req, "img.png")
    image = Image.open('img.png')

    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    print(model.config.id2label[predicted_label])
