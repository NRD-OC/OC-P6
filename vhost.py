def create_file(file_name, lines):
    open(file_name, 'w').write("")
    for line in lines:
        open(file_name, 'a').write(line + "\n")


apache_conf = 'apache.conf'
web_site = 'test.com'
port = '80'
web_directory = '/var/www/html/' + web_site
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


create_file(apache_conf, vhost)

