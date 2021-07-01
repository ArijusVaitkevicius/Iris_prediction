from flask import Flask, render_template
from forms import FlowerForm
import os
from flower import Flower

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('secret_key')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def flower_prediction():
    form = FlowerForm()
    if form.validate_on_submit():
        flower = Flower(sepal_length=form.sepal_length.data,
                        sepal_width=form.sepal_width.data,
                        petal_length=form.petal_length.data,
                        petal_width=form.petal_width.data)
        data = flower.prediction()

        return render_template('prediction.html', data=data)

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
