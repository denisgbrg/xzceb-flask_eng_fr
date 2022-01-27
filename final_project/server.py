from machinetranslation import translate
from flask import Flask, render_template, request
import json

app = Flask("Web Translator",static_folder="static")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')    
    return translate.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')    
    return translate.frenchToEngish(textToTranslate)

@app.route("/")
def renderIndexPage():
    print("Root request")
    return render_template("index.html")

if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=8080)
