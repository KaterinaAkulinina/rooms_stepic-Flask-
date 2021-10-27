from flask import Flask, flash
from flask import render_template
from flask_bootstrap import Bootstrap

from project.forms import gameForm
from game_rooms import Rooms

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'My name'

rooms = Rooms(row=2, col=0)

@app.route('/')
def index():
    rooms.row = 2
    rooms.col = 0
    return render_template('index.html')


@app.route('/game/', methods=['post', 'get'])
def game():

    form = gameForm()

    if form.validate_on_submit():
        side = form.way.data
        nsteps = form.number_steps.data
        way = rooms.get_way(side=side, nsteps=nsteps)
        return render_template('game.html', form=form, way=way)

    flash('Утро началось внезапно... Ты проснулся в грязном и холодном помещении.'
              ' Что было вчера вечером? Память безвозвратно утрачена. Ок, пора выбираться отсюда.'
              ' На свежий воздух - на балкон!')
    return render_template('game_init.html', form=form)


if __name__ == "__main__":
    app.run(host='127.0.0.3', port=5000, debug=True)
