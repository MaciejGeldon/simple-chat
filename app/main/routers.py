from flask import session, url_for, request, render_template
from werkzeug.utils import redirect

from app.main.forms import LoginForm
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    name = session.get('name', '')
    if name == '':
        return redirect('.index')
    return render_template('chat.html', name=name)
