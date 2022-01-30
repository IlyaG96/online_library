import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import distribute, chunked
from pathlib import Path


def render_index_pages():

    with open(file='database/books.json', mode='r') as file:
        books = json.load(file)

    book_pages = list(chunked(books, 10))

    env = Environment(
        loader=FileSystemLoader('/Users/ilyagabdrakhmanov/PycharmProjects/online_library/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    Path('pages').mkdir(parents=True, exist_ok=True)

    for page_num, page_content in enumerate(book_pages):

        books_col1, books_col2 = distribute(2, page_content)

        template = env.get_template('template.html')
        rendered_page = template.render(books_col1=list(books_col1), books_col2=list(books_col2))
        with open(file=f'pages/index{page_num+1}.html', mode='w', encoding="utf8") as file:
            file.write(rendered_page)

    print('site reloaded')


def main():

    render_index_pages()
    server = Server()
    server.watch('templates/template.html', render_index_pages)
    server.serve(root='.')


if __name__ == '__main__':
    main()