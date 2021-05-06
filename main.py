"""Idea taken from https://www.notion.so/Sentence-Email-Generator-a36d269ce8e94cc58daf723f8ba8fe3e"""

import os
import csv
from gpt import GPT, Example, set_openai_key
import json
import requests
from google.cloud import storage
from io import StringIO

set_openai_key(key=os.environ['OPENAI_KEY'])
# Construct GPT object and show some examples
gpt = GPT(
          # engine="davinci",
          engine="ada",
          temperature=0.2,
          max_tokens=25)

bucketClient = storage.Client(project='cyberdynesystems')
bucket = bucketClient.get_bucket(bucket_or_name="cyberdyne_system_models")
blob = bucket.get_blob(blob_name='emails.csv')
blob = blob.download_as_string()
blob = blob.decode('utf-8')
blob = StringIO(blob)

email_dataset = csv.reader(blob)

for row in email_dataset:
    email_file = row[0]
    expected_subject = row[1]

    expected_body = bucket.get_blob(blob_name='data/'+email_file)
    expected_body = expected_body.download_as_string()
    expected_body = expected_body.decode('utf-8')
    expected_body = StringIO(expected_body)
    expected_body = expected_body.replace('\n', '')

    gpt.add_example(Example(expected_body, expected_subject))

# Roy's changes from the cloud function
def get_subject_line(request):
    """
    This will Return an example subject line given an email body.
    :return:  subject line
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    body = request.args.get('body')
    suggestedSubjectLines = []

    for i in range(5):
        response = gpt.submit_request(body)
        offset = 0
        if not gpt.append_output_prefix_to_query:
            offset = len(gpt.output_prefix)
        line = response['choices'][0]['text'][offset:].replace('\n', '')
        if line not in [x['line'] for x in suggestedSubjectLines]:
            score = requests.get('https://us-central1-cyberdynesystems.cloudfunctions.net/spam_check?subjectLine={}'.format(line))
            score = json.loads(score.text)
            suggestedSubjectLines.append({'line': line,
                                         'hamScore': score.get('prediction_probability_pct').get('Ham')})
        if len(suggestedSubjectLines) == 3:
            break

    response = dict(suggested_subject_lines=suggestedSubjectLines)
    headers = {'Access-Control-Allow-Origin': '*'}

    return (json.dumps(response), 200, headers)


# Testing
class FakeRequest:

    def __init__(self, args):
        self.args = args
        self.method = 'post'

        self.test = dict()
myRequest = FakeRequest(args=dict(
                                  body="Dear Peter, I'm hungry and wan't to go to lunch.  are you going to lunch? Chinese food sounds great but Indian would be good too.",
                                  # body="Dear George, Do you like vacations?  I'm going to India and I wan't to bring a friend. How does the month of May sound?  Lets plan this vacation sometime soon."
                                  )
                      )

x = get_subject_line(request=myRequest)
print(x)