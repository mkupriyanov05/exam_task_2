from flask import request, render_template
from setup import app


@app.route('/', methods=['GET', 'POST'])
def calculating():
    height, weight = request.form.get('height'), request.form.get('weight')
    if weight and height is not None:
        height = float(height)
        weight = float(weight)
        if (weight <= 0) or (height <= 0):
            index = 'Wrong weight or height'
        else:
            index = weight / (height ** 2)
    else:
        index = None
    return render_template('index.html', index=index)


if __name__ == '__main__':
    app.run()
