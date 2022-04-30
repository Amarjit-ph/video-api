from ast import Mod
from dataclasses import fields
import re
from this import d
from typing_extensions import Required
from unittest import result
from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from numpy import flip

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# VIDEO MODEL
class VideoModel (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


db.create_all()
videos = {}


# REQUEST PARSER
videos_put_args = reqparse.RequestParser()
videos_put_args.add_argument(
    "name", type=str, help="Name of the video is required", required=True)
videos_put_args.add_argument(
    "views", type=int, help="Views of the video", required=True)
videos_put_args.add_argument(
    "likes", type=int, help="Likes of the video", required=True)


# ABORT
def abort_for_video_not_found(video_id):
    if video_id not in videos:
        abort(404, message="Your requested video is not found")


def abort_for_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Your video is already exist")


# RESOURCE FIELD
resource_field = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


# VIDEO
class Video(Resource):
    @marshal_with(resource_field)  # Serialization
    def get(self, video_id):
        # abort_for_video_not_found(video_id)
        result = VideoModel.query.get(id=video_id)
        return result

    @marshal_with(resource_field)  # Serialization
    def put(self, video_id):
        args = videos_put_args.parse_args()
        video = VideoModel(id)
        return videos[video_id], 201

    def delete(self, video_id):
        abort_for_video_not_found(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
