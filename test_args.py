import sys


def usage_error():
    print("Usage :")
    print("install_apache.py http://<website name>")
    print("or")
    print("install_apache.py https://<website name>")
    sys.exit(2)
    
if len(sys.argv) != 2 or len(sys.argv[1]) < 8:
    usage_error()
else:
    url = sys.argv[1]
    if url[:7] == "http://":
        port = "80"
        web_site = url[7-len(url):]
    elif url[:8] == "https://" and len(url) > 8:
        port = "443"
        web_site = url[8-len(url):]
    else:
        usage_error()
        
