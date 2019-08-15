from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/t")
def hello():
    name = request.args.get('name', default = '*', type = str)
    description = request.args.get('description', default = '*', type = str)
    text="This is a text from a varialbe. "
    return text +" Parameters passed "+name+" " +description
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
