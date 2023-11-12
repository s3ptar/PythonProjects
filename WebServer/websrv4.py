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

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import http.server
import socketserver
"""*********************************************************************
* Informations
*********************************************************************"""
"""https://docs.aiohttp.org/en/stable/web_quickstart.html#run-a-simple-web-server"""
"""*********************************************************************
* Declarations
*********************************************************************"""

"""*********************************************************************
* Constant
*********************************************************************"""
hostName = "localhost"
serverPort = 8080
WebContent = "content"
project_path = os.path.dirname(os.path.abspath(__file__))
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
class handler_web_request(BaseHTTPRequestHandler):
    def do_GET(self):
        print("do_GET")
        if self.path == '/':
            self.path = 'content/index.html'
        #body = open(project_path+'\\content\\index.html').read()
        #self.send_response(200)
        #self.send_header("Content-type", "text/html")
        #self.send_header("Content-Length", str(len(body)))
        #self.end_headers()
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


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
    webServer = HTTPServer((hostName, serverPort), handler_web_request)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.") 
