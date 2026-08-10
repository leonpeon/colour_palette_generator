from flask import Flask, render_template, request
from colours import Colours

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        image = request.files["image"]
        image = image.filename
        print(f"FILENAME: {image}")
        colours = Colours(image)
        colour_list = colours.top_colours()

        return render_template("colours.html", colour_list=colour_list)

    return render_template("index.html")

@app.route("/image", methods=["GET", "POST"])
def show_image():
    return render_template("colours.html")

if __name__ == "__main__":
    app.run(debug=True)