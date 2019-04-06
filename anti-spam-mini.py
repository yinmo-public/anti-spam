# -*- coding: utf-8 -*-
from Line.linepy import *
from datetime import datetime
from time import sleep
#==================================================================================================================#
me = LINE()
me.log("Auth Token : " + str(me.authToken))
meMID = me.profile.mid
oepoll = OEPoll(me)
#==================================================================================================================#
def logError(text):
    me.log("[ 錯誤 ] " + str(text))
#==================================================================================================================#
def lineBot(op):
    try:
        if op.type == 5:
            me.blockContact(op.param1)
        if op.type == 13:
            if meMID in op.param3:
               group = me.getGroup(op.param1)
               if str(group.name).lower() in ["邀機","test","spam","邀機降臨","測試","。","幹","幹你娘","fuck"]:  #群名過濾
                  me.rejectGroupInvitation(op.param1)
               elif len(group.members) < 5:  #人數過濾
                  me.rejectGroupInvitation(op.param1)
        if op.type == 21 or op.type == 22 or op.type ==24:
            me.leaveRoom(op.param1)
        if op.type == 26 and op.message.contentType == 0:
            msg = op.message
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != me.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if 'ORGCONTP' in msg.contentMetadata.keys()!= None and msg.contentMetadata['ORGCONTP'] == "CALL":
                if msg.contentMetadata['GC_EVT_TYPE'] == "I":
                    me.blockContact(sender)
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except:
        pass
        
        
