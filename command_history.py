# From https://stackoverflow.com/questions/6558765/how-do-you-see-the-entire-command-history-in-interactive-python

import readline
for i in range(readline.get_current_history_length()):
    print (readline.get_history_item(i + 1))