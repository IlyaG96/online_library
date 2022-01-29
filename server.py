import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell


def render_index_page():
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


render_index_page()

server = Server()
server.watch('/templates/*.html', render_index_page)
server.serve(root='.')
