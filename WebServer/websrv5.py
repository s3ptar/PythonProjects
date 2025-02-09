# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""*********************************************************************
*! \file:                   websrv.py
*  \projekt:                python webserver
*  \created on:             07.03.2019
*  \author:                 R. Gräber
*  \version:                0
*  \history:                -
*  \brief
*********************************************************************"""

"""*********************************************************************
* Includes
*********************************************************************"""

import http.server
import socketserver
import json
import logging.config
from pythonjsonlogger import jsonlogger

"""*********************************************************************
* Informations
*********************************************************************"""
"""https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server"""
"""*********************************************************************
* Declarations
*********************************************************************"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "json",
        },
        "file":{
            "class" : "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "filename": "logfile.log",
            "maxBytes": 1024000,
            "backupCount": 3,
        },
    },
    "loggers": {"": {"handlers": ["file"], "level": "DEBUG"}},
}

"""*********************************************************************
* Constant
*********************************************************************"""
hostName = "localhost"
serverPort = 8087
DIRECTORY = "content"

"""*********************************************************************
* Global Variable
*********************************************************************"""

"""*********************************************************************
* local Variable
*********************************************************************"""

"""*********************************************************************
* Constant
*********************************************************************"""

"""*********************************************************************
* Local Funtions
*********************************************************************"""

"""*********************************************************************
*! \fn          async def handler_web_request(BaseHTTPRequestHandler)
*  \brief       handler function for web request
*  \param       BaseHTTPRequestHandler - request data
*  \exception   none
*  \return      side content
*********************************************************************"""
class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    #def _set_headers(self):
    #    self.send_response(200)
    #    self.send_header('Content-type', 'text/html')
    #    self.end_headers()

    #def do_HEAD(self):
    #    self._set_headers()
    def do_GET(self):
        print(self.path.rpartition('.')[-1])
        #self._set_headers()
        #self.send_response(200)
        #self.send_header('Content-type', 'text/html')
        #self.end_headers()
        #self.wfile.write(b'Hello, world!')
        if self.path == '/':
            self.path = '/content/index.html'
            #print("base path")
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        if self.path == '/content/css/style.css':
            self.path = '/content/css/style.css'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        if self.path == 'style.css':
            self.path = '/content/css/style.css'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        if self.path == '/content/js/javascript.js':
            self.path = '/content/js/javascript.js'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
            
        """    
        if self.path == '/readADC':
            #r="{<h1>Hello World</h1>}"
            r={'data':'test22'}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            json_string = json.dumps(r)
            self.wfile.write(json_string.encode(encoding='utf_8'))
            #self.wfile.write(r.encode("utf-8"))
            self.wfile.flush()
            print(r)

            #self.wfile.write("<?xml version='1.0'?>");
            #self.wfile.write("<sample>Some XML</sample>");
            #self.wfile.close();
        else:
            #self.path = 'content/index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        """
        if '/update?' in self.path:
            # self._set_headers()
            print(self.path[7:-1])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            #return http.server.SimpleHTTPRequestHandler.do_GET(self)

        if '/start_task!' in self.path:
            print(self.path[12:-1])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            json_obj = self.path[6:-1]

    def do_POST(self):
        print('connection ajax from:', self.address_string())


"""*********************************************************************
*! \fn          main routine
*  \brief       program starting point
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""

if __name__ == "__main__":        
    #body = open(project_path+'\\content\\index.html').read()
    #print(project_path+'\\content\\index.html')
    #print((body))
    logging.config.dictConfig(LOGGING)

    Handler = HttpRequestHandler
    Handler.extensions_map.update({
        '.html': 'text/html',
        '.css': '/content/css',
        '.js': '/content/js',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon',
    })
    Handler.DIRECTORY = "content"
    my_server = socketserver.TCPServer(("", serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    logging.info("An info")
    logging.warning("A warning")

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass

    my_server.server_close()
    print("Server stopped.") 
