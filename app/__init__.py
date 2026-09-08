import os , urlib.parse , urllib.request , render_template
from app.youtube import youtuube_bp
Gemini_api_key="Gemini API Key";

def home():
  return render_template ("indexx.html") # render_template is an function to call render which integrate in frontend

def create_app():
  app = Flask(_name_)
  app.register_blueprint(youtube_bp, url_prefix="/youtube")

@app.route("/html")

def html():
  return render_template("index.html")

return app;
