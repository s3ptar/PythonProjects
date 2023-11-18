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
import logging

"""*********************************************************************
* Informations
*********************************************************************"""
"""https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server"""
"""*********************************************************************
* Declarations
*********************************************************************"""

logging.basicConfig(filename="logging.log", encoding='utf-8')

"""*********************************************************************
* Constant
*********************************************************************"""
hostName = "localhost"
serverPort = 8089
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
    
    def do_GET(self):
        print(self.path.rpartition('.')[-1])
        print(self.path)
        if self.path == '/':
            self.path = '/content/index.html'
            #print("base path")
            #if self.path == '/css/style.css':
            #    self.path = 'content/css/style.css'
            #if self.path == '/js/javascript.js':
            #    self.path = 'content/js/javascript.js' 
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
            
            
        if self.path == '/readADC':
            #r="{<h1>Hello World</h1>}"
            r={'data':'test'}
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
    Handler = HttpRequestHandler
    Handler.extensions_map.update({
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'content/js',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon',
    })
    Handler.DIRECTORY = "content"
    my_server = socketserver.TCPServer(("", serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        my_server.serve_forever()
    except KeyboardInterrupt:
        pass

    my_server.server_close()
    print("Server stopped.") 
