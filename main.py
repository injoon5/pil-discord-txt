from typing import Optional
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from textimg import gen
from urllib.parse import unquote


app = FastAPI(title="Discord txt to img",
    description="It makes a image by the text **YOU** want!!",
    version="0.1.5")

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

gen(" ")

fonts = ["nanum", "lotte", "gungseo", "plexsans", "gugi", "krnuri", "krfr-type", "seoulnamsan", "slei", "spoqa"]
colors = ["original", "red", "green", "yellow", "blue", "pink", "grey", "white", "black", "blurple_old", "blurple"]

@app.get('/{text}')
def img_generation_endpoint(text, font: Optional[str] = "nanum", color: Optional[str] = "original"):
  #text = unquote(text.__dict__['scope']['path_params']["text"])
  if (color not in colors or font not in fonts) or (color not in colors and font not in fonts):
    gen("요청이 잘못되었습니다. ")
    return FileResponse('pil_text.png')
  if len(text) > 10:
    gen("10자 까지만 허용")
    return FileResponse('pil_text.png')
  
  gen(text, color, font)
  return FileResponse('pil_text.png')

@app.get('/g/{text}')
def moved(text, reqfont: Optional[str] = "nanum", reqcolor: Optional[str] = "original"):
  return RedirectResponse(url=f'/{text}?font={reqfont}&color={reqcolor}')


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port="8080")
