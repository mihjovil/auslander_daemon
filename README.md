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
locally too without any required changes and since it is not a consumption API, the flask development server will do
just fine.

The application is using the factory patter from flask, which is why instead if running the app like a python module, it
is recommended to run it using the flask command directly. The simplest way to run the application without 
specific settings would be the following command:
```
flask run
```
This command should be executed in the root folder and should start the flask environment with the application. As
above, this is not a high consumption API, which means that the flask default server will do the trick.

## What is required?
In order to use this application, one needs to create an account in Telegram and a chat-bot in it. 
[This post](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)
is a good example of the required steps to have a working bot in Telegram to communicate to. Since the application is
in Python, and it is a web application, one of the easiest ways to communicate to a phone and alert it of the 
availability of appointments is to use this chat communication to Telegram. 

The steps are the following:
1. Create a Telegram account or login to yours
2. Go to Settings and create an ID
3. Send a message to RawDataBot (that is a contact name one can find in the browser)
4. Copy your ID from the response
5. Search for BotFather and send `/start`. This will provide instructions to create a new bot with `/newbot`
6. Copy the access token from the response, this is necessary for all future communications

In the environmental variables of this project you must specify the token and the ID.

## Future work
TODO
