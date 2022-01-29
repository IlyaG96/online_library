import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import distribute


def render_index_page():

    env = Environment(
        loader=FileSystemLoader('/Users/ilyagabdrakhmanov/PycharmProjects/online_library/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    with open(file="database/books.json", mode="r") as file:
        books = json.load(file)
    books_col1, books_col2 = distribute(2, books)

    template = env.get_template('template.html')
    rendered_page = template.render(books_col1=list(books_col1), books_col2=list(books_col2))

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    print('site reloaded')


render_index_page()

server = Server()
server.watch('templates/template.html', render_index_page)
server.serve(root='.')
