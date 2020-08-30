from . import auth
from .. import login_manager
from flask_login import login_user, current_user, login_required
from app.auth.forms import RegisterForm
from app import db
from flask import url_for, render_template, flash, request, redirect
from app.email import send_email
from ..models import User


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.blueprint != 'auth':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print(form.validate_on_submit())
    flash(form.errors)
    # if request.method == 'POST' and form.validate():
    if form.validate_on_submit():
        new_user = User(name=form.name.data, username=form.username.data,
                        email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        send_email(form.email.data, 'Account Confirmation Email',
                   'auth/email/confirm', token=new_user.generate_confirmation_token(), user=new_user)
        # print(form.name.data)
        flash('You have registered your account successfully.' + \
              ' An account confirmation email has been sent to your email. Please login and confirm your account.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>', methods=['GET', 'POST'])
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if not current_user.verify_confirmation_token(token):
        return render_template('auth/unconfirmed.html')
    flash('Your account has been confirmed.')
    return redirect(url_for('main.index'))


@auth.route('/resend_confirmation')
@login_required
def resend_confirmation():
    send_email(current_user.email, 'Account Confirmation Email',
               'auth/email/confirm', token=current_user.generate_confirmation_token())
    flash('Your new account confirmation email has been resent.')
    return redirect(url_for('auth.login'))


@auth.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return redirect(url_for('main.index'))
