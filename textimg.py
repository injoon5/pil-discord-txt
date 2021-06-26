import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

fontDict = {"nanum": "font/NanumGothic-Bold.ttf", "lotte": "font/12롯데마트드림Medium.ttf", "gungseo": "font/hy궁서-yoond1004.ttf", "plexsans": "font/IBMPlexSansKR-Regular.ttf", "gugi": "font/Gugi-Regular.ttf", "krnuri": "font/HangeulNuriR.ttf", "krfr-type": "font/KoreanFrenchTypewriter.ttf", "seoulnamsan": "font/SeoulNamsanM.ttf", "slei": "font/SLEIGothicTTF.ttf", "spoqa": "font/SpoqaHanSansNeo-Regular.ttf"}
colorDict = {"original": {"stroke": (50,53,59,255), "color": (250,250,250,255)}, "red": {"stroke": (255, 0, 0,0), "color": (255, 0, 0)}, "green": {"stroke": (60, 179, 113,0), "color": (60, 179, 113)}, "yellow": {"stroke": (255, 165, 0,0), "color": (255, 165, 0)}, "blue": {"stroke": (0, 0, 255,0), "color": (0, 0, 255)}, "pink": {"stroke": (238, 130, 238,0), "color": (238, 130, 238)}, "grey": {"stroke": (120, 120, 120,0), "color": (120, 120, 120)}, "white": {"stroke": (255, 255, 255,0), "color": (255, 255, 255)}, "black": {"stroke": (0, 0, 0,0), "color": (0, 0, 0)}, "blurple_old": {"stroke": (114, 137, 218,0), "color": (114, 137, 218)}, "blurple": {"stroke": (88, 101, 242, 0), "color": (88, 101, 242)}}
def gen(text, color="original", font="nanum"):
  # font = ImageFont.truetype("Arial-Bold.ttf",14)
  font = ImageFont.truetype(fontDict[font],42)
  x = font.getsize(text)[0] + 2
  y = font.getsize(text)[1] + 2
  img=Image.new("RGBA", (x,y),(255,255,255,0))
  draw = ImageDraw.Draw(img)
  # Black: (50,53,59,255)
  # White: (250,250,250,255)
  draw.text((x, y/2), text, colorDict[color]["color"], font=font, anchor="rm", stroke_width=3, stroke_fill=colorDict[color]["stroke"])
  draw = ImageDraw.Draw(img)
  img.save("pil_text.png")