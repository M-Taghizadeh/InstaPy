from urllib.request import urlopen
import requests, datetime, time, json, random
from igql import InstagramGraphQL

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

# CUT
IGQL_API = InstagramGraphQL()
today = datetime.datetime.now()
UserMedia = []
Likes = []
Comments = []

# SOMETHINGS
URLS = []
months = {
    'Jan' : '01',
    'Feb' : '02',
    'Mar' : '03',
    'Apr' : '04',
    'May' : '05',
    'Jun' : '06',
    'Jul' : '07',
    'Aug' : '08',
    'Sep' : '09',
    'Oct' : '10',
    'Nov' : '11',
    'Dec' : '12',
}

# TOTAL LIKES && COMMENTS
def GetData(USERNAME):
    try :
        try :
            USER = IGQL_API.get_user(USERNAME)
        except :
            print (BG_P+" "+USERNAME+" "+BG_R+" NOT ON INSTAGRAM OR PRIVATE ACCOUNT "+W)
            pass
        for media in USER.timeline() :
            UserMedia.append(media)
        FinishWork(UserMedia)
    except KeyError :
        print(BG_R+" CANNOT GET IT RIGHT NOW "+BG_K+" CHANGE YOUR IP "+W)
        pass

def FinishWork(MEDIA):
    TotalLikes = 0
    TotalComments = 0
    for AllMedia in MEDIA :
        for Posts in AllMedia :
            node = Posts["node"]
            Likes.append(str(node["edge_media_preview_like"]["count"]))
            Comments.append(str(node["edge_media_to_comment"]["count"]))
    for like in Likes :
        LIKES = TotalLikes + int(like)
        TotalLikes = LIKES
        print (Y+"λ "+LB+"TOTAL LIKES :"+W,LIKES, end='\r')
        time.sleep(0.02)

    print (Y+"λ "+LB+"TOTAL LIKES :"+W,LIKES)
    for comment in Comments :
        COMMENTS = TotalComments + int(comment)
        TotalComments = COMMENTS
        print (Y+"λ "+LB+"TOTAL COMMENTS :"+W,COMMENTS, end='\r')
        time.sleep(0.02)
    print (Y+"λ "+LB+"TOTAL COMMENTS :"+W,COMMENTS)

# JOINED
def JoinedWork():
    try :
        for AllMedia in UserMedia :
            for Posts in AllMedia :
                node = Posts["node"]
                URLS.append(str(node["display_url"]))
        TARGET = urlopen(URLS[-1])
        data = TARGET.info()
        GhostWork(data, today)
    except :
        pass

def GhostWork(DATA, TODAY):
    try :
        # TODAY
        year = TODAY.strftime("%Y")
        day = TODAY.strftime("%d")
        month = TODAY.strftime("%m")

        # ACCOUNT
        JoinedIn = str(DATA["Last-Modified"])
        AccMonth = months[JoinedIn[8:11]]
        AccDay = JoinedIn[5:7]
        AccYear = JoinedIn[12:16]

        Real(day,month,year,AccDay,AccMonth,AccYear)
    except :
        pass

def Real(DAY,MONTH,YEAR,ACC_DAY,ACC_MONTH,ACC_YEAR):
    time.sleep(2)
    try :
        if int(MONTH) == int(ACC_MONTH) :
            FinalYear = int(YEAR) - int(ACC_YEAR)
            FinalMonth = int(MONTH) - int(ACC_MONTH)
            if int(DAY) < int(ACC_DAY) :
                FinalYear = int(YEAR) - 1 - int(ACC_YEAR)
                FinalMonth = int(MONTH) +12 - int(ACC_MONTH)
                FinalDay = int(DAY) + 30 - int(ACC_DAY)
                print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
                print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
            else :
                FinalDay = int(DAY) - int(ACC_DAY)
                print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
                print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
        elif int(MONTH) < int(ACC_MONTH) :
            FinalYear = int(YEAR) - 1 - int(ACC_YEAR)
            FinalMonth = int(MONTH) + 12 - int(ACC_MONTH)
            if int(DAY) < int(ACC_DAY) :
                FinalMonth = int(MONTH) + 12 - int(ACC_MONTH) - 1
                FinalDay = int(DAY) + 30 - int(ACC_DAY)
                print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
                print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
            else :
                FinalDay = int(DAY) - int(ACC_DAY)
                print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
                print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
        elif int(DAY) < int(ACC_DAY) :
            FinalYear = int(YEAR) - int(ACC_YEAR)
            FinalMonth = int(MONTH) - 1 - int(ACC_MONTH)
            FinalDay = int(DAY) + 30 - int(ACC_DAY)
            print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
            print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
        else :
            FinalYear = int(YEAR) - int(ACC_YEAR)
            FinalMonth = int(MONTH) - int(ACC_MONTH)
            FinalDay = int(DAY) - int(ACC_DAY)
            print (Y+"λ "+LB+"ACCOUNT AGE : "+W, end='')
            print (FinalYear,"YEAR",FinalMonth,"MONTH",FinalDay,"DAY.")
    except :
        pass

# LOCATIONS
def Location():
    Help = '"'
    Help2 = ':"'
    Help3 = ',"'
    Loca = []

    DisplayURLS = []
    UrlsDate = []


    DataFromJsonFile = {}

    data = {}
    for AllMedia in UserMedia :
        for Posts in AllMedia :
            node = Posts["node"]
            Loca.append(str(node["location"]))
            DisplayURLS.append(str(node["display_url"]))

            # SHORT
            DataFromJsonFile[str(node["shortcode"])] = {}
            DataFromJsonFile[str(node["shortcode"])]["shortcode"] = str(node["shortcode"])
            DataFromJsonFile[str(node["shortcode"])]["display_url"] = str(node["display_url"])
            DataFromJsonFile[str(node["shortcode"])]["location"] = str(node["location"])

    k = 1
    for PP in DataFromJsonFile :
        if "None" == DataFromJsonFile[PP]["location"] :
            pass
        else :
            X = DataFromJsonFile[PP]["location"]
            G = X.replace('True',"'True'")
            G = G.replace('False',"'False'")
            G = G.replace(": '",Help2)
            G = G.replace(", '",Help3)
            G = G.replace("{'","{"+Help)
            G = G.replace("':",Help+":")
            G = G.replace(":'",":"+Help)
            G = G.replace("',",Help+",")
            G = G.replace(",'",","+Help)
            G = G.replace("'}",Help+"}")
            Y = json.loads(G)
            data["LOCATION "+"#"+str(k)] = Y

            # LOCATION
            Location = data["LOCATION "+"#"+str(k)]["name"]
            LocationID = data["LOCATION "+"#"+str(k)]["id"]

            # GET DATE
            DataFromURL = urlopen(DataFromJsonFile[PP]["display_url"])
            WasHere = DataFromURL.info()["Last-Modified"]

            # POST URL
            Post = "https://instagram.com/p/"+DataFromJsonFile[PP]["shortcode"]
            k += 1


            ShowToUser(Location, LocationID, WasHere, Post)


def ShowToUser(LOCATION, LOCATION_ID, WAS_THERE, POST):
    List = [BG_K,BG_R,BG_P]
    X = random.choice(List)
    print (X+"LOCATION : ",LOCATION+W)
    print (X+"λ LOCATION ID : ",LOCATION_ID+W)
    print (X+"λ WAS HERE ON : ",WAS_THERE+W)
    print (X+"λ POST :",POST+W)

