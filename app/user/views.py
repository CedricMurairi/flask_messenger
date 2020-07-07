#!/usr/bin/python3

from . import user


@user.route("/<string:username>/create-channel")
def create_channel(username):
	pass


@user.route("/<string:username>/join-channel")
def join_channel(username):
	pass
