# Deploying to Heroku

## Prerequisites

If you haven't yet done so, [sign up for a Heroku account](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#prerequisites) and [install the Heroku CLI](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/heroku.md#installation), and make sure you can login and list your applications.

```sh
heroku login # just a one-time thing when you use heroku for the first time

heroku apps # at this time, results might be empty-ish
```

> NOTE: some students have reported that when running `heroku login` in Git Bash, it hangs after successfully logging them in. If this is the case for you, close that Git Bash window and when you open a new one you should be all set.

>NOTE: If you get IP Mismatch on web server. You can login in the terminal(OS user) by following commands

```sh
heroku login -i
```



## Server Setup

> IMPORTANT: run the following commands from the root directory of your repository!

Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different):

```sh
heroku create final-project-lcl # choose your own unique name!
```

Verify the app has been created:

```sh
heroku apps
```

Also verify this step has associated the local repo with a remote address called "heroku":

```sh
git remote -v
```
## Set up API key
You can either set api key value on the server or type in the terminal

For example:
```sh
heroku config # at this time, results might be empty-ish

# set environment variables:
heroku config:set APP_ENV="production"
```

## Deploying


1. You need to create a procfile on root directory, in this case, the file is already installed.
```sh
web: gunicorn "web_app:create_app()"
```
2. You need to install gunicorn package in the requirements.txt file

3. Before deployment, check you current working directory. Make sure it is one the right path

```sh
pwd
```

4. Check for the branch, it has to be on the main

```sh
git branch
```

5. After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:

```sh
git push heroku main
```

> NOTE: any time you update your source code, you can repeat this deployment command to upload your new code onto the server

## Running the Script in Production

Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:

```sh
heroku run bash # login to the server
# ... whoami # see that you are not on your local computer anymore
# ... ls -al # optionally see the files, nice!
# ... python -m app.daily_briefing # see the output, nice!
# ... exit # logout

# or alternatively, run it from your computer, in "detached" mode:
heroku run "python -m app.covid_lookup.py"
```

## Running web app from the server
After deploying app the heroku, we can now visit the web application through link below
https://final-project-lcl.herokuapp.com/





