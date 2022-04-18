import requests
from pystyle import Colorate, Colors
from treelib import Tree
from pycenter import center
import os

os.system("cls")
title = """
         ,-.-.     ,----.                       ,-,--.    _,.----.                ,---.          _ __    
,-..-.-./  \==\ ,-.--` , \   _..---.          ,-.'-  _\ .' .' -   \  .-.,.---.  .--.'  \      .-`.' ,`.  
|, \=/\=|- |==||==|-  _.-` .' .'.-. \        /==/_ ,_.'/==/  ,  ,-' /==/  `   \ \==\-/\ \    /==/, -   \ 
|- |/ |/ , /==/|==|   `.-./==/- '=' /        \==\  \   |==|-   |  .|==|-, .=., |/==/-|_\ |  |==| _ .=. | 
 \, ,     _|==/==/_ ,    /|==|-,   '          \==\ -\  |==|_   `-' \==|   '='  /\==\,   - \ |==| , '=',| 
 | -  -  , |==|==|    .-' |==|  .=. \         _\==\ ,\ |==|   _  , |==|- ,   .' /==/ -   ,| |==|-  '..'  
  \  ,  - /==/|==|_  ,`-._/==/- '=' ,|       /==/\/ _ |\==\.       /==|_  . ,'./==/-  /\ - \|==|,  |     
  |-  /\ /==/ /==/ ,     /==|   -   /        \==\ - , / `-.`.___.-'/==/  /\ ,  )==\ _.\=\.-'/==/ - |     
  `--`  `--`  `--`-----```-._`.___,'          `--`---'             `--`-`--`--' `--`        `--`---'             

                                        By Nikuma


"""

print(Colorate.Horizontal(Colors.yellow_to_green, center(title)))

username = input(Colorate.Horizontal(Colors.yellow_to_green, "Username: "))

requet = requests.get(f"https://api.github.com/users/{username}")

data = requet.json()

tree = Tree()
ids = Tree()
url = Tree()
email = Tree()
follow = Tree()
Networks = Tree()
tree.create_node(Colorate.Color(Colors.green, f"\n{username}"), 1)
ids.create_node(Colorate.Color(Colors.green, f"Informations"), "informations")
ids.create_node(Colorate.Color(Colors.white, f"Identifiant: {data['id']}"), parent="informations")
ids.create_node(Colorate.Color(Colors.white, f"Pseudo: {data['login']}"), parent="informations")
ids.create_node(Colorate.Color(Colors.white, f"Biographie: {data['bio']}"), parent="informations")
ids.create_node(Colorate.Color(Colors.white, f"Location: {data['location']}"), parent="informations")
ids.create_node(Colorate.Color(Colors.white, f"Company: {data['company']}"), parent="informations")

url.create_node(Colorate.Color(Colors.green, f"Url"), "url")
url.create_node(Colorate.Color(Colors.white, f"Avatar url: {data['avatar_url']}"), parent="url")
url.create_node(Colorate.Color(Colors.white, f"Html url: {data['html_url']}"), parent="url")
url.create_node(Colorate.Color(Colors.white, f"Followers Url: {data['followers_url']}"), parent="url")
url.create_node(Colorate.Color(Colors.white, f"following url : {data['following_url']}"), parent="url")
url.create_node(Colorate.Color(Colors.white, f"following url : {data['gists_url']}"), parent="url")

email.create_node(Colorate.Color(Colors.green, f"Email(s)"), "email")
email.create_node(Colorate.Color(Colors.white, f"Email: {data['email']}"), parent="email")

follow.create_node(Colorate.Color(Colors.green, f"Follower"), "follower")
follow.create_node(Colorate.Color(Colors.white, f"Abonnée: {data['followers']}"), parent="follower")
follow.create_node(Colorate.Color(Colors.white, f"Abonnement: {data['following']}"), parent="follower")    

Networks.create_node(Colorate.Color(Colors.green, f"Networks and Blog"), "neting")
Networks.create_node(Colorate.Color(Colors.white, f"Blog: {data['blog']}"), parent="neting")
Networks.create_node(Colorate.Color(Colors.white, f"Twiter: {data['twitter_username']}"), parent="neting")

tree.paste(1, ids)
tree.paste(1, url)
tree.paste(1, email)
tree.paste(1, follow)
tree.paste(1, Networks)

tree.show()


