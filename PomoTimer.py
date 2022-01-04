"""
PomoTimer
designed as a Pomodoro Timer system for doing schoolwork
"""
import typer
import time
import os

app = typer.Typer()

"""
---------------------------------------------------------------------------------------------------------
terminal commands
---------------------------------------------------------------------------------------------------------
"""

@app.command()
def timer(on_time: str, off_time: str, iterations: str, turn_on=['cmatrix', 'playerctl play'], turn_off=['playerctl pause'], end_timer='turn off'):
    """
    use as
    PomoTimer timer hh:mm:ss iterations
    you don't have to do hours, will split up any amount of types of time
    """

    # total amount of time in the on/off sessions
    on_time_tot, off_time_tot = findTimeTot(on_time), findTimeTot(off_time)

    iterations = int(iterations)

    # loop through actions, up until exit case
    for i in range(iterations - 1):
        turnOnActions(turn_on, on_time_tot)
        turnOffActions(turn_off, off_time_tot)

    exitCase(turn_on, on_time_tot, turn_off, off_time_tot)


"""
---------------------------------------------------------------------------------------------------------
functions
---------------------------------------------------------------------------------------------------------
"""

def findTimeTot(time_arr):
    # split up time
    time = time_arr.split(':')

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

def turnOnActions(turn_on, on_time_tot):
    # iterate through actions
    for i in range(len(turn_on)): os.system(turn_on[i])

    time.sleep(on_time_tot)

def turnOffActions(turn_off, off_time_tot):
    # iterate through actions
    for i in range(len(turn_off)): os.system(turn_off[i])

    time.sleep(off_time_tot)

def exitCase(turn_on, on_time_tot, turn_off, off_time_tot):
    turnOnActions(turn_on, on_time_tot)
    if end_timer != 'nothing':
        if end_timer == 'turn off':
            turnOffActions(turn_off, off_time_tot)
        else:
            os.system(end_timer)

"""
---------------------------------------------------------------------------------------------------------
execution
---------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    app()
