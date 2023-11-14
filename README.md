# adv-web-tech
That's my repo for the Advanced Web Tech module!


## Tech stack: 

1. Python Flask
2. SQAlchemy SQLite
3. Html templating with Jinja
4. CSS Bootstrap
5. OpenAI ChatGPT 3.5 Turbo API
6. Docker x Docker-compose
7. Gunicorn
8. Aiohttp + Werkzeug security
9. Caddy

## To start the application server

`git clone https://github.com/ervette/web-tech.git`

`cd web-tech`

`pip install -r requirements.txt`

`apt-get install caddy ` for Linux

`brew install caddy` for MacOS

`Follow the official site for windows installation` for Windows

`caddy start ./Caddyfile`

`gunicorn --timeout 600 main:app` 

`Go to https://webtech-2324-56.napier.ac.uk/ to access the app`