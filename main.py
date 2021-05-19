from flask import Flask, send_file
from textimg import gen

app = Flask('Discord Text Image')
gen(" ")

@app.errorhandler(404)
def page_not_found(error):
  gen("!")
  return send_file('pil_text.png', download_name='Fatal error!!!.jpg')


@app.route('/g/<text>', strict_slashes=False)
def gen_page(text):
  if len(text) > 1:
    gen("!")
    return send_file('pil_text.png', download_name='Fatal error!!!.jpg')
  elif len(text) < 1:
    gen(" ")
    return send_file('pil_text.png', download_name='empty.png')
  gen(text)
  return send_file('pil_text.png', download_name='Created with pil-discord-txt.png')

app.run(host='0.0.0.0', port=8080)