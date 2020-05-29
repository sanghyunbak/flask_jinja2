from flask import Flask
from jinja2 import Template, select_autoescape, Environment, PackageLoader

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/jinja2')
def jinja2():

    print('app name : {}'.format(app.name))

    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml', 'json'])
    )
    template = env.get_template('test.json')
    print(template.render(test='123'))

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
