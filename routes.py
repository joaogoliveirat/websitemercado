from market import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, ComprarItem
from flask_login import login_user, logout_user, login_required

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"
    

@app.route('/lojadewaifus/')
@login_required
def lojadewaifus_page():
    comprar_item = ComprarItem()
    items = Item.query.all()
    return render_template('lojadewaifus.html', items = items, comprar_item = comprar_item)


@app.route('/register/', methods = ['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data, email = form.email.data, password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account Created. Welcome, {user_to_create.username}.", category='success')
        return redirect(url_for('lojadewaifus_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit:
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
            login_user(attempted_user)
            flash('Login Successful.', category='success')
            return redirect(url_for('lojadewaifus_page'))
        else:
            flash('Não existe uma conta com essa combinação de Username e Senha, tente novamente.', category='danger')


    return render_template('login.html', form = form)


@app.route('/logout/')
def logout_page():
    logout_user()
    flash('Logout Successful.', category='info')
    return redirect(url_for('home'))

@app.route('/manual/')
def manual_page():
    return render_template('manual.html')

@app.route('/galeria/')
@login_required
def galeria_page():
    return render_template('galeria.html')
