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
def timer(on_time: str, off_time: str, iterations: str, turn_on=['cmatrix', 'playerctl play'], turn_off=['playerctl pause'], end_timer='nothing'):
    """use as
    PomoTimer timer hh:mm:ss iterations
    """

    # total amount of time in the on/off sessions
    on_time_tot, off_time_tot = find_time_tot(on_time), find_time_tot(off_time)

    iterations = int(iterations)

    # loop through actions, up until exit case
    for i in range(iterations - 1):
        turn_on_actions(turn_on, on_time_tot)
        turn_off_actions(turn_off, off_time_tot)

    # exit case
    turn_on_actions(turn_on, on_time_tot)
    if end_timer != 'nothing':
        os.system(end_timer)

@app.command()
def setup():
    os.system('sudo apt install playerctl')
    os.system('sudo apt install cmatrix')

"""
---------------------------------------------------------------------------------------------------------
functions
---------------------------------------------------------------------------------------------------------
"""

def find_time_tot(time_arr):
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

def turn_on_actions(turn_on, on_time_tot):
    # iterate through actions
    for i in range(len(turn_on)): os.system(turn_on[i])

    time.sleep(on_time_tot)

def turn_off_actions(turn_off, off_time_tot):
    # iterate through actions
    for i in range(len(turn_off)): os.system(turn_off[i])

    time.sleep(off_time_tot)

"""
---------------------------------------------------------------------------------------------------------
execution
---------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    app()
