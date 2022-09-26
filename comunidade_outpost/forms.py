from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade_outpost.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Sign in')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("There is already an account with this email. Log in to proceed.")


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Remember me')
    botao_submit_login = SubmitField('Log in')


class FormEditarPerfil(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('New profile picture', validators=[FileAllowed(['jpg', 'png', 'svg', 'gif'])])
    hobbie_1 = BooleanField('Videogames')
    hobbie_2 = BooleanField('Filmes')
    hobbie_3 = BooleanField('Esportes')
    hobbie_4 = BooleanField('Cantar')
    hobbie_5 = BooleanField('Animes')
    hobbie_6 = BooleanField('Calistenia')
    hobbie_7 = BooleanField('Crossfit')
    hobbie_8 = BooleanField('Dança')
    botao_submit_editarperfil = SubmitField('Submit')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("There is already an user with this email.")


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do post', validators=[DataRequired(), Length(5, 40)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Create post')


class FormEditarPost(FlaskForm):
    titulo = StringField('Post`s title', validators=[DataRequired(), Length(5, 40)])
    corpo = TextAreaField('Write your post here', validators=[DataRequired()])
    botao_submit = SubmitField('Edit post')