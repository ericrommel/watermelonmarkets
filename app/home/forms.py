from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email

from app import LOGGER


class AnswerSurveyForm(FlaskForm):
    """
    Form to ask questions
    """

    LOGGER.info("Generate the question form for the survey")

    store_name = StringField("What is the name of your store?", validators=[DataRequired(), Length(max=100)])
    balance = DecimalField("What is the balance left on your gift card?", validators=[DataRequired()])
    price_to_selling = DecimalField("What price are you selling at?", validators=[DataRequired()])
    crypto_network = SelectField(
        "Which network would you like to receive funds at?", coerce=int, validators=[DataRequired()]
    )
    wallet_address = StringField(
        "What address do you want to receive funds at?", validators=[DataRequired(), Length(max=100)]
    )
    email_address = StringField("What is your email address?", validators=[Email(), Length(max=100)])


class AddCryptoNetworkForm(FlaskForm):
    """
    Form to add new crypto networks
    """

    LOGGER.info("Generate a crypto network form for adding crypto networks")

    crypto_name = StringField(
        "What is the name of the new crypto network?", validators=[DataRequired(), Length(max=50)]
    )
    crypto_symbol = StringField(
        "What is symbol of the new crypto network?", validators=[DataRequired(), Length(max=10)]
    )
