# PYSHELL — Примеры для тестирования

Запусти shell и попробуй эти команды:

## 1. Простые команды

```bash
pyshell> echo hello world
hello world

pyshell> pwd
/path/to/current/directory

pyshell> ls
(список файлов в текущей директории)

pyshell> python --version
Python 3.14.3
```

## 2. Команды с аргументами

```bash
pyshell> echo "Hello, PYSHELL!"
Hello, PYSHELL!

pyshell> ls -la
(подробный список файлов)

pyshell> cat EXAMPLES.md
(содержимое этого файла)
```

## 3. Перенаправления (redirections)

```bash
# Вывод в файл
pyshell> echo "test content" > output.txt
pyshell> cat output.txt
test content

# Добавление в файл
pyshell> echo "more content" >> output.txt
pyshell> cat output.txt
test content
more content

# Ошибки в файл
pyshell> ls /nonexistent 2> error.log
pyshell> cat error.log
ls: cannot access '/nonexistent': No such file or directory
```

## 4. Pipes (конвейеры)

```bash
# Простой pipe
pyshell> echo "hello world" | wc -w
2

# Несколько pipes
pyshell> ls | wc -l
(количество файлов)

# grep через pipe
pyshell> ls | grep .py
(все файлы с расширением .py)
```

## 5. Комбинированные примеры

```bash
# Вывод в файл и через grep
pyshell> ls -la | grep .py > python_files.txt

# Несколько команд подряд
pyshell> pwd; ls; echo "Done"
/current/path
(список файлов)
Done
```

## 6. Что еще не работает (TODO)

- `cd` - изменение директории (builtin)
- `exit` - выход (builtin)
- Фоновые задачи (`&`)
- Ctrl+Z (SIGTSTP)
- Переменные окружения (`export`, `unset`)
- История команд (readline на Windows)

## Как запустить

```bash
python shell.py
```

Введи команду и нажми Enter. Ctrl+D для выхода.
