from PIL import Image, ImageDraw, ImageFont
import os

class ImageEditor:
    def __init__(self, image_path=None):
        # Initialize the ImageEditor
        self.image_path = image_path
        self.image = None
        
    def load_image(self, image_path):
        # Load the image from the given path
        self.image_path = image_path
        self.image = Image.open(image_path)

    def save_image(self):
        # Save the watermarked image with new filename
        output_path = os.path.splitext(self.image_path)[0] + "_watermarked" + os.path.splitext(self.image_path)[1]
        self.image.save(output_path)
        self.image_path = None

    def add_text(self, text):
        # Add centered text to the image
        draw = ImageDraw.Draw(self.image)
        font_size = min(self.image.width // 10, self.image.height // 10)
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font)
        x = (self.image.width - text_width) // 2
        y = (self.image.height - text_height) // 2
        draw.text((x, y), text, font=font, fill="white")
