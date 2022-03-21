nums = int(input())

parking_register = dict()
for i in range(nums):
    command_line = input().split(" ")
    if command_line[0] == "register":
        name = command_line[1]
        number = command_line[2]
        if name not in parking_register.keys():
            print(f"{name} registered {number} successfully")
            parking_register[name] = number
        else:
            print(f"ERROR: already registered with plate number {number}")
    elif command_line[0] == "unregister":
        name = command_line[1]
        if name not in parking_register:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_register[name]

for user, number in parking_register.items():
    print(f"{user} => {number}")
