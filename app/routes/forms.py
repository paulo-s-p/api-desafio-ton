from wtforms import Form, SubmitField, TextAreaField, PasswordField, EmailField, FloatField, IntegerField
from wtforms.validators import DataRequired



class RegisterUser(Form):
    firstName = TextAreaField('firstName', name='firstName', validators=[DataRequired()])
    lastName = TextAreaField('lastName', name='lastName', validators=[DataRequired()])
    email = EmailField('email', name='email', validators=[DataRequired()])
    password = PasswordField('password', name='password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class RegisterAccount(Form):
    title = TextAreaField('title', name='title', validators=[DataRequired()])
    value = FloatField('value', name='value', validators=[DataRequired()])
    idUser = IntegerField('id_user', name='id_user', validators=[DataRequired()])
    submit = SubmitField('Enviar')

