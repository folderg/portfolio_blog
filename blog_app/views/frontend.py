import aiohttp
from aiohttp_jinja2 import template

import json
from aiohttp import web

from .. import db


Messages=[]

@template('index.html')
async def index(request):
    return {'name': 'username', 'messages' : Messages}


async def create_message(self):
    try:
        data = await self.json()
        session = db.create_session()
        note =db.Post()

        print (data)
        note.tittle= data.get('tittle')
        note.body = data.get('text')
        note.username = data.get('username')
        session.add(note)
        session.commit()
        session.close()
        Messages.append(data.get('text'))
        response_obj={'status':'ok'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def create_user(self):
    try:
        data = await self.json()
        session = db.create_session()
        note =db.User()
        
        print (data)
        note.password = data.get('password')
        note.username = data.get('username')
        session.add(note)
        session.commit()
        session.close()
        response_obj={'status':'ok'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)



async def create_comment(self):
    try:
        data = await self.json()
        session = db.create_session()
        note =db.Comment()
        
        print (data)
        note.comment = data.get('comment')
        note.username = data.get('username')
        session.add(note)
        session.commit()
        session.close()
        response_obj={'status':'ok'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)