#!/usr/bin/python
#-*- coding: utf-8 -*-

## 실행방법
# python hello_world.py

import asyncio
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(5000)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
