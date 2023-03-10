import requests
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to th OpenAI API")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "Your Key Here"
# api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": 'Bearer ' + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script to  ${args.prompt}",
    "max_tokens": 1000,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open("output.py", "w") as file:
        file.write(response_text)

else:
    print(f"Request failed with status code: {response.status_code}")