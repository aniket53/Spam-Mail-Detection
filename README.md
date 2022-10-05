
# Spam Mail Detection

Provide your mail body as input to the trained machine learning model and ML model will tell you that whether that mail is SPAM or HAM mail.



## Table of Contents
1. Deployment
2. Software & Tools
3. Commands
4. Features
5. Developers
6. Feedback
## Deployment

```bash
  spam-mail-detector-cicd.herokuapp.com
```


## Software & Tools

1. Github Account
2. Visual Studio Code IDE
3. Heroku Account
4. Git CLI 
## Commands
1. Create a new Environment
```bash
  conda create -p venv python==3.7 -y
```

2. To Run the Environment
```bash
  conda activate venv/
```

3. Create "requirements.txt"

4. Install all dependencies from "requirements.txt" file
```bash
  pip install -r requirements.txt
```

5. Git Setup
```bash
  git config --global user.name
  git config --global user.email
  git add . 
  git commit -m "commit message" 
  git push origin main
```

6. Run flask app
```bash
  python app.py
```

7. Heroku Deployment

```bash
  Create a Procfile
    web: gunicorn app:app
```
8. Heroku deployment using Docker and Github Actions(CICD Pipeline)
```bash
  Create two folders
    .github
    .github/workflows
  Create .yaml file
    main.yaml
```

9. Github Actions
```bash 
  Go to Repo settings->Secrets ->Actions ->New secret Key ->Add all the keys
```
## Features

1. Model is trained using Logistic Regression algorithm based on supervised learning.
2. Attribute Information (in order): 

        - mail-body
3. SPAM- mail is categorized as spam mail.
4. HAM- mail is categorized as normal mail.

## Developers

- [@aniket53](https://github.com/aniket53) 



## Feedback

Feel free to provide the feedback.

Contact Here:- akhot610@gmail.com
