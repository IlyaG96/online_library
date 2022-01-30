# Онлайн библиотека с фантастикой

Учебный проект для курсов web-разработчиков [dvmn](https://dvmn.org).  
Тестовый сайт можно посетитить, если нажать [сюда](https://ilyag96.github.io/online_library/pages/index1).

<img src="https://dvmn.org/media/lessons/qz65h.png"  width=50% height=50%>

## Установка
Понадобится установленный Python 3.8+ и git.

Клонируем репозиторий:
```bash
git@github.com:IlyaG96/online_library.git```
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
- Сами же обложки, тексты книг и json достает специальный скрипт, репозиторий с ним откроется в соседней вкладке, если нажать <a href="https://github.com/IlyaG96/parser_online_library" tagret="_blank">сюда</a>
</details>

