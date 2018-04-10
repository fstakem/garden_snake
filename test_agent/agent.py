from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

keywords = ['create', 'select', 'insert', 'drop',
                               'delete', 'from', 'where', 'table']

# commands
# -------------
# quit
# connect
# connect status
# disconnect
# subscribe
# send command

history = InMemoryHistory()
completer = WordCompleter(keywords, ignore_case=True)



def handle_cmd(cmd):
    print('cmd: {}'.format(cmd))

def main():
    while True:
        cmd = prompt('tester> ', history=history, auto_suggest=AutoSuggestFromHistory(), completer=completer)
        handle_cmd(cmd)


if __name__ == '__main__':
    main()


