from flask import render_template, flash, redirect, url_for, request, session
from flask_wtf.csrf import generate_csrf

from app import db, LOGGER
from app.models import SurveyResponse, CryptoNetwork
from . import home
from .forms import AnswerSurveyForm, AddCryptoNetworkForm


def save_survey(form):
    store_name = form.store_name.data
    balance = form.balance.data
    price_to_selling = form.price_to_selling.data
    crypto_network = form.crypto_network.data
    wallet_address = form.wallet_address.data
    email_address = form.email_address.data

    survey_response = SurveyResponse(
        store_name=store_name,
        balance=balance,
        price_to_selling=price_to_selling,
        crypto_network=crypto_network,
        wallet_address=wallet_address,
        email_address=email_address,
    )

    db.session.add(survey_response)
    db.session.commit()
    LOGGER.info("Survey data has been saved")


def save_crypto_network(form):
    crypto_name = form.crypto_name.data
    crypto_symbol = form.crypto_symbol.data

    crypto_response = CryptoNetwork(crypto_name=crypto_name.capitalize(), crypto_symbol=crypto_symbol.upper())

    db.session.add(crypto_response)
    db.session.commit()
    LOGGER.info("Crypto network data has been saved")


@home.route("/")
@home.route("/index")
def homepage():
    """
    Render the homepage templates on the '/' or '/index' route
    """

    LOGGER.info("Home page has been called")

    return render_template("home/index.html")


@home.route("/results")
def results():
    """
    Render the results templates on the '/results' route
    """

    LOGGER.info("Results page has been called")
    cryptos = CryptoNetwork.query.all()
    responses = SurveyResponse.query.all()
    return render_template("home/results.html", responses=responses, cryptos=cryptos)


@home.route("/survey", methods=["GET", "POST"])
def solve_a_survey():
    """
    Answer a survey
    """

    LOGGER.info("Answer survey page has been called")

    crypto_networks = CryptoNetwork.query.all()

    form = AnswerSurveyForm()
    form.crypto_network.choices = [(network.id, network.crypto_name) for network in CryptoNetwork.query.all()]
    csrf_token = generate_csrf()

    if request.method == "POST":
        LOGGER.info("POST request to save the answers")
        session["form_data"] = request.form.to_dict()
        save_survey(form)
        return render_template("home/thanks.html")

    return render_template(
        "home/survey.html",
        # questions=questions,
        form=form,
        crypto_networks=crypto_networks,
        csrf_token=csrf_token,
    )


@home.route("/crypto", methods=["GET", "POST"])
def crypto():
    """
    Render the crypto network template on the '/crypto' route
    """

    LOGGER.info("Crypto network page has been called")

    form = AddCryptoNetworkForm()
    csrf_token = generate_csrf()

    if request.method == "POST":
        save_crypto_network(form)
        return render_template("home/index.html")

    return render_template("home/crypto.html", form=form, csrf_token=csrf_token)


@home.before_request
def before_request():
    """
    Save data if refreshing the page
    """

    if request.method == "GET" and request.referrer is not None and "survey" in request.referrer:
        LOGGER.info("Page was refreshed. Get form data to save")
        form_data = session.get("form_data")
        if form_data:
            LOGGER.info("There are data to be saved. Save it")
            form = AnswerSurveyForm(data=form_data)
            save_survey(form)
            session.pop("form_data", None)
