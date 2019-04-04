from flask import Flask, url_for, render_template
import erdbebenanalyse

app = Flask(__name__)

"""
@app.route("/amk")
def test():
    return '<a href=' + url_for("hello", name="Hans") + '>Lass dich grueßen</a>' # link generiert, der beim klicken auf app.route/hello fuehrt

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name + "!"
"""

@app.route("/disclaimer", methods=["GET", "POST"])
def disclaimer():
    return render_template("disclaimer.html")

@app.route("/index", methods=["GET", "POST"]) # Karte
def index():
    erdbebenanalyse.mapping()

    iframe = url_for('static', filename="Karte.html")
    #iframe= "/Users/hoangvutuyen/Desktop/earthbeben/static/Karte.html"
    return render_template("index.html", iframe=iframe)

@app.route("/index1", methods=["GET", "POST"]) # Was sind Erdbeben
def index1():
    return render_template("index1.html")

@app.route("/index1", methods=["POST"]) 
def reply1():
    return render_template("index1.html")

@app.route("/index2", methods=["GET", "POST"]) # Die staerksten Erdbeben
def index2():
    return render_template("index2.html")

@app.route("/index2", methods=["POST"])
def reply2():
    return render_template("index2.html")

@app.route("/index3", methods=["GET", "POST"])
def index3():
    return render_template("index3.html")

@app.route("/index3", methods=["POST"])
def reply3():
    return render_template("index3.html")

@app.route("/index4", methods=["GET", "POST"])
def index4():
    return render_template("index4.html")

@app.route("/index5", methods=["GET", "POST"])
def index5():
    return render_template("index5.html")

@app.route("/index6", methods=["GET", "POST"])
def index6():
    return render_template("index6.html")

@app.route("/datenschutz", methods=["GET", "POST"])
def datenschutz():
    return render_template("datenschutz.html")

@app.route("/impressum", methods=["GET", "POST"])
def impressum():
    return render_template("impressum.html")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(port = 1337, debug = True, threaded= True) # debug bei deploy auf False setzen