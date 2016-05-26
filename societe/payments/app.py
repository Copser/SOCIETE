import os
from flask import Flask, render_template, request

import stripe


# Fetch test_secret_key and test_publishable_key from envirnment import
# for are payments application

stripe_keys = {
    'secret_key': os.environ['STRIPE_TEST_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_TEST_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.run(debug=True)
