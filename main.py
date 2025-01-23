from application_queue.application_handler import Application
from palindrom_dequeue.palindrom import Palindrom

def parse_input(user_input):
    if not user_input:
        print("Please enter a command.")
        return "commands", []
    else: 
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args


def main():
    
    print("Welcome to the D&A bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in ["application", "1"]:
            application = Application()
            application.run()
        elif command in ["palindrom", "2"]:
            palindrom = Palindrom()
            print(palindrom.palindrom(args[0]))
        elif command in ["check", "3"]:
            pc = Palindrom()
            print(pc.check(args[0]))
        elif command in ["commands", "help", "command", "0"]:
            print("Available commands: hello, application, palindrom, check, help, commands, close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()