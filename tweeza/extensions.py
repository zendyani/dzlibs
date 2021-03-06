# -*- coding: utf-8 -*-


from flask.ext.mongoengine import MongoEngine
db = MongoEngine()

from flask_mail import Mail
mail = Mail()

from flask.ext.babel import Babel
babel = Babel(default_locale='en')

from flask.ext.login import LoginManager
login_manager = LoginManager()

from flaskext.bcrypt import Bcrypt
bcrypt = Bcrypt()

from rauth.service import OAuth2Service

github = OAuth2Service(
    name='github',
    base_url='https://api.github.com/',
    authorize_url='https://github.com/login/oauth/authorize',
    access_token_url='https://github.com/login/oauth/access_token',
    client_id='d259d8f16784ca5636d6',
    client_secret='c7715efdf294bc4f486b6e91a658c679106e59ea',
)


# for the Gravatar service
from flaskext.gravatar import Gravatar
gravatar = Gravatar(size=35, rating='g', default='mm',
                    force_default=False,
                    force_lower=False)
