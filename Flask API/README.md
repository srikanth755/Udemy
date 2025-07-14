# Flask API

It is a web framework that is created ussing the python programming language.

1. WSGI - Web Server Gateway Interface
2. Jinja 2 template Engine

Let us say we have a web server (AWS EC2, Azure APP, GCP etc) and have a web app that is to be deployed in web server. Many requests will come to the server and it sends the requests to the web app and gets the response. While doing this it follows a protocol named WSGI.

Jinja 2 template engine is used to create the dynamic webpages. Basically we have the web templates connected to different data sources (DB, ML model, Mongodb etc), so, web page connected to the data source is dynamic webpage.