from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", usr="ervette")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        valid = False
        if len(email) < 4:
            flash("Email must be more than 4 characters", category="error")
        elif len(firstName) < 2:
            flash("Name must be more than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords are not the same", category="error")
        elif len(password1) < 7:
            flash("Password must be more than 7 characters", category="error")
        else:
            # add to database
            valid = True
            flash("Account Created", category="success")

    return render_template("sign_up.html")
