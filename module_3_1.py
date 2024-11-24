calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(sstr):
    count_calls()
    return  len(sstr), sstr.upper(), sstr.lower()


def is_contains(sstr, list_str):
    contains = False
    for i in list_str:
        if sstr.lower() == i.lower():
            contains = True
            break
    count_calls()
    return contains


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)