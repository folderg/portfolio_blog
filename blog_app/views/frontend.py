import aiohttp
from aiohttp_jinja2 import template

import json
from aiohttp import web

Messages=[]

@template('index.html')
async def index(request):
    return {'name': '123', 'messages' : Messages}
    #return aiohttp.web.Response(text='Ok')


@template('index.html')
async def new_message(request):
    try:
        message = await request.text()
        message = message[message.find("=") + 1 : ]
        Messages.append(message)
        response_obj = {'status': 'succes', 'message':'message successfully created'}
        return {'name': 'username', 'messages' : Messages}
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)



async def new_message_api(request):
    try:
        message = await request.text()
        message = message[message.find("=") + 1 : ]
        Messages.append(message)
        response_obj = {'status': 'succes', 'message':'message successfully created'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)












async def new_message_api(request):
    try:
        #user=request.query['name']
        message = await request.text()
        print('creating a new message: ', message)
        Messages.append(message)
        response_obj = {'status': 'succes', 'message':'message successfully created'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj={'status':'failed','message':str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)
