import json
from django.http import HttpResponse


def json_response(response_data):
    return HttpResponse(json.dumps(response_data),
            mimetype="application/json")
