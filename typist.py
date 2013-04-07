import sys

welcome_msg = "\nWelcome to Typist for Programmers!\n\nType 'start' to start learning practicing on your typing or type 'commands' for a list of commands\n"



def main():
	print welcome_msg
	inpt = get_input()
	execute(inpt)
	return 0


def get_input():
	user_input = raw_input("Type: ")
	return user_input 


def execute(inpt):
	
	if inpt ==

















if __name__ == "__main__":
	exit = main()
	sys.exit(exit)