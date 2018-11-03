from flask import render_template, flash, redirect, url_for, request
from app.main import bp


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                           title=('Home')
                           )
