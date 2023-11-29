import logging
import requests
from openai import OpenAI

log = logging.getLogger()
log.setLevel(logging.DEBUG)

API_HOST = 'https://jsonplaceholder.typicode.com'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)


def test_openai(event, context):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


def list_posts(event, context):
    """ Retrieve posts list """
    url = API_HOST + '/posts'

    log.debug('calling ' + url)
    res = requests.get(url)

    response = {
        "statusCode": res.status_code,
        "body": res.text
    }

    return response


def get_post(event, context):
    """ Retrieve post by id """
    url = API_HOST + '/posts/' + str(event['pathParameters']['id'])

    log.debug('calling ' + url)
    res = requests.get(url)

    response = {
        "statusCode": res.status_code,
        "body": res.text
    }

    return response
