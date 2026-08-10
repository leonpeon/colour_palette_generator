from flask import Flask, render_template, request
from colours import Colours
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        image = request.files.get("image")

        if image is None or image.filename == "":
            return render_template("index.html")

        image_path = "static/check_image/image.jpg"
        image.save(image_path)

        colours = Colours(image_path)
        colour_list = colours.top_colours()

        return render_template("colours.html", colour_list=colour_list)

    return render_template("index.html")

@app.route("/image", methods=["GET", "POST"])
def show_image():
    return render_template("colours.html")

if __name__ == "__main__":
    app.run(debug=True)