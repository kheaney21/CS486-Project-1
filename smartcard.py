from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from smartcard.CardConnectionObserver import CardConnectionObserver

from smartcard import *

name = 'Kelly Heaney'
assignment = 'Project 1'
description = 'Read ATR from smart card'

print(name, ' ', assignment, ' ', description)

#MasterCard A0000000041010

cardtype = AnyCardType()
cardrequest = CardRequest(timeout = 1, cardType = cardtype)
cardservice = cardrequest.waitforcard()

#add observer to watch for connect/disconnect, apdu command/response
ob = ConsoleCardConnectionObserver()
cardservice.connection.addObserver(ob)

cardservice.connection.connect()
print toHexString(cardservice.connection.getATR())
print cardservice.connection.getReader()

#mastercard
card = A0000000041010
byte = bytes(bytearray.fromhex(card))

header = 0x00, 0xA4, 0x04, 0x00, byte, 0x00, [0x9000]
#trailer =  

#apdu = header + trailer
apdu = header
#response is the returned apdu, sw1 and sw2 are status words to designate success or error
response, sw1, sw2 = cardservice.connection.trasmit(apdu)
print 'response: ', toHexString(response)