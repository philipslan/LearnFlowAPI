from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView
from learnflow.models import User, Track, Comments, Link

api = Blueprint('api', __name__, template_folder='templates')





class UserView(MethodView):

	def get(self):
		return jsonify(ye='ya')

	def post(self):
		return "yo"




# Register the urls
api.add_url_rule('/user', view_func=UserView.as_view('user'))
#core.add_url_rule('/update', view_func=StatusView.as_view('list'))
#core.add_url_rule('/status/<user_id>/', view_func=UserStatusView.as_view('status'))
#core.add_url_rule('/register', view_func=RegisterUserView.as_view('register'))
#core.add_url_rule('/login', view_func=LoginUserView.as_view('login'))
#core.add_url_rule('/possiblefriends', view_func=GatherFriendsView.as_view('possiblefriends'))
#core.add_url_rule('/groups', view_func=UserGroupsView.as_view('groups'))
#core.add_url_rule('/members', view_func=GroupMemberView.as_view('members'))


