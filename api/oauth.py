#!/usr/bin/python3

class Oauth(object):
    client_id = "717294639748612176"
    client_secrect = "1YzSdiXZMSCyloqS1NyYbYXwJsaf5N2o"
    scope = "identify" # %20 entro cada nuevo scope identify%20guilds.
    redirect_uri = "http://127.0.0.1:5000/login"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}"

