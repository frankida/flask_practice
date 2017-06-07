from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm

app = Flask(__name__)

app.secret_key='development-key'

app.app_context().push()

@app.route('/')
def index():

    user = 'guest'
    if 'email' in session:
        user=session['email'].split("@")[0]
        return render_template('index.html', user=user)
    else:
        return render_template('index.html', user=user)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form=SignupForm()

    if request.method =="POST":
        if form.validate() ==False:
            return  render_template("signup.html", form=form)
        else:
            session['email']= form.email.data
            ## inside our session i want to create an email cookie

            return  redirect(url_for('index'))
    elif request.method =="GET":
        return render_template("signup.html", form=form)

if __name__=='__main__':
    app.run(debug=True)

