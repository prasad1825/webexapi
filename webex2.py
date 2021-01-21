import json
import urllib3
import requests
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'https://webexapis.com'
teams_path = "/v1/teams"
rooms_path = "/v1/rooms"
msg_path = "/v1/messages"
token = "Bearer OTJmNGUzMDctNjZiOS00MTA1LThiYzgtNjAwOGZmNDdmOWIxMzgyNzVlN2ItNDA3_PE93_9c184b70-71a8-484c-a9fd-6f9782462ba1"

teams_url = f"{host}{teams_path}"
rooms_url = f"{host}{rooms_path}"
msg_url = f"{host}{msg_path}"

teams_body = {
    "name" : "prasadroom"
}

headers = {
    "Authorization": token,
    "Content-type": "application/json"
}


#teams_post = requests.post(teams_url,headers=headers,data=json.dumps(teams_body),verify=False).json()
#teams_get = requests.get(teams_url,headers=headers,verify=False).json()
#pprint(json.dumps(teams_get, indent=2, sort_keys=True))

#teams = teams_get['items']

#for team in teams:
#    if team['name'] == "prasadroom":
#       teamId = team['id']
#       print(teamId)





rooms_body = {
    "title" : "room",
    #"teamId": teamId
}

rooms_post = requests.post(rooms_url,headers=headers,data=json.dumps(rooms_body),verify=False).json()
rooms_get = requests.get(rooms_url,headers=headers,verify=False).json()
pprint(json.dumps(rooms_get, indent=2, sort_keys=True))


rooms = rooms_get['items']

for room in rooms:
    if room['title'] == "room":
        roomId = room['id']
        print(roomId)

#### Exercise 1 ####

msg_body = {
   "roomId" : roomId,
   "text": 'hello world'
}



msg_post = requests.post(msg_url,headers=headers,data=json.dumps(msg_body),verify=False).json()
msg_get = requests.get(msg_url,headers=headers,verify=False).json()



#### Exercise 2 ####

msg_body1 = {
    "roomId": roomId,
    "text": "hello word",

"attachments": [
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "ColumnSet",
                    "columns": [

                        {

                            "type": "Column",
                            "width": 2,

                            "items": [

                                {
                                    "type": "TextBlock",
                                    "text": "do you like adaptive cards? ",
                                    "size": "large"
                                },
                                {
                                    "type": "Input.Text",
                                    "id": "input1",
                                    "placeholder": "enter comment",
                                    "maxLength": 500
                                },

                                {
                                    "type": "Input.ChoiceSet",
                                    "id": "input2",
                                    "style": "compact",
                                    "isMultiSelect": False,
                                    "label": "Default Input.ChoiceSet label (prasad)",
                                    "choices": [
                                        {
                                            "title": "Yes",
                                            "value": "Yes"
                                        },
                                        {
                                            "title": "No",
                                            "value": "No"
                                        }
                                    ]
                                }

                            ]

                        }

                    ]

                }

            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "OK"
                }
            ]
        }
    }
]
}

msg_post1 = requests.post(msg_url,headers=headers,data=json.dumps(msg_body1),verify=False).json()
