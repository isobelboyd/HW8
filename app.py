from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friend_list = [
    {"title": "The Hobbit",
     "author": "Tok", 
     "pages": 224,
     "classif": "fiction",
     "details": "read", 
     "procure": "Library",},
]

###### Custom Error Pages ######
# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


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
        classif = form["classif"]
        details = form["details"]
        procure = form["procure"]

        print(title)
        print(author)
        print(pages)
        print(classif)
        print(details)
        print(procure)

       

        friend_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classif": classif,
            "details": details,
            "procure": procure,

         
        }
        print(friend_dict)
        friend_list.append(
            friend_dict
        )
        print(friend_list)

        flash(
            "The book ;" + title + " has been added to the database.",
            "success",
        )
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
