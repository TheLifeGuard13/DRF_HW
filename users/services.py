import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product_name):
    """Создает страйп продукт."""
    return stripe.Product.create(name=product_name)


def create_stripe_price(product, amount):
    """Создает страйп цену."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product_data={"name": product},
    )


def create_stripe_session(price):
    """Создает страйп сессию."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="subscription",
    )
    return session.get("id"), session.get("url")
