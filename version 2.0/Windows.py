import time
import spotipy

"""
--------------------------------------------------------------------------------------------------------------------
architecture
--------------------------------------------------------------------------------------------------------------------
"""

def userInput():
    user_inputs = waitInput()
    on_time, off_time, iterations = timeSplits(user_inputs)

    return on_time, off_time, iterations

def pomoCount(on_time, off_time, iterations):
    for i in range(iterations):
        countdown(on_time)
        countdown(off_time)

"""
--------------------------------------------------------------------------------------------------------------------
input
--------------------------------------------------------------------------------------------------------------------
"""

def waitInput():
    user_inputs = input('>> ')
    user_inputs = user_inputs.split(' ')

    return user_inputs

def timeSplits(user_inputs):
    on_time = user_inputs[0]
    off_time = user_inputs[1]
    iterations = user_inputs[2]

    return int(on_time), int(off_time), int(iterations)

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
    total_time = str(total_time)

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


"""
--------------------------------------------------------------------------------------------------------------------
spotify CURRENTLY WORKING ON WINDOWS 
--------------------------------------------------------------------------------------------------------------------
"""

def playMusic():
    start_playback()

def pauseMusic():
    stop_playback()


"""
--------------------------------------------------------------------------------------------------------------------
execution
--------------------------------------------------------------------------------------------------------------------
"""

# while True:
    # on_time, off_time, iterations = userInput()
    # pomoCount(on_time, off_time, iterations)


"""
--------------------------------------------------------------------------------------------------------------------
execution
--------------------------------------------------------------------------------------------------------------------
"""

playMusic()
pauseMusic()
