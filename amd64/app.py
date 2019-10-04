from flask import Flask
import os
import socket
import platform

app = Flask(__name__)

def get_ip():
    # IPv4
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        pass

    # IPv6
    try:
        return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
    except:
        pass

    return 'localhost'

@app.route("/")
def hello():
    html = "<h3>Hello MONSTER Kitty {name}!</h3>" \
	   "<b>IP Address:</b> {ipaddr}<br/>" \
	   "<b>Container :</b> {container}<br/>" \
	   "<b>Platform  :</b> {plat}<br/>" \
	   "<HR>" \
	   "<CENTER><IMG SRC=\"/static/helloKitty.png\" ALIGN=\"BOTTOM\"> </CENTER>" \
	   "<HR>"
    return html.format(name=os.getenv("NAME", "world"), ipaddr=get_ip(), container=socket.gethostname(), plat=platform.platform())

if __name__ == "__main__":
    app.run(host='::', port=80)
