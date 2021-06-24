import aiohttp
from aiohttp_jinja2 import template

import json
from aiohttp import web

from .. import db


Messages=[]

@template('index.html')
async def index(request):
    return {'name': 'username', 'messages' : Messages}


async def create_post(self):
    try:
        data = await self.json()
        session = db.create_session()
        note =db.Post()

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


async def get_messages(self):
    try:
        session = db.create_session()
        if(self.query):
            data = int(self.query['post'])
            print(data)
            posts = session.query(db.Post).filter(db.User.id==int(data))
        else:
            posts = session.query(db.Post).all()
        
        session.close()
        response_obj=[]
        for n in posts:
            response_obj.append({ n.id: n.body})
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)

