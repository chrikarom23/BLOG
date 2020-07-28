from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tempdb = {0: {"id": 0, "title": "Null Blog", "content": "Lorem Ipsum"}}


@app.route("/")
def home():
    return render_template("Home.html", posts = tempdb)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = tempdb.get(post_id)
    if not post:
        return render_template("404.html")
    return render_template("view.html", post=post)


@app.route("/post/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(tempdb)
        tempdb[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)