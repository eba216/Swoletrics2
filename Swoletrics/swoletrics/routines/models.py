from swoletrics import db
from typing import List
from datetime import datetime


class Set(db.model):
    __tablename__ = "sets"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True)

    def __init__(self, reps: int, weight: float):
        self.reps = reps
        self.weight = weight

    def __str__(self):
        return f"{self.weight} x {self.reps}"


exercise_set = db.Table('exercise_set',
                        db.Column('set_id', db.Integer, db.ForeignKey('set.id'), primary_key=True),
                        db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True)
                        )


class Exercise(db.model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True)
    sets = db.relationship('Sets', secondary=exercise_set, lazy='subquery',
                           backref=db.backref('exercises', lazy=True)
                           )

    def __init__(self, name: str, date: datetime, sets: List[Set] = None, body_parts: List[str] = None):
        self.name = name
        self.date = date
        self.body_parts = body_parts
        self.sets = sets


workout_exercise = db.Table('workout_exercise',
                            db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
                            db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key=True)
                            )


class Workout(db.model):
    __tablename__ = "workouts"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True)

    def __init__(self, name: str, date: datetime, exercises: List[Exercise]):
        self.name = name
        self.date = date
        self.exercises = exercises

    # volume method


class Routine(db.model):
    __tablename__ = "routines"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True)
    routine = db.relationship('Routine', backref='user', lazy='dynamic')

    def __init__(self, name: str, date: datetime, workouts: List[Workout]):
        self.name = name
        self.date = date
        self.workouts = workouts

# class User(db.Model, UserMixin):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     #routine = db.relationship('Routine', backref='user', lazy='dynamic')
#     password_hash = db.Column(db.String)
#
#
# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )
#
# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))
#
# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
