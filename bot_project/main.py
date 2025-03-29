from assistant_bot.utils import parse_input
from assistant_bot.handlers import handle_command
from assistant_bot.data import contacts


def main():
    print("Welcome to assistant bot!")

    while True:
        user_input = input("Enter the command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break

        result = handle_command(command, args, contacts)
        print(result)

if __name__ == "__main__":
    main()
