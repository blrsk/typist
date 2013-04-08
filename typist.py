#!/Users/abalaresque/Desktop/typist/venv/bin/python
import sys
import subprocess
import time
from termcolor import colored, cprint

"""
	REQUIRED APIs

	- Gletch: Input and read one character at the time.
	- termColor: Changes text color.

"""

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


# RANDOM TEXT GENERATOR

"""CHOMSKY is an aid to writing linguistic papers in the style
    of the great master.  It is based on selected phrases taken
    from actual books and articles written by Noam Chomsky.
    Upon request, it assembles the phrases in the elegant
    stylistic patterns that Chomsky is noted for.
    To generate n sentences of linguistic wisdom, type
        (CHOMSKY n)  -- for example
        (CHOMSKY 5) generates half a screen of linguistic truth."""

leadins = """To characterize a linguistic level L,
    On the other hand,
    This suggests that
    It appears that
    Furthermore,
    We will bring evidence in favor of the following thesis:
    To provide a constituent structure for T(Z,K),
    From C1, it follows that
    For any transformation which is sufficiently diversified in application to be of any interest,
    Analogously,
    Clearly,
    Note that
    Of course,
    Suppose, for instance, that
    Thus
    With this clarification,
    Conversely,
    We have already seen that
    By combining adjunctions and certain deformations,
    I suggested that these results would follow from the assumption that
    If the position of the trace in (99c) were only relatively inaccessible to movement,
    However, this assumption is not correct, since
    Comparing these examples with their parasitic gap counterparts in (96) and (97), we see that
    In the discussion of resumptive pronouns following (81),
    So far,
    Nevertheless,
    For one thing,
    Summarizing, then, we assume that
    A consequence of the approach just outlined is that
    Presumably,
    On our assumptions,
    It may be, then, that
    It must be emphasized, once again, that
    Let us continue to suppose that
    Notice, incidentally, that """
# List of LEADINs to buy time.

subjects = """ the notion of level of grammaticalness
    a case of semigrammaticalness of a different sort
    most of the methodological work in modern linguistics
    a subset of English sentences interesting on quite independent grounds
    the natural general principle that will subsume this case
    an important property of these three types of EC
    any associated supporting element
    the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction
    the speaker-hearer's linguistic intuition
    the descriptive power of the base component
    the earlier discussion of deviance
    this analysis of a formative as a pair of sets of features
    this selectionally introduced contextual feature
    a descriptively adequate grammar
    the fundamental error of regarding functional notions as categorial
    relational information
    the systematic use of complex symbols
    the theory of syntactic features developed earlier"""
# List of SUBJECTs chosen for maximum professorial macho.

verbs = """can be defined in such a way as to impose
    delimits
    suffices to account for
    cannot be arbitrary in
    is not subject to
    does not readily tolerate
    raises serious doubts about
    is not quite equivalent to
    does not affect the structure of
    may remedy and, at the same time, eliminate
    is not to be considered in determining
    is to be regarded as
    is unspecified with respect to
    is, apparently, determined by
    is necessary to impose an interpretation on
    appears to correlate rather closely with
    is rather different from"""
#List of VERBs chosen for autorecursive obfuscation.

objects = """ problems of phonemic and morphological analysis.
    a corpus of utterance tokens upon which conformity has been defined by the paired utterance test.
    the traditional practice of grammarians.
    the levels of acceptability from fairly high (e.g. (99a)) to virtual gibberish (e.g. (98d)).
    a stipulation to place the constructions into these various categories.
    a descriptive fact.
    a parasitic gap construction.
    the extended c-command discussed in connection with (34).
    the ultimate standard that determines the accuracy of any proposed grammar.
    the system of base rules exclusive of the lexicon.
    irrelevant intervening contexts in selectional rules.
    nondistinctness in the sense of distinctive feature theory.
    a general convention regarding the forms of the grammar.
    an abstract underlying order.
    an important distinction in language use.
    the requirement that branching is not tolerated within the dominance scope of a complex symbol.
    the strong generative capacity of the theory."""
# List of OBJECTs selected for profound sententiousness.

import textwrap, random
from itertools import chain, islice, izip

def chomsky(times=1, line_length=72):
    parts = []
    for part in (leadins, subjects, verbs, objects):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length)




# GLOBALE VARIABLES
total_speed = 0
characters = 0
stats = []



# MESSAGES
welcome_msg = 	"""
					\nType 'start' to start improving your typing speed or type 'commands' for a list of commands.\n
				"""

commands = {'workout':'Generates random sentences to practice on.', 'start':'Start using the program.', 'next':'Go to level 2', 'commands':'Display list of commands.', 'rules':'Basic rules of the program.', 'stats':'See your average speed.', 'quit':'Exit the program.'}

templates = [
"Did you know that the big hack is awesome?",
"It is pretty awesome believe me!",
"I love typing in the terminal."
]

templates1 = [
"Keep hacking and stay healthy :)",
"I hope you are enjoying this little demo",
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

<<<<<<< HEAD
=======
  - Average speed lower than 8 seconds: You are a grand master hacker typist.
  - Average speed between 8 and 12 seconds: Damn you are fast. Keep up the good work!
  - Average speed between 12 and 15 seconds: You are a good typist. On your way to greatness.
  - Average speed between 15 and 18 seconds: You're solid. Keep these fingers moving.
  - Average speed between 18 and 20 seconds: Rome was not built in one day. You'll get there.
  - Average speed higher than 20 seconds: Go back to work!

  Start next level! (type 'next')


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
			for stat in stats:
				print '\n' + 'Your average speed was: ' + colored(str(round(stat, 2)), 'blue') + '\n'
		elif command == 'start':
			start()
		elif command == 'next':
			next()
		elif command == 'workout':
			workout()
		else:
			print "\nThis command does not match. Try again or press 'commands' for all available commands."
			prompt_input()
		return True


# COMMAND 'START'
def start():
	print rules_msg
	prompt_input("Press enter to continue ")
	print start_msg
	for template in templates:
		new_exercise(template)
	print '\n'
	show_stats()
	print '\n'
	print "Congrats, you completed level 1. On to the next level! (type 'next')"

# COMMAND 'NEXT'
def next():
	prompt_input("Press enter when you are ready to start ")
	for template in templates1:
		new_exercise(template)
	print '\n'
	show_stats()
	print '\n'
	print "Congrats, you completed level 2. Check out your average speed! (type 'stats')"

# COMMAND 'WORK OUT'
def workout():
	sentences_num = int(prompt_input("How many sentences would you like to generate? ") or 1)
	templates = []
	x = 0
	while x < sentences_num:
		 templates.append(chomsky(1))
		 x+=1
	print templates
	for template in templates:
		new_exercise(template)
	print '\n'
	show_stats()
	print '\n'
	print "You are done."

# ITERATE EXERCISE
def new_exercise(new_string):
	original_str = new_string
	print '\n'
	print "Try that:\n" + original_str
	regex_check(original_str)

# CHECK USER INPUT CHAR BY CHAR

def regex_check(original_str):
	char_list = list(original_str)
	global characters
	characters = len(char_list)
	k = 0
	errors = 0
	for letter in char_list:
		ch = getch()
		if ch == '0':
			return
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
	global characters
	avg_speed = total_speed / float(characters)
	print colored('\nYour average speed is ' + str(round(avg_speed, 2)) + ' characters per second.', 'blue')	
	stats.append(avg_speed)











if __name__ == "__main__":
	exit = main()
	sys.exit(exit)


