import http.client
import json

def get_upcoming():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': '9df97b651e4244bbb8da6d50a6156d2b',
        'X-Response-Control': 'minified'
    }
    # should get next 7 fixtures
    connection.request('GET', '/v1/fixtures', None, headers)
    upcoming_fixtures = json.loads(connection.getresponse().read().decode())
    return upcoming_fixtures