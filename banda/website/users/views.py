from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from sqlalchemy.sql.functions import user
from wtforms.validators import Email
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_required, login_user, logout_user, current_user
from .forms import SignupForm, LoginForm, ResetPasswordForm, RequestResetForm
from flask_mail import Message

user = Blueprint('user', __name__)


@user.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                flash("Logged in succesfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
    return render_template("login.html", user=current_user, form=form)
