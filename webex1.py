
import os
import ast
os.environ['WEBEX_TEAMS_ACCESS_TOKEN'] = 'OTJmNGUzMDctNjZiOS00MTA1LThiYzgtNjAwOGZmNDdmOWIxMzgyNzVlN2ItNDA3_PE93_9c184b70-71a8-484c-a9fd-6f9782462ba1'
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.components import TextBlock
from pyadaptivecards.actions import Submit

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI()

all_rooms = api.rooms.list()
my_rooms = [room for room in all_rooms if 'room' in room.title]
print(my_rooms)

my_room = api.rooms.create('room')

api.messages.create(my_room.id, text="hello world!")

#, files=["https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"]

print(my_room.id)

greeting = TextBlock("Basic Card")
first_name = Text('first_name', placeholder="First Name")
age = Number('age', placeholder="Age")

submit = Submit(title="Send me!")

card = AdaptiveCard(body=[greeting, first_name, age], actions=[submit])
#card2 = AdaptiveCard(body=[age],actions=[submit])
# Create a webex teams api connection

room_id = my_room.id
# Create a dict that will contain the card as well as some meta information
attachment = {
    "contentType": "application/vnd.microsoft.card.adaptive",
    "content": card.to_dict(),
}
api.messages.create(roomId=room_id, text="Fallback", attachments=[attachment])

for room in my_rooms:
   api.rooms.delete(room.id)
