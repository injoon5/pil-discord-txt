from flask import Flask, send_file, request
from textimg import gen

app = Flask('Discord Text Image')
gen(" ")

fonts = ["nanum", "lotte", "gungseo", "plexsans", "gugi", "krnuri", "krfr-type", "seoulnamsan", "slei", "spoqa"]
colors = ["original", "red", "green", "yellow", "blue", "pink", "grey", "white", "black", "blurple_old", "blurple"]

@app.errorhandler(404)
def page_not_found(error):
  gen("404 Not Found")
  return send_file('pil_text.png', download_name='Fatal error!!!.png')
@app.route('/g/<hh>')
def moved(hh):
  gen("g를 빼고 요청해주세요.")
  return send_file('pil_text.png', download_name="checkaddress.png")
@app.route('/<string:text>')

@app.route('/<string:text>')
@app.route('/', defaults={ "text": "텍스트 확인" })
def gen_page(text):
  #text = request.path.split("/")[2]
  font = "nanum"
  color = "original"
  if "font" in request.args.to_dict():
    font = request.args.to_dict()["font"]
  if "color" in request.args.to_dict():
    color = request.args.to_dict()["color"] 
  
  if (color not in colors or font not in fonts) or (color not in colors and font not in fonts):
    gen("요청이 잘못되었습니다. ")
    return send_file('pil_text.png', download_name='Fatal error!!!.png')
  if len(text) > 10:
    gen("10자 까지만 허용")
    return send_file('pil_text.png', download_name='Fatal error!!!.png')

  gen(text, color, font)
  return send_file('pil_text.png', download_name='Created with pil-discord-txt.png')

app.run(port=os.getenv("PORT", default=5000))
