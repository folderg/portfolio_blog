
from .views import frontend



def setup_routes(app):
    app.router.add_route('POST','/api/message.create',frontend.create_message)
    app.router.add_route('POST','/api/user.create',frontend.create_user)
    app.router.add_route('POST','/api/comment.create',frontend.create_comment)
    
    app.router.add_get('/',frontend.index)

   
    #app.router.add_view('/api/message.create',frontend.Create_message)
    #app.router.add_post('/',frontend.new_message)  
    #app.router.add_post('/api/',frontend.new_message_api)