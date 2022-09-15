from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Parker Gagliano',
        'title': 'Bottlecap for sale',
        'content': 'this is a rare collectable bottlecap',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Parker Gagliano',
        'title': 'stamp for sale(rare, real)',
        'content': 'this is a rare collectable stamp',
        'date_posted': 'April 1, 2022'
    }
]


@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="Project")


if __name__ == '__main__':
    app.run(debug=1)
