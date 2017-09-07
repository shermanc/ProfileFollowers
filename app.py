from __future__ import (absolute_import, print_function)
import requests
import json



from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


def response_builder(github_id):
    response = {}
    follower_profile_list = []

    github_client = requests.get('https://api.github.com/user/' + github_id)

    if github_client.status_code == 200:

        user_data = json.loads(github_client.text)
        followers = requests.get(user_data['followers_url'])


        if len(json.loads(followers.text)) == 0:

            return {'github_username': user_data['login'],
                            'github_id': user_data['id'],
                            'profile_followers': []
                            }
        else:

            user_profile_followers = json.loads(followers.text)

            response.update({'github_username': user_data['login'],
                             'github_id': user_data['id'],
                             'profile_followers': []
                             })


            for follower in user_profile_followers:

                follower_profile = {'github_username': follower['login'],
                                    'github_id': follower['id'],
                                    'profile_followers': []
                                    }

                follower_profile_list.append(follower_profile)

            response['profile_followers'] = follower_profile_list

            return response

    else:

        if github_client.status_code == 404:
            message = 'user not found'
        else:

            message = 'something went wrong'

        return {'Error': {
            'error_code': github_client.status_code,
            'error_message': message
        }}


@app.route('/github/users/<string:github_id>')
def followers(github_id):

    if github_id is not None:
        response = response_builder(github_id)

        count = 0

        for follower in response['profile_followers']:
            if count > 5:
                continue
            inner_loop_count = 0
            profile_follower_response = response_builder(str(follower['github_id']))
            response['profile_followers'][count]['profile_followers'] = profile_follower_response['profile_followers']

            for profile in profile_follower_response['profile_followers']:
                if inner_loop_count > 5:
                    continue
                follower_response = response_builder(str(profile['github_id']))

                response['profile_followers'][count]['profile_followers'][inner_loop_count]['profile_followers'] = follower_response['profile_followers']
                inner_loop_count = inner_loop_count + 1
            count = count + 1
        return jsonify(response)
    else:
        return jsonify({'Error': {
                'error_code': 400,
                'error_message': "Please include Github Id param in the request"
            }})

if __name__ == '__main__':
    app.run(debug=True)