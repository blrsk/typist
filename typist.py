import sys
import subprocess
import re
import time

# GLOBALE VARIABLES
welcome_msg = "\nWelcome to Typist for Programmers!\n\nType 'start' to start practicing on your typing speed or type 'commands' for a list of commands.\n"

commands = ['start', 'commands', 'quit']

templates = [
"""
l
""",

"""
hacking is cool
""",

"""
indeed
""",

"""
it is.
""",

"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
"""
]



# RUNS PROGRAM
def main():
	clear_screen()
	print welcome_msg
	more = True
	while (more):
		inpt = prompt_input()
		more = execute_command(inpt)
	return 0



# UNIX SCRIPT TO CLEAR SCREEN
def clear_screen():
	subprocess.call('clear', shell=True)





# PROMPT INPUT
def prompt_input():
	user_input = raw_input("\nType:\n")
	return user_input

# MATCH COMMANDS TO FUNCTIONS
def execute_command(command):
	if command == 'quit':
		return False
	else:
		if command == 'commands':
			print "\nList of commands:"
			for c in commands:
				print "'" + c + "'" + ": " + c
			prompt_input()

		elif command == 'start':
			start()

		else:
			print "\nThis command does not match. Try again or press 'commands' for all available commands."
			prompt_input()
		return True


# COMMAND 'START'
start_msg = "Okay! Let's get started with a little placement test. When you are ready to start type this text:\n(You won't be able to go back if you make a mistake so try to be as precise as you can)"

def start():
	print start_msg
	for idx, val in enumerate(templates):
		new_exercise(val)

# ITERATE EXERCISE
def new_exercise(original_str):
	print original_str
	regex_check(original_str)

# LOAD REGEX AND CHECK USER INPUT
def regex_check(original_str):
	char_list = list(original_str)[1:-1]
	start = time.time()
	user_str = prompt_input()
	char_list_user = list(user_str)
	elapsed = str(int((time.time() - start)))
	errors = 0
	i = 0
	print '\n'
	print char_list
	print char_list_user
	for letter in char_list:
		if i < len(char_list_user):
			if letter != char_list_user[i]:
				errors += 1
			i += 1
		else:
			break
	print '\nYour time is ' + elapsed + ' seconds.'
	if errors != 0:
		print 'You have done ' + str(errors) + ' mistakes.'
	elif len(char_list) == len(char_list_user):
		print 'Perfect typing! Very impressive...'
	else:
		print 'You were on track but you did not finish...'







# GLETCH - TO READ ONE CHARACTER AT THE TIME

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()












if __name__ == "__main__":
	exit = main()
	sys.exit(exit)


