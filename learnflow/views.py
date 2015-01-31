from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView
from learnflow.models import User, Track, Comments, Link
from mongoengine.base import ValidationError

api = Blueprint('api', __name__, template_folder='templates')





class UserView(MethodView):

	def get(self):
		return jsonify(ye='ya')

	def post(self):
		return "yo"


class TrackView(MethodView):

	def get(self, track_id):
		if track_id is not None:
			try:
				track = Track.objects(id=track_id).first()
				if track:
					return jsonify(tracks=track)
				else:
					return jsonify(status="Track not found")
			except ValidationError:
				return jsonify(status="Track not found")
		else:
			return jsonify(tracks=Track.objects().all())

# Register the urls
user_view = UserView.as_view('user_api')
api.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
api.add_url_rule('/users/', view_func=user_view, methods=['POST'])
api.add_url_rule('/users/<user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])


track_view = TrackView.as_view('track_api')
api.add_url_rule('/tracks/', defaults={'track_id': None}, view_func=track_view, methods=['GET'])
api.add_url_rule('/tracks/', view_func=track_view, methods=['POST'])
api.add_url_rule('/tracks/<track_id>', view_func=track_view, methods=['GET', 'PUT', 'DELETE'])


#core.add_url_rule('/update', view_func=StatusView.as_view('list'))
#core.add_url_rule('/status/<user_id>/', view_func=UserStatusView.as_view('status'))
#core.add_url_rule('/register', view_func=RegisterUserView.as_view('register'))
#core.add_url_rule('/login', view_func=LoginUserView.as_view('login'))
#core.add_url_rule('/possiblefriends', view_func=GatherFriendsView.as_view('possiblefriends'))
#core.add_url_rule('/groups', view_func=UserGroupsView.as_view('groups'))
#core.add_url_rule('/members', view_func=GroupMemberView.as_view('members'))


