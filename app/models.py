from datetime import datetime
from app import db
from app import LOGGER


class SurveyResponse(db.Model):
    """
    Create a Survey Response table
    """

    LOGGER.info("Create a Survey Response table")

    __tablename__ = "survey_responses"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    price_to_selling = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    crypto_network = db.Column(db.Integer, db.ForeignKey("crypto_networks.id"))
    network = db.relationship("CryptoNetwork", backref="survey_responses")
    wallet_address = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return (
            f"<SurveyResponse {self.id}: {self.store_name} {self.balance} "
            f"{self.price_to_selling} {self.crypto_network} {self.wallet_address} "
            f"{self.email_address} {self.created_at}>"
        )


class CryptoNetwork(db.Model):
    """
    Create a Crypto Network table
    """

    LOGGER.info("Create a Crypto Network table")

    __tablename__ = "crypto_networks"

    id = db.Column(db.Integer, primary_key=True)
    crypto_name = db.Column(db.String(50), nullable=False)
    crypto_symbol = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<CryptoNetwork {self.id}: {self.crypto_name} {self.crypto_symbol}>"
