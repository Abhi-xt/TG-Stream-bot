
![GitHub Repo stars](https://img.shields.io/github/stars/code-x-mania/filestreambot?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/code-x-mania/filestreambot?color=green&style=flat)
![GitHub contributors](https://img.shields.io/github/contributors/code-x-mania/filestreambot?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/code-x-mania/filestreambot?color=yellow)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/code-x-mania/filestreambot)
![GitHub](https://img.shields.io/github/license/code-x-mania/filestreambot)
[![Bot Support](https://img.shields.io/badge/File%20Stream%20Bot-support%20group-blue)](https://t.me/codexmania)
<h1 align="center">FileStreamBot</h1>
<p align="center">
  <a href="https://github.com/code-x-mania/FileStreamBot">
    <img src="https://socialify.git.ci/Code-X-Mania/filestreambot/image?description=1&descriptionEditable=Powerful%20and%20fast%20bot%20made%20for%20streaming%20movies&font=Source%20Code%20Pro&forks=1&issues=1&language=1&owner=1&pattern=Floating%20Cogs&pulls=1&stargazers=1&theme=Dark" alt="Cover Image" width="650">
  </a>

  
  <p align="center">
    A Telegram bot to all media and documents files to web link .
    <br />
   </strong></a>
    <br />
    <a href="https://github.com/code-x-mania/FileStreamBot/issues">Report a Bug</a>
    |
    <a href="https://github.com/code-x-mania/FileStreamBot/issues">Request Feature</a>
  </p>


<hr>



## 🍁 About This Bot :

<p align="center">
    <a href="https://github.com/code-x-mania/FileStreamBot">
        <img src="https://i.ibb.co/DwQD0rK/download-1.jpg" height="100" width="100" alt="FileStreamBot Logo">
    </a>
</p>
<p align='center'>
    This bot will give you stream links for Telegram files without the need of waiting till the download completes
</p>


## ♢ How to make your own :

Either you could locally host or deploy on [Heroku](https://heroku.com)
### 💜 Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)

<br>

#### ♢ Click on This Drop-down and get more details

<br>
<details>
  <summary><b>Deploy on Heroku :</b></summary>


1. Fork This Repo
2. Click on the button to Deploy and follow steps

<h4> So Follow Above Steps 👆 and then deploy other wise bot won't work</h4>

Press the below button to Fast deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

then goto the <a href="#mandatory-vars">variables tab</a> for more info on setting up environmental variables. </details>


<details>
  <summary><b>Host it on VPS Locally :</b></summary>


```py
git clone https://github.com/code-x-mania/FileStreamBot
cd FileStreamBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m Code_X_Mania
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

Setting up things

If you're on Heroku, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:

```py
API_ID=12345
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
BIN_CHANNEL=-100
PORT=8080
FQDN=your_server_ip
OWNER_ID=your_user_id
DATABASE_URL=mongodb_uri
```
  </details>

<details>
  <summary><b>Vars and Details :</b></summary>

`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.

`OWNER_ID` : Your Telegram User ID

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can ask in [Me Telegram](https://t.me/adarshhh0).

 Option Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<details>
  <summary><b>How to Use :</b></summary>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.

To get an instant stream link, just forward any media to the bot and boom, its fast af.

### Channel Support
Bot also Supported with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button. </details>

### 🔷 Credits : 

- [Adarsh Goel_(me)](https://t.me/codexmania)
- [EverythingSuckz](https://github.com/EverythingSuckz) 
- Everyone In This Journey !

### Contributions By percentage
 - [Adarsh Goel_(me)](https://t.me/codexmania) for making some changes according to my taste + I added new features😎_________35% code
 - [EverythingSuckz](https://github.com/EverythingSuckz)   He owns the source code ;-;_______________________60% code
 - All who had helped me with logics  and plus who have helped [EverythingSuckz](https://github.com/EverythingSuckz)_________________5%  code
 - I dont own the source code . As told earlier I just made some changes I dont own it's base code 😇
 - Feel free to contribute  
 - 😀
 
 

