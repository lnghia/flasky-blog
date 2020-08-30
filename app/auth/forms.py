from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import Email, Required, Length, EqualTo, ValidationError
from ..models import User


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(0, 64)])
    username = StringField('Username', validators=[
        Required(), Length(0, 64)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(
        0, 64), EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField('Confirm password', validators=[
                                     Required(), Length(0, 64)])
    register = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in used.')
