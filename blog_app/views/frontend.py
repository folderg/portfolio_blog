import aiohttp
from aiohttp_jinja2 import template

import json
from aiohttp import web

from .. import db


Messages=[]

@template('index.html')
async def index(request):
    return {'name': '123', 'messages' : Messages}

class Create_message(web.View):
    async def post(self):
        data = await self.request.json()
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

