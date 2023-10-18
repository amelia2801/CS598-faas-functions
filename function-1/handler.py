import urllib.request
from PIL import Image

MAX_SIZE = (100,100)

def handle(req):
    # req: the image URL (from S3)
    urllib.request.urlretrieve(req, "img.png")

    img = Image.open('img.png')
    width, height = img.size

    # If image width or height is larger than MAX_SIZE, resize the image
    if width > MAX_SIZE[0] | height > MAX_SIZE[1]:
        img.thumbnail(MAX_SIZE)

    return img