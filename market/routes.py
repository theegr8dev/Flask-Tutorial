from flask import render_template
from market import app
from market.forms import RegisterForm
from market.models import Item


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
