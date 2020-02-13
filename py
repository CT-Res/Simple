import asyncio
import logging
import re
import time
import os
from datetime import datetime
from aiowebsocket.converses import AioWebSocket
 

async def startup(uri):
 async with AioWebSocket(uri) as aws:
  converse = aws.manipulator
  #print("制作者：jvruo醉梦未苏\nQQ:1927699372\n\n注：表情无法显示")
  #time.sleep(2)
  #i=os.system("cls")
  ad=input('输入你网址最后一串数字')
  await converse.send('{"MessageType":"get","PlanId":'+ad+',"UserFlagFrom":"b4645","TextLimit":-50,"StartGoodId":0,"StartTextId":0,"StartSignalId":0,"UserIdFrom":8670390,"DeviceType":10}')
  while True:
   mes = await converse.receive()
   t=1
   st=mes.decode('UTF-8').replace('"','')
   mat=re.findall(r'mt:\w+',st)
   m1=re.findall(r'uf_n:(.*?),uf_t',st)
   m2=re.findall(r'c:(.*?),ct:',st)
   lu=re.findall(r'lu:(.*?),ls:',st)
   if(m2==None):
       print("<emjoy>")
       return
   for x in range(0,min(len(m1),len(m2))):
       if(mat[x]=='mt:signal'):
           continue
       print("\t\t\t",lu[x])
       print("uf_n:",m1[x])
       print("c:",m2[x])
   
if __name__ == '__main__':
 remote = 'wss://message.yunke.com/message.plan.ws?getOnlineUserSignal=0'
 try:
  asyncio.get_event_loop().run_until_complete(startup(remote))
 except KeyboardInterrupt as exc:
  logging.info('Quit.')
