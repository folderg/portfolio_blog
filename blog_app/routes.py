
from .views import frontend



def setup_routes(app):
    app.router.add_route('GET','/',frontend.index)

    app.router.add_post('/api/',frontend.new_message_api)
    app.router.add_post('/',frontend.new_message)