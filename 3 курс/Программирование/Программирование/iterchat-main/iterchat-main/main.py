import asyncio
import tornado.ioloop
import tornado.web

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

        # localhost:8888/ -> Hello, world

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler), 
    ])

    # 

if __name__ == "__main__":
#python3 main.py or python main.py
	

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
