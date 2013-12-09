#!/usr/bin/env python
import sys

from flask import Flask, render_template
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG

app = Flask(__name__)
app.config.from_object(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

NAVIGATION = (
	{'title': 'Home', 'slug': ''},
	{'title': 'Our Company', 'slug': 'about'},
	{'title': 'Locations', 'slug': 'locations'},
	{'title': 'Resources', 'slug': 'resources'},
)

@app.route('/')
def index():
    return render_template('index.html', nav=NAVIGATION)


@app.route('/<slug>/')
def page(slug):
	template = 'content/%s.html' % slug
	return render_template(template, nav=NAVIGATION)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
       app.run()
	
	
