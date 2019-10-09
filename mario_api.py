from flask import Flask, request, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import find_shortest_path
from database import db, mario_princess_model

# Create an instance of flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ninetendo.db'
app.config['SECRET_KEY'] = "random string"

# Initiate the database
db = SQLAlchemy(app)

# root adress for the game.
@app.route('/')
def welcome_page():
    return render_template('welcome_to_mario.html')


#get the deatils of grid and pass to pathToPrincess for processing
@app.route('/login',methods=['GET'])
def login():
        grid_crps = ''
        gridlen = int(request.args.get('gridlen'))
        for i in range(gridlen):
            row = 'member'+str(i)
            if(grid_crps==''):
                grid_crps = request.args.get(row)
            else:
                grid_crps = grid_crps + "," + request.args.get(row)
        return redirect(url_for('pathToPrincess_gui', glen = gridlen, grid=grid_crps))


# process the data and save the results
@app.route('/mario/<int:glen>/<grid>', methods=['GET'])
def pathToPrincess(glen,grid):
    grid = list([x for x in grid.split(',')])
    try:
        path = find_shortest_path(glen, grid)
        record = mario_princess_model(datetime.utcnow(), glen, str(grid), str(path))
        record.saveToDB()
    except Exception as e:
      print(e)
      return "Invalid Grid!!! Please Try again."
    return jsonify(path)

# GUI representation
@app.route('/mario_gui/<int:glen>/<grid>', methods=['POST','GET'])
def pathToPrincess_gui(glen,grid):
    grid = list([x for x in grid.split(',')])
    try:
        path = find_shortest_path(glen, grid)
        record = mario_princess_model(datetime.utcnow(), glen, str(grid), str(path))
        record.saveToDB()
    except Exception as e:
      print(e)
      return "Invalid Grid!!! Please Try again."
    return render_template('show_path.html', path=path, grid=grid, glen = glen)


# endpoint to get the log details
@app.route('/log')
def show_db_log():
    cum_path = mario_princess_model.query.all()
    json_path = [ path.json() for path in cum_path ]
    return jsonify(json_path)

# gui output for the game
@app.route('/result')
def show_grid_path():
    return render_template('show_table.html', msp =mario_princess_model.query.all())


if __name__ == '__main__':
    db.create_all()
    #app.run(debug=True)