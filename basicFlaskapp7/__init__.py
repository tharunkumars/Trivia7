import os

from flask import (
    Flask, 
    jsonify,
    app,
)

app = Flask(__name__)

def create_app(test_config):
    ##Creating a directory for SQLLite
    print ( " inside create_app " )
    print ( " inside test_config  " , test_config)
    app = Flask(__name__, instance_relative_config=True)

    print("instance_path", app.instance_path)
    print("instance name", app.name)

    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    """
    if test_config is None:
    # load the instance config, if it exists, when not testing
    # app.config.from_pyfile('config.py', silent=True)
        print("test_config ",test_config)
    else:
     # load the test config if passed in
        print("inside else")
        app.config.from_mapping(test_config)
    """
    try:
        print ( " inside makedirs " )
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

@app.route('/')
def hello_world():
    return 'Hello, World! , Hello , God'
    #return jsonify({'message':'Hello, World!'})
    #return app  

@app.route('/smiley')
def smiley():
    return ':)'

if __name__ == '__main__':
    print ( " inside main " )
    create_app(None)
    app.run(debug=True)