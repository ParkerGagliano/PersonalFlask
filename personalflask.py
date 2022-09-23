from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b0840af5a08f99cbd53c13fe64773dfd'


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
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="Project")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'joesmith@gmail.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=1)
