from pynput import keyboard

ctr = keyboard.Controller()

money = int(input("Input unit : "))
money_ = money
def go(_money):
    money = int(_money)
    ctr.type([keyboard.Key.backspace])
    ctr.type(f'A{money}')
    ctr.type([keyboard.Key.enter])
    ctr.type(f'B{money}')
    ctr.type([keyboard.Key.enter])
    ctr.type(f'C{money}')
    ctr.type([keyboard.Key.enter])

def on_press(key):
    global money, money_
    try:
        if (key.char == '='):
            go(money)        
        elif (key.char == 't'):
            money = 1.2 * money
            go(money)
        elif (key.char == 'f'):
            money = 1.5 * money
            go(money)
        elif (key.char == 'q'):
            money = money_
            go(money)
        elif (key.char == '-'):
            ctr.type([keyboard.Key.backspace])
            ctr.type(f'取消')
            ctr.type([keyboard.Key.enter])

    except AttributeError:
        pass

 
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()