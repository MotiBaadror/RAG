import requests
import json

from simple_query import return_response, corpus_of_documents

user_input = "I dont like to hike"
relevant_document = return_response(user_input, corpus_of_documents)
full_response = []
# https://github.com/jmorganca/ollama/blob/main/docs/api.md
prompt = """
You are a bot that makes recommendations for activities. You answer in very short 
sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

url = 'http://localhost:11434/api/generate'
data = {
    "model": "llama3.2",
    "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document)
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
# print(response.status_code)
# print(response.text)
try:
    count = 0
    for line in response.iter_lines():
        # filter out keep-alive new lines
        # count += 1
        # if count % 5== 0:
        #     print(decoded_line['response']) # print every fifth token
        if line:
            decoded_line = json.loads(line.decode('utf-8'))

            full_response.append(decoded_line['response'])
finally:
    response.close()
print(''.join(full_response))