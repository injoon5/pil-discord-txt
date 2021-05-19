import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def gen(text):
  # font = ImageFont.truetype("Arial-Bold.ttf",14)
  font = ImageFont.truetype("NanumGothic-Bold.ttf",42)
  img=Image.new("RGBA", (50,50),(255,255,255,0))
  draw = ImageDraw.Draw(img)
  # Black: (50,53,59,255)
  # White: (250,250,250,255)
  draw.text((25, 25),text,(250,250,250,255),font=font, anchor="mm", stroke_width=3, stroke_fill=(50,53,59,255))
  draw = ImageDraw.Draw(img)
  img.save("pil_text.png")