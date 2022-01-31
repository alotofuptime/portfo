from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("./database.txt", mode="a", encoding="utf-8") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}\n{subject}\n{message}\n")
        return file


def write_to_csv(data):
    with open("./database.csv", mode="a", encoding="utf-8", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2,
            delimiter=",",
            quotechar="'",
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])
    return "New form submitted to database"


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        except:
            return "Did not save to database"
        return redirect("thankyou.html")
    else:
        return "Something went wrong. Try again!"
