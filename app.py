from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friend_list = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Add a Book to My Library", friends=friend_list
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        Classification = form["Classification"]
        details = form["details"]
        procure = form["procure"]

        print(title)
        print(author)
        print(pages)
        print(Classification)
        print(details)
        print(procure)

       

        friend_dict = {
            "title": Title,
            "author": Author,
            "pages": Pages,
            "Classification": classification,
            "details": Details,
            "procure": Procurement,

         
        }
        print(friend_dict)
        friend_list.append(friend_dict)
        print(friend_list)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template(
        "about.html", pageTitle="About Page", friends=friend_list
    )

if __name__ == "__main__":
    app.run(debug=True)
