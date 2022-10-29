import string


password = input("Enter the password!   ")
length = len(password)



lengthCondition = False


def is_small_condition_ok(char):
    return char.islower()


def is_big_condition_ok(char):
    return char.isupper()


def is_digit_condition_ok(char):
    return char.isdigit()


def is_spec_condition_ok(char):
    return char in string.punctuation


conditions = [{
    "condition": is_small_condition_ok,
    "success": False,
    "message": "You don't have small letters!"
}, {
    "condition": is_big_condition_ok,
    "success": False,
    "message": "You don't have big letters!"
}, {
    "condition": is_digit_condition_ok,
    "success": False,
    "message": "You don't have numbers!"
}, {
    "condition": is_spec_condition_ok,
    "success": False,
    "message": "You don't have a special symbol!"
}]

if len(password) == 0:
    print("You didn't enter your password!")
else:
    if length > 8:
        lengthCondition = True

    for char in password:
        for condition_item in conditions:
            if not condition_item["success"]:
                if condition_item["condition"](char):
                    condition_item["success"] = True

    level = 0
    for condition_item in conditions:
        if condition_item["success"]:
            level += 1

    if lengthCondition and level == len(conditions):
        print("You have a secure password!")
    else:
        if not lengthCondition:
            print("Your password too short!")
            level -= 1

        for condition_item in conditions:
            if not condition_item["success"]:
                print(condition_item["message"])

        if level < 3:
            print("Your password is not secure! (low level)")
        elif 3 <= level < 5:
            print("Your password is not secure! (medium level)")
