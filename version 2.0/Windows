import time


"""
--------------------------------------------------------------------------------------------------------------------
countdown
--------------------------------------------------------------------------------------------------------------------
"""

def countdown(total_time):
    total_time = findTimeTot(total_time)

    while total_time > 0:
        time.sleep(1)
        total_time -= 1
        displayTime(total_time)

def findTimeTot(total_time):
    # split up time
    time = total_time.split(':')

    iterations = len(time)
    multiplier = 1
    multiply = [1]

    # create value of specific type of digit
    for i in range(iterations): multiply.append(multiplier * 60)

    # multiply by value type of digit
    for i in range(iterations):
        value = -abs(i + 1)
        final_value = int(time[value]) * multiply[i]

    return final_value

def displayTime(total_time):
    m, s = divmod(total_time, 60)
    h, m = divmod(m, 60)
    timePrint = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    print('\r', timePrint, end="")

def waitInput():
    total_time = input('>> ')

    countdown(total_time)


"""
--------------------------------------------------------------------------------------------------------------------
spotify
--------------------------------------------------------------------------------------------------------------------
"""



"""
--------------------------------------------------------------------------------------------------------------------
execution
--------------------------------------------------------------------------------------------------------------------
"""

while True:
    waitInput()
