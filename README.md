# Ausländerbehörde Daemon
This repository has the code to check if the website of the Immigration office in Hannover has changed and has 
appointments available. It will send a message to my Telegram if there is a change so that I can use the website and 
get an appointment fast.
1. [How to use?](#how-to-use)
2. [What is required?](#what-is-required)
3. [Future work](#future-work)

## How to use?
The repository contains a flask application with a daemon inside that will check the website every minute and if it
detects that the website has available appointments it will send a message using Telegram to an existing chatbot. 
The repository contains all the settings for a free Heroku deployment. However, it is my understanding that this free
tier will finish soon, therefore, it might not be free anymore and/or even not work. On the other side the code can run
locally too without any required changes and since it is not a consumption API the flask deveopment server will do
just fine.

The application is using the factory patter from flask, which is why instead if running the app like a python module, it
is recommended to run it using the flask command directly. The simplest way to run the application without 
specific settings would be the following command:
```
flask run
```
This command should be executed in the root folder.

## What is required?
In order to use this application, one needs to create an account in Telegram and a chat-bot in it.
TODO

## Future work
TODO
