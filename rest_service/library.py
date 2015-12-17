from flask import Flask
import html
import json
import pickle
from mob_gen import *


app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
	return "Dungeon Crawler API v0.0.1"

@app.route("/mob_list/<mobs>", methods=['GET', 'POST', 'PUT'])
def mob_list(mob=None):
	if request.methods == 'POST':
		if mob != None:
			pickle.dump(MobGen.generate_mob(), mobs.pickle, json)#mob, mobs.pickle, PROTOCOL=json)
		else:
			return 'ERROR: Attempt to save a null or unknown object.  Please specify what mobs to add to the list.'
	if request.methods == 'GET':
		# do getty thing
		pass
	if request.methods == 'PUT':
		# modify/update the entire mob list
		pass
    # page = library.json('jsonhere')
    # page.body().h1("Welcome")
    # return str(page)
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)


# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()
