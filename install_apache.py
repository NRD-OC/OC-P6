import sys
import subprocess


def usage_error():
    print("Usage :")
    print("install_apache.py http://<website name>")
    print("or")
    print("install_apache.py https://<website name>")
    sys.exit(2)


def create_file(file_name, lines):
    open(file_name, 'w').write("")
    for line in lines:
        open(file_name, 'a').write(line + "\n")


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

apache_conf = '/etc/apache2/sites-available/001-' + web_site + '.conf'
web_directory = '/var/www/html/' + web_site
index_html = web_directory + '/index.html'
vhost = ["<VirtualHost *:" + port + ">",
         "  ServerName " + web_site,
         "  ServerAdmin webmaster@" + web_site,
         "  DocumentRoot " + web_directory,
         "",
         "  CustomLog ${APACHE_LOG_DIR}/" + web_site + "-access.log combined",
         "  ErrorLog ${APACHE_LOG_DIR}/" + web_site + "-error.log",
         "",
         "  <Directory " + web_directory + ">",
         "    Options All",
         "    AllowOverride None",
         "  </Directory>",
         "</VirtualHost>",
         ]
page = ["<!DOCTYPE html>",
        "<html>",
        "\t<head>",
        "\t\t<meta charset=\"utf-8\" />",
        "\t\t<title>Index - " + web_site + "</title>",
        "\t</head>",
        "",
        "\t<body>",
        "\t\t<p>Bienvenue sur " + web_site + " !</p>",
        "\t</body>",
        "</html>"
        ]


subprocess.run(["apt-get", "update"])
subprocess.run(["apt-get", "-y", "upgrade"])
subprocess.run(["apt-get", "-y", "install", "apache2"])

subprocess.run(["mkdir", web_directory])
create_file(apache_conf, vhost)
create_file(index_html, page)
subprocess.run(["a2ensite", "001-" + web_site])
subprocess.run(["a2dissite", "000-default"])
subprocess.run(["systemctl", "reload", "apache2"])
