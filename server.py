import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import distribute, chunked
from pathlib import Path


def render_index_pages():
    with open(file='online_library_example/media/books.json',
              mode='r') as file:
        books = json.load(file)
    books_on_page = 10
    book_pages = list(chunked(books, books_on_page))

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    Path('online_library_example/pages').mkdir(parents=True,
                                               exist_ok=True)
    cols_number = 2
    for page_num, page_content in enumerate(book_pages):
        books_col1, books_col2 = distribute(cols_number, page_content)

        template = env.get_template('template.html')
        rendered_page = template.render(books_col1=list(books_col1),
                                        books_col2=list(books_col2),
                                        number_of_pages=len(book_pages),
                                        current_page=page_num + 1
                                        )
        with open(file=f'online_library_example/pages/index{page_num + 1}.html',
                  mode='w',
                  encoding='utf8') as file:
            file.write(rendered_page)

    print('site reloaded')


def main():
    render_index_pages()
    server = Server()
    server.watch('templates/template.html', render_index_pages)
    server.serve(root='.')


if __name__ == '__main__':
    main()
