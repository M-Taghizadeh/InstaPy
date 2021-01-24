# Import modules
import urllib.request
import json
import sys
import os
import time
try :
    import requests
    from igql import InstagramGraphQL
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install igql')
    sys.exit()

# For Console Color
W = "\033[0m"
G = '\033[32;1m'
Y = '\033[33;1m'
R = '\033[31;1m'
B = '\033[1;34;40m'
LB = '\033[1;36;40m'
BG_R = '\033[0;37;41m'
BG_G = '\033[0;37;42m'
BG_P = '\033[0;37;44m'
BG_K = '\033[0;37;45m'

dict = {
    "logo":'''
    ██╗███╗   ██╗███████╗████████╗ █████╗ ██████╗ ██╗   ██╗
    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║██╔██╗ ██║███████╗   ██║   ███████║██████╔╝ ╚████╔╝ 
    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═══╝   ╚██╔╝  
    ██║██║ ╚████║███████║   ██║   ██║  ██║██║        ██║   
    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝        ╚═╝  
    ''',
	"FirstMsg": '''
    \tWELCOME TO InstaPy TOOLS
    \tλ InstaPy V.1.0
    \tλ BY Mohammad Taghizadeh (Tqzdh) 
    \tλ Get Instagram Users Information''',
    "Spaces": "\n",
	"No Internet": " You Are Not Connected ",
	"Check": "You Must Be Connected With Internet ",
	"Connected": "You Are Connected\n",
	"Try": "Try Again\n",
	"GoodBye": "[~] See You Later ",
	"IK": '"',
	"Help": '''
    ······················································
    | Command                | For What                  |
    ······················································
    | Help                   | Show Help Table           |
    ······················································
    | CTRL + C + ENTER       | EXIT FROM THE TOOL        |
    ······················································
    | Exit                   | EXIT FROM THE TOOL	     |
    ······················································
    | Enter A Username       | Dump All User Information |
    ······················································
    ''',
	"Draw": '''
    + λ [ InstaPy V.1.0 ]
    + λ [ BY Mohammad Taghizadeh (Tqzdh) ]
    + λ [ Get Instagram Users Information ]
    >>> EXIT USE : CTRL + C + ENTER\n
    ''',
	"Target": {
        "USERNAME" : "",
    },
	"Headers": {
        "content-type": "application/json",
        "User-agent": "",
    }
}

# MAIN
def main():
    for char in dict["Connected"] :
        sys.stdout.write(BG_G+char+W)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.3)
    os.system('cls')
    Banner()

# FALSE MAIN
def FalseMain():
    for char in dict["No Internet"] :
        sys.stdout.write(BG_R+char+W)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for char in dict["Check"] :
        sys.stdout.write(Y+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    for char in dict["Try"] :
        sys.stdout.write(BG_R+char+W)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.exit()

# FLUSH
def Flush(Which):
    for char in Which :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.05)

class DumpFromJsonFile :    
    USERNAME = ""

    def GetUser(self):
        try :
            URL = 'https://www.instagram.com/'+self.USERNAME+'/?__a=1'
            req = requests.get(url=URL, headers=dict["Headers"])
            data = req.json()
        except :
            Flush(BG_P+" "+self.USERNAME+" "+BG_R+"NOT ON INSTAGRAM"+W+' > Error : GetUser() URL')
            sys.exit()
        try :
            STORY_URL = 'https://www.instagram.com/graphql/query/?query_hash=c9100bf9110dd6361671f113dd02e7d6&variables={'+dict["IK"]+'user_id'+dict["IK"]+':'+dict["IK"]+data["graphql"]["user"]["id"]+dict["IK"]+','+dict["IK"]+'include_reel'+dict["IK"]+':true,'+dict["IK"]+'include_logged_out_extras'+dict["IK"]+':true}'
            req_story = requests.get(url=STORY_URL, headers=dict["Headers"])
            story = req_story.json() ["data"]["user"]["has_public_story"]
        except :
            pass

        Flush(BG_R+"EXTRACTING DATA FROM : "+BG_P+" ", end='')
        Flush((data["graphql"]["user"]["username"]).upper())
        Flush(' '+W)

        # SUREFACE DATA
        Flush(BG_G+"SURFACE DATA "+W)
        Flush(Y+"λ "+LB+"FULL NAME : "+W, end='')
        Flush(data["graphql"]["user"]["full_name"])
        Flush(Y+"λ "+LB+"PRIVATE ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_private"]))
        Flush(Y+"λ "+LB+"VERIFIED ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_verified"]))
        Flush(Y+"λ "+LB+"BUSINESS ACCOUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_business_account"]))
        try :
            Flush(Y+"λ "+LB+"BUSINESS CATEGORY NAME : "+W, end='')
            Flush(str(data["graphql"]["user"]["business_category_name"]))
        except :
            pass
        Flush(Y+"λ "+LB+"SHOW SUGGESTED PROFILES : "+W, end='')
        Flush(str(data["show_suggested_profiles"]))
        Flush(Y+"λ "+LB+"SHOW FOLLOW DIALOG : "+W, end='')
        Flush(str(data["show_follow_dialog"]))
        Flush(Y+"λ "+LB+"SHOW VIEW SHOP : "+W, end='')
        Flush(str(data["show_view_shop"]))
        Flush(Y+"λ "+LB+"SHOW ACCOUNT CATEGORY : "+W, end='')
        Flush(str(data["graphql"]["user"]["should_show_category"]))
        try :
            Flush(Y+"λ "+LB+"ACCOUNT CATEGORY NAME : "+W, end='')
            Flush(data["graphql"]["user"]["category_name"])
            Flush(Y+"λ "+LB+"ACCOUNT CATEGORY ENUM : "+W, end='')
            Flush(data["graphql"]["user"]["category_enum"])
        except :
            pass
        Flush(Y+"λ "+LB+"BIO : "+W, end='')
        Flush(data["graphql"]["user"]["biography"])
        try :
            Flush(Y+"λ "+LB+"LINK IN BIO : "+W, end='')
            Flush(data["graphql"]["user"]["external_url"])
            Flush(Y+"λ "+LB+"INSIDE THIS LINK : "+W, end='')
            Flush(data["graphql"]["user"]["external_url_linkshimmed"])
        except :
            pass
        Flush(Y+"λ "+LB+"POSTS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
        Flush(Y+"λ "+LB+"FELIX VIDEOS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_felix_video_timeline"]["count"]))
        Flush(Y+"λ "+LB+"FOLLOWERS COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_follow"]["count"]))
        Flush(Y+"λ "+LB+"FOLLOWING COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
        Flush(Y+"λ "+LB+"HIGHLIGHT REEL COUNT : "+W, end='')
        Flush(str(data["graphql"]["user"]["highlight_reel_count"]))
        Flush(Y+"λ "+LB+"HAS PUBLIC STORY : "+W, end='')
        Flush(str(story))
        Flush(Y+"λ "+LB+"HAS AR EFFECTS : "+W, endFlush='')
        Flush(str(data["graphql"]["user"]["has_ar_effects"]))
        Flush(Y+"λ "+LB+"HAS CLIPS : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_clips"]))
        Flush(Y+"λ "+LB+"HAS GUIDES : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_guides"]))
        Flush(Y+"λ "+LB+"HAS CHANNEL : "+W, end='')
        Flush(str(data["graphql"]["user"]["has_channel"]))
        Flush ('')

        # DEEP DATA
        Flush (BG_K+"λ DEEP DATA "+W)
        Flush (Y+"λ "+LB+"LOGGING PAGE ID : "+W, end='')
        Flush(str(data["logging_page_id"]))
        Flush (Y+"λ "+LB+"ID : "+W, end='')
        Flush(data["graphql"]["user"]["id"])

        # DARK DATA
        Flush (BG_R+"DARK DATA "+W)
        Flush (Y+"λ "+LB+"IS JOINED RECENTLY : "+W, end='')
        Flush(str(data["graphql"]["user"]["is_joined_recently"]))
        Flush(Y+"λ "+LB+"ACCOUNT AGE : "+W)
        Flush(Y+"	"+BG_P+"LOOKING FOR ACCOUNT AGE "+W)
        Flush(W+'')
        try :
            Flush(Y+"λ "+LB+" CONNECTED WITH FACEBOOK : "+W,end='')
            Flush(str(data["graphql"]["user"]["connected_fb_page"]))
            Flush('')
        except :
            Flush(Y+"λ "+LB+" CONNECTED WITH FACEBOOK : "+W+" NO")

        Flush(Y+"λ "+LB+"FBID : "+W, end='')
        Flush(str(data["graphql"]["user"]["fbid"]))
        Flush(Y+"λ "+LB+"COUNTRY BLOCK : "+W, end='')
        Flush(str(data["graphql"]["user"]["country_block"]))

        Flush(Y+"λ "+LB+"EMAIL : "+W, end='')
        Flush("It can't be known right now.")
        Flush(Y+"λ "+LB+"PHONE : "+W, end='')
        Flush("It can't be known right now.")

# ASK
def Ask():
    try :
        command = input (LB+"λ InstaPy "+R+"/ "+LB+"USERNAME "+R+"> "+W)
        if command.lower() == "help" :
            Flush(dict["Help"])
            Ask()
        elif command.lower() == "exit" :
            Flush(BG_P+dict["GoodBye"]+W)
            sys.exit()
        else :
            try :
                dict["Target"]["USERNAME"] = command
                GetAll = DumpFromJsonFile()
                GetAll.USERNAME = dict["Target"]["USERNAME"]
                GetAll.GetUser()
            except :
                Flush(BG_P+" "+command+" "+BG_R+"NOT ON INSTAGRAM"+W+' > Error : GetAll.GetUser() Class')
                Flush(Y+"[!]"+G+" CHANGE YOUR IP ADDRESS THEN TRY AGAIN"+W)
                sys.exit()
    except KeyboardInterrupt :
        Flush(BG_P+dict["GoodBye"]+W)
        sys.exit()

# BANNER
def Banner():
    for space in dict["Spaces"]*5 :
        sys.stdout.write(space)
        sys.stdout.flush()
    for char in dict["logo"] :
        sys.stdout.write(R+char+W)
        sys.stdout.flush()
    time.sleep(0.1)
    for char in dict["Draw"] :
        sys.stdout.write(Y+char+W)
        sys.stdout.flush()
        time.sleep(0.005)
    Ask()

# CHECK INTERNET
def connect():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

# SCREEN
def Screen():
    os.system('cls')
    for space in dict["Spaces"]*5 :
        sys.stdout.write(space)
        sys.stdout.flush()
        time.sleep(0.01)
    for char in dict["logo"] :
        sys.stdout.write(R+char+W)
        sys.stdout.flush()
        time.sleep(0.005)
    time.sleep(0.1)
    for char in dict["FirstMsg"] :
        sys.stdout.write(B+char+W)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.1)
    for space in dict["Spaces"]*4 :
        sys.stdout.write(space)
        sys.stdout.flush()
        time.sleep(0.01)
    connect()
    if connect() :
        main()
    else :
        FalseMain()

# RUN
Screen()



