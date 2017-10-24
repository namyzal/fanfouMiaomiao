#!/home/namyzal/.virtualenvs/fanfou6/bin/python
# -*- coding: utf-8 -*-
import time
import fanfou

consumer = {'key': 'db4736b0c26cd5699350e6b76df6dc87', 'secret': 'a801cf0d7437a5027423d6c080ba3daf'}
client = fanfou.XAuth(consumer, 'forumverify@126.com', '000aaa')
fanfou.bound(client)  

while True:
	curTime=time.localtime()
	curHr=curTime.tm_hour+8
	if curHr>=24:
		curHr=curHr-24
	curMin=curTime.tm_min
	curSec=curTime.tm_sec
	print str(curHr)+':'+str(curMin)+':'+str(curSec)
	if curMin==0 and curSec==0:
		nMW=curHr/10
		nM=curHr%10
		str1=''
		for i in range(0,nMW):
			str1=str1+'ß÷~'
		for j in range(0,nM):
			str1=str1+'ß÷ÎØ'			
		str1=str1+' '+str(curHr)+'µãÀ²'
		if curHr>=0 and curHr<=7:
			str1=str1+' zzZ zzZ'
		if nMW==0 and nM==0:
			body = {'status': 'ºÇÇ·~~~'}
		else:
			body = {'status': str1}
		client.statuses.update(body)
	time.sleep(1)
