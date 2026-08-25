from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, bcrypt
from app.models import User, Category, Article

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('home.html')

@main.route('/register')
def register():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/dashboard')
@login_required
def dashboard():
    categories = Category.query.all()
    return render_template('dashboard.html', categories=categories)

@main.route('/category/<int:category_id>')
@login_required
def category(category_id):
    cat = Category.query.get_or_404(category_id)
    articles = Article.query.filter_by(category_id=category_id).all()
    return render_template('category.html', category=cat, articles=articles)

@main.route('/article/<int:article_id>')
@login_required
def article(article_id):
    art = Article.query.get_or_404(article_id)
    return render_template('article.html', article=art)
