from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email = email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists')

    username = StringField(label = 'Username', validators=[Length(min=2, max=40), DataRequired()])
    email = StringField(label = 'Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Senha', validators=[Length(min=4), DataRequired()])
    password2 = PasswordField(label = 'Confirme a Senha', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Criar Conta')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = StringField(label='Senha', validators=[DataRequired()])
    submit = SubmitField(label='Entrar')

class ComprarItem(FlaskForm):
    submit = SubmitField(label='Comprar')

class VenderItem(FlaskForm):
    submit = SubmitField(label='Vender')