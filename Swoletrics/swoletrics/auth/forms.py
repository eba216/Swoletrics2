from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Your Username', validators=[DataRequired()],
                           render_kw={"type": "text", "placeholder": "username"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"type": "password", "placeholder": "password"})
    remember_me = BooleanField('Keep me logged in', render_kw={"class": "pure-checkbox"})
    submit = SubmitField("Log In", render_kw={"class": "pure-button"})


class SignupForm(FlaskForm):
    username = StringField('Username',
                    validators=[
                        DataRequired(), Length(3, 80),
                        Regexp('^[A-Za-z0-9_]{3,}$',
                            message='Usernames consist of numbers, letters,'
                                    'and underscores.')],
                           render_kw={"type": "text", "placeholder": "username"})
    password = PasswordField('Password',
                    validators=[
                        DataRequired(),
                        EqualTo('password2', message='Passwords must match.')
                    ], render_kw={"type": "password", "placeholder": "password"})
    password2 = PasswordField('Confirm Password', validators=[DataRequired()],
                              render_kw={"type": "password", "placeholder": "password"})
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 120), Email()],
                        render_kw={"type": "text", "placeholder": "email@example.com"})

    submit = SubmitField("Sign Up", render_kw={"class": "pure-button"})

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken.')
