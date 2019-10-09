from flask_sqlalchemy import SQLAlchemy
from flask import flash

# Create instance of the db
db = SQLAlchemy()

class mario_princess_model(db.Model):
    __tablename__ = 'mario'

    def __init__(self, req_time, grid_size, grid_map, s_path):
        self.req_time = req_time
        self.grid_size = grid_size
        self.grid_map = grid_map
        self.s_path = s_path

    id = db.Column('grid_id', db.Integer, primary_key=True)
    req_time = db.Column(db.DateTime)
    grid_size = db.Column(db.String(10))
    grid_map = db.Column(db.PickleType)
    s_path = db.Column(db.PickleType)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
        flash('Record was successfully added')

    def json(self):
        return {
            'time_log': self.req_time,
            'grid_size': self.grid_size,
            'grid_map': self.grid_map,
            'short_path(s)': self.s_path
        }