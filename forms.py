from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class FlowerForm(FlaskForm):
    sepal_length = FloatField(label="Įveskite taurėlapio ilgį:", validators=[DataRequired()])
    sepal_width = FloatField(label="Įveskite taurėlapio plotį", validators=[DataRequired()])
    petal_length = FloatField(label="Įveskite žiedlapio ilgį", validators=[DataRequired()])
    petal_width = FloatField(label="Įveskite žiedlapio plotį", validators=[DataRequired()])

    submit = SubmitField(label='Rodyti gėlę!!!')
