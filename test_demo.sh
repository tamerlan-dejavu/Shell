#!/bin/bash

echo "TEST 1: Echo and basic commands"
echo 'echo "Hello from PYSHELL!"' | python shell.py | grep -v "pyshell>"
echo ""

echo "TEST 2: Pipe with word count"
echo 'echo "one two three four five" | wc -w' | python shell.py | grep -v "pyshell>"
echo ""

echo "TEST 3: File redirection"
echo 'echo "First line" > /tmp/test.txt' | python shell.py
echo 'cat /tmp/test.txt' | python shell.py | grep -v "pyshell>"
echo ""

echo "TEST 4: Append to file"
echo 'echo "Second line" >> /tmp/test.txt' | python shell.py
echo 'cat /tmp/test.txt' | python shell.py | tail -2 | head -1
echo ""

echo "TEST 5: Multiple pipes"
echo 'echo -e "python\njava\nruby\ngo" | grep -v java | wc -l' | python shell.py | grep -v "pyshell>"
