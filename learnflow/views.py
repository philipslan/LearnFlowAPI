from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView
from learnflow.models import User, Track, Comment, Link
from mongoengine.base import ValidationError

from learnflow import flask_bcrypt

api = Blueprint('api', __name__, template_folder='templates')





class UserView(MethodView):

	def get(self):
		return jsonify(ye='ya')

	def post(self):
		data = request.get_json(force=True)

		new_user = User(
			username=data['username'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			hashed_pw=flask_bcrypt.generate_password_hash(data['password']),
			saved_tracks=[],
			mastered_tracks=[]
		)
		new_user.save()
		print new_user
		return jsonify(status="success", user=new_user)


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
			return jsonify(status="success", tracks=Track.objects().all())

	def post(self):
		data = request.get_json(force=True)
		author = User.objects(id=data['author_id']).first()
		new_track = Track(
			author=author,
			title=data['title'],
			description=data['description'],
			tags=[],
			links=[],
			children_tracks=[],
			completed=0,
			not_completed=0,
			hours=data['hours']
		)
		new_track.save()
		return jsonify(status="success", track=new_track)



class LinkView(MethodView):
	def get(self, link_id):
		if link_id is not None:
			try:
				link= Link.objects(id=link_id).first()
				if track:
					return jsonify(links=link)
				else:
					return jsonify(status="Link not found")
			except ValidationError:
				return jsonify(status="Link not found")
		else:
			return jsonify(links=Link.objects().all())


	def post(self):
		data = request.get_json(force=True)
		author = User.objects(id=data['author_id']).first()
		new_track = Link(
			url= data['url'],
			description= data['description']
		)
		new_link.save()
		return jsonify(status="success", link=new_link)
		

class CommentView(MethodView):


	def get(self, comment_id):
		if comment_id is not None:
			try:
				comment = Comment.objects(id=comment_id).first()
				if comment:
					return jsonify(comments=comment)
				else:
					return jsonify(status="Comment not found")
			except ValidationError:
				return jsonify(status="Track not found")
		else:
			return jsonify(status="success", comments=Comment.objects().all())

	def post(self):
		data = request.get_json(force=True)
		author  = User.objects(id=data['author_id']).first()
		track = Track.objects(id=data['track_id']).first()
		try:
			link = Link.objects(id=data['link_id']).first()
		except ValidationError:
			link = None
		new_comment = Comment(
			body=data['body'],
			author=author,
			track=track,
			node=link
		)
		new_comment.save()
		return jsonify(status="success", track=new_track)


# Register the urls
user_view = UserView.as_view('user_api')
api.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
api.add_url_rule('/users/', view_func=user_view, methods=['POST'])
api.add_url_rule('/users/<user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])


track_view = TrackView.as_view('track_api')
api.add_url_rule('/tracks/', defaults={'track_id': None}, view_func=track_view, methods=['GET'])
api.add_url_rule('/tracks/', view_func=track_view, methods=['POST'])
api.add_url_rule('/tracks/<track_id>', view_func=track_view, methods=['GET', 'PUT', 'DELETE'])

comment_view = CommentView.as_view('comment_api')
api.add_url_rule('/comments/', defaults={'comment_id': None}, view_func=comment_view, methods=['GET'])
api.add_url_rule('/comments/', view_func=comment_view, methods=['POST'])
api.add_url_rule('/comments/<comment_id>', view_func=comment_view, methods=['GET', 'PUT', 'DELETE'])

# Create Links
link_view = LinkView.as_view('link_api')
api.add_url_rule('/links/', defaults={'link_id': None}, view_func=link_view, methods=['GET'])
api.add_url_rule('/links/', view_func=link_view, methods=['POST'])
api.add_url_rule('/links/<link_id>', view_func=link_view, methods=['GET','PUT','DELETE'])

#core.add_url_rule('/update', view_func=StatusView.as_view('list'))
#core.add_url_rule('/status/<user_id>/', view_func=UserStatusView.as_view('status'))
#core.add_url_rule('/register', view_func=RegisterUserView.as_view('register'))
#core.add_url_rule('/login', view_func=LoginUserView.as_view('login'))
#core.add_url_rule('/possiblefriends', view_func=GatherFriendsView.as_view('possiblefriends'))
#core.add_url_rule('/groups', view_func=UserGroupsView.as_view('groups'))
#core.add_url_rule('/members', view_func=GroupMemberView.as_view('members'))


