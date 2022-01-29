import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('/Users/ilyagabdrakhmanov/PycharmProjects/online_library/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

with open(file="database/books.json", mode="r") as file:
    books = json.load(file)


template = env.get_template('template.html')
rendered_page = template.render(books=books)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

