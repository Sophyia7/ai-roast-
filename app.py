from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
import markdown 

from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)

# GitHub authentication - store this securely in environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

# Define the authentication for Nebius API client connection 
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        repo = request.form['repo']
        

        # Get the languages used in the repo
        languages_url = f'https://api.github.com/repos/{username}/{repo}/languages'
        languages_response = requests.get(languages_url)
        languages = languages_response.json() if languages_response.status_code == 200 else {}

        # Get user's commits from the username and repository
        commits_message = f'https://api.github.com/repos/{username}/{repo}/commits'
        commits_response = requests.get(commits_message, headers=HEADERS)

        if commits_response.status_code != 200:
            return f"Error: {commits_response.json().get('message')}"
        
        commits = []
        for commit in commits_response.json():
            commit_info = {
                'commit_message': commit['commit']['message'],
                'author': commit['author']['login'],
                'date': datetime.strptime(commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d'),
                'url': commit['html_url']
            }
            commits.append(commit_info)


        prompt = f""" You are a senior developer known for your sharp wit and brutally honest feedback. I need you to take a look at my commit history and unleash your most savage, technically-accurate roast. 
        I want you to dissect every bad practice, point out every flaw, and do it with a sense of humor that stings yet educates. 
        Here's my commit history: {commits}
        
        Don't hold back - I want to feel the burn of your technical criticism. Make sure your response is in two paragraphs: the first paragraph should be your most ruthless roast, filled with humor and technical insights, and the second paragraph should offer constructive advice on how I can improve my commit practices. 
        Your feedback should be both enlightening and entertaining.
        """

        # Init the model and generating the roast
        response = client.chat.completions.create(
            model="google/gemma-2-27b-it",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            top_p=0.9
        )
        roast = response.choices[0].message.content
        formatted_roast = markdown.markdown(roast)

        return render_template('result.html', roast=formatted_roast, languages=languages)
    
    return render_template('index.html')




# Keep running the app when changes are made
if __name__ == '__main__':
    app.run(debug=True)
else:
    print("The application is running in a production environment.")






