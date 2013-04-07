import sys
import subprocess
import re
import time
from termcolor import colored, cprint

"""
	REQUIRED APIs

	- Gletch: Input and read one character at the time.
	- termColor: Changes text color.

"""

# GLOBALE VARIABLES
total_speed = 0
sentences = 0



# MESSAGES
welcome_msg = 	"""
					\nType 'start' to start improving your typing speed or type 'commands' for a list of commands.\n
				"""

commands = {'start':'Start using the program.', 'next':'Go to level 2', 'commands':'Display list of commands.', 'rules':'Basic rules of the program.', 'stats':'See your average speed.', 'quit':'Exit the program.'}

templates1 = [
"""
keep hacking
""",

# """
# hacking is cool
# """,

# """
# 1, 2, 3!
# """,

# """
# I love you.
# """,

# """
# The cat is blue
# """
]

templates = [
"""
Did you know that the big hack is awesome?
""",

"""
It is pretty awesome believe me!
""",

"""
I love typing in the terminal.
"""
]

rules_msg = """
Before we start, here are a few rules that will help you learn faster:
 - Use your ten fingers to type at all times.
 - Only use the space bar for both spaces and indentation.
 - Do not use any other keys except characters and digits.
 - Once you've typed, you cannot erase, so just keep going.
 - Try to keep a steady pace and maintain the same speed when typing.
 - Typing is fun so enjoy yourself!
"""
start_msg = """
Let's get started!
"""
stats_msg = """
All sentences are designed to take between 10 and 20 seconds to type.
Each mistake you make adds 1 second to your total time.

 So here is a scale to help you understand where you stand:

  - Average speed lower than 8 seconds: You are a grand master hacker typist.
  - Average speed between 8 and 12 seconds: Damn you are fast. Keep up the good work!
  - Average speed between 12 and 15 seconds: You are a good typist. On your way to greatness.
  - Average speed between 15 and 18 seconds: You're solid. Keep these fingers moving.
  - Average speed between 18 and 20 seconds: Rome was not built in one day. You'll get there.
  - Average speed higher than 20 seconds: Go back to work!

  Start level 2! (type 'next')


"""


# RUNS PROGRAM
def main():
	clear_screen()
	print colored('\nWelcome to Hacker Typist!\n', 'magenta')
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
def prompt_input(str="\nType: "):
	user_input = raw_input(str)
	return user_input

# MATCH COMMANDS TO FUNCTIONS
def execute_command(command):
	if command == 'quit':
		return False
	else:
		if command == 'commands':
			print "\nList of commands:"
			for c in commands:
				print "'" + c + "'" + ": " + commands[c]
		elif command == 'rules':
			print rules_msg
		elif command == 'stats':
			show_stats()
			print stats_msg
		elif command == 'start':
			start()
		elif command == 'next':
			next()	
		else:
			print "\nThis command does not match. Try again or press 'commands' for all available commands."
		return True


# COMMAND 'START'
def start():
	print rules_msg
	prompt_input("Press enter to continue ")
	print start_msg
	for template in templates:
		new_exercise(template)
	print '\n'
	print "Congrats, you completed level 1. Check out your average speed! (type 'stats')"

# COMMAND 'NEXT'
def next():
	prompt_input("Press enter when you are ready to start ")
	for template in templates1:
		new_exercise(template)
	print '\n'
	print "Congrats, you completed level 2. Check out your average speed! (type 'stats')"

# ITERATE EXERCISE
def new_exercise(new_string):
	original_str = new_string
	print "Try that:\n" + original_str,
	regex_check(original_str)

# CHECK USER INPUT CHAR BY CHAR

def regex_check(original_str):
	char_list = list(original_str)[1:-1]
	k = 0
	errors = 0
	for letter in char_list:
		ch = getch()
		k += 1
		if k == 1:
			start = time.time()
		if ch == letter:
			sys.stdout.write(ch)
		else:
			sys.stdout.write(colored(ch, 'white', 'on_red'))
			errors += 1
	exact_elapsed = (time.time() - start)
	elapsed = str(round(exact_elapsed, 2))
	global total_speed
	total_speed += exact_elapsed + (errors)
	global sentences
	sentences += 1
	print '\n'
	if elapsed == 0:
		print "\nYour time is less than a second!"
	else:
		print '\nYour time is ' + elapsed + ' seconds.'
	if errors != 0:
		print 'You made ' + str(errors) + ' mistakes.'
	else:
		print 'Perfect typing! Very impressive...'
	print '\n'


# SHOW STATS

def show_stats():
	global total_speed
	global sentences
	avg_speed = total_speed / float(sentences)
	print colored('\nYour average speed is ' + str(round(avg_speed, 2)) + ' seconds per sentence.', 'blue')




# READ INPUT ONE CHARACTER AT THE TIME
class _Getch:
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


