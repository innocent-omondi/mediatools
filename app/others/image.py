# from PIL import Image

# img = Image.open(r"http://127.0.0.1:8000/media/images/android-chrome-512x512.png")
# img.save(r"news.jpeg")
import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("Output.gif")
shape.image_data.save("Output3.pdf")