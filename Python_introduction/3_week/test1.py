err = KeyboardInterrupt("here")
print(type(err), isinstance(err, Exception), err)

while True:
    try:
        print("Enter number:", end=" ")
        number = int(input())
    except ValueError:
        print("Something wrong, try again!")
    except KeyboardInterrupt:
        print("\nЯ тебя ща сука сам выключу! А ну иди сюда, тварь ебаная...")
        exit()
    else:
        print("Good job! Good boy!")
        break

print("Your number:", number)
print("")

database = {
    "green": [1, 3, 6, 2],
    "blue": [34, 2, 90]
}

def request_to_database(data = database):
    assert isinstance(data, dict), "Arg is not a dict!"
    try:
        color = input("Enter color:")
        index = int(input("Enter index:"))
        return data[color][index]
    except LookupError:
        print("Incorrect request, return None")
    finally:
        print("Finally block here!")

try:
    number = request_to_database()
except AssertionError as err:
    print(err)
    print("Error tryed")
print("\nReturned answer:", number)