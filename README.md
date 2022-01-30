# Онлайн библиотека с фантастикой

Учебный проект для курсов web-разработчиков [dvmn](https://dvmn.org).  
Тестовый сайт можно посетитить, если нажать [сюда](https://ilyag96.github.io/online_library/pages/index1).

<img src="https://dvmn.org/media/lessons/qz65h.png"  width=50% height=50%>

## Установка
Понадобится установленный Python 3.8+ и git.

Клонируем репозиторий:
```bash
git@github.com:IlyaG96/online_library.git
```
И незамедлительно создаем в этой папке виртуальное окружение:
```bash
cd online_library
python3 -m venv env
```

Не забываем его активировать:
```bash
source env/bin/activate
pip install -r requirements.txt
```
## Вероятные сценарии использования

### Какой такой питон? Я хочу просто скачать библиотеку!
<details>
<summary>Инструкция здесь :) </summary>

- Скачай весь код (иначе не выйдет) [по этой ссылке](https://github.com/IlyaG96/online_library/archive/refs/heads/main.zip)
- Разархивируй скачанный архив
- Перейди в папку pages (online_library/pages)
- Открой файл index1.html
- Если что-то идет не так, попробуй открыть страничку, используя веб-браузер Chrome
</details>

### Окей, неплохо, а откуда сайт данные берет?
<details>
<summary>Да все просто, открывай скорее!</summary>

- Сайт берет данные из онлайн-библиотеки [tululu.org](http://tululu.org/b9/)
- Сами же обложки, тексты книг и json достает специальный скрипт, репозиторий с ним откроется в текущем окне, если нажать <a href="https://github.com/IlyaG96/parser_online_library">сюда</a>
</details>

### Хочу добавить книг, обложек и запустить и себя.
<details>
<summary>Это будет не так просто, но ты точно справишься!</summary>

- Перейди в docs/database и обрати внимание на папки books и covers. В них будут помещены обложки книг и их тексты, но, прежде чем что-то туда закидывать, давай разберемся с файлом books.json.

```json
[
  {
    "title": "Алиби",
    "author": "ИВАНОВ Сергей",
    "cover_link": "http://tululu.org/shots/239.jpg",
    "comments": [
      "Детский вариант анекдотов про Шерлока Холмса)",
      "Загадки я люблю.)))",
      "А мне понравилось, люблю, знаете ли, всякие загадочки, головоломочки, кроссвордики, Гимнастика ума, одним словом... \nВо всём можно найти положительные моменты, не разгадал загадку, так хоть гренки научился готовить отменные... :-)",
      "Очень поучительное для ребенка 10 лет."
    ],
    "genres": [
      "Научная фантастика",
      "Прочие Детективы"
    ],
    "cover_name": "239.jpg"
  }
]
```
Он представляет из себя список словарей, в котором перечислены:
- Название книги (обязательно)
- Автор книги (обязательно)
- Ссылка на обложку книги 
- Комментарии
- Жанры книги (обязательно)
- Имя обложки, которое используется при рендеринге страниц (обязательно)

Чтобы добавить свою книгу, сначала нужно добавить запись в books.json, содержащую информацию о книге.
После - добавить текст книги в формате .txt в books и обложку в covers.   
Если обложки нет, то 
`cover_name` может быть `nopic.gif`

Сервер запускается командой
```shell
python server.py
```
Если видишь в терминале нечто подобное:
```shell
site reloaded
[I 220130 23:34:43 server:335] Serving on http://127.0.0.1:5500
[I 220130 23:34:43 handlers:62] Start watching changes
[I 220130 23:34:43 handlers:64] Start detecting changes
```
То сайт работает [по этому адресу](http://127.0.0.1:5500)
</details>
