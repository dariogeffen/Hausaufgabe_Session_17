from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        guess = request.cookies.get("last_guess")
        secret = str(random.randint(1, 30))
        response = make_response(render_template("index.html"))
        response.set_cookie("secret_number", secret)
        return response
    elif request.method == "POST":
        guess = str(request.form.get("number"))
        secret = request.cookies.get("secret_number")
        if guess == secret:
            response = make_response(render_template("success.html", number = guess))
            response.set_cookie("last_guess", guess)
            return response
        elif int(guess) > int(secret):
            indication = "smaller"
            response = make_response(render_template("about.html", compare=indication, number = guess))
            response.set_cookie("last_guess", guess)
            response.set_cookie("indication", indication)
            return response
        elif int(guess) < int(secret):
            indication = "bigger"
            response = make_response(render_template("about.html", compare=indication, number = guess))
            response.set_cookie("last_guess", guess)
            response.set_cookie("indication", indication)
            return response

@app.route("/about", methods=["GET","POST"])
def about():
    guess = str(request.form.get("number"))
    secret = request.cookies.get("secret_number")
    if guess == secret:
        response = make_response(render_template("success.html", number = guess))
        response.set_cookie("last_guess", guess)
        return response
    elif int(guess) > int(secret):
        indication = "smaller"
        response = make_response(render_template("about.html", compare=indication, number = guess))
        response.set_cookie("last_guess", guess)
        response.set_cookie("indication", indication)
        return response
    elif int(guess) < int(secret):
        indication = "bigger"
        response = make_response(render_template("about.html", compare=indication, number = guess))
        response.set_cookie("last_guess", guess)
        response.set_cookie("indication", indication)
        return response

@app.route("/success", methods=["GET", "POST"])
def success():
    response = make_response(render_template("about.html", compare=indication, number = guess))
    return render_template("index.html")


if __name__ == '__main__':
    app.run()  # if you use the port parameter, delete it before deploying to Heroku