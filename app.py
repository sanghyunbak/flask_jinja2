import json

from flask import Flask, request
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

@app.route('/run', methods=['GET', 'POST'])
def run():
    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml', 'json'])
    )
    template = env.get_template('test.json')
    print(template.render(test='123'))

    if request.method == 'GET':
        print('GET method')
        return 'GET OK'
    elif request.method == 'POST':
        print('POST method')
        jsonParam = json.loads(request.get_data())
        cmd = jsonParam['cmd']
        import subprocess
        ret = subprocess.run(cmd)
        print('ret : {}'.format(ret))
        print(str(jsonParam))
        return 'Post OK'
    else:
        return 'Not supported method : {}'.format(request.method)

if __name__ == '__main__':
    app.run()
