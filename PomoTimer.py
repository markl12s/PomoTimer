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
    on_time_arr = on_time.split(':')
    off_time_arr = off_time.split(':')

    iterations = int(iterations)

    on_time_tot = find_time_tot(on_time_arr)
    off_time_tot = find_time_tot(off_time_arr)

    for i in range(iterations - 1):
        turn_on_actions(turn_on, on_time_tot)

        turn_off_actions(turn_off, off_time_tot)

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

def find_time_tot(time):
    iterations = len(time)
    multiplier = 1
    multiply = [1]

    for i in range(iterations): multiply.append(multiplier * 60)

    for i in range(iterations):
        value = -abs(i + 1)
        final_value = int(time[value]) * multiply[i]

    return final_value

def turn_on_actions(turn_on, on_time_tot):
    for i in range(len(turn_on)): os.system(turn_on[i])

    time.sleep(on_time_tot)

def turn_off_actions(turn_off, off_time_tot):
    for i in range(len(turn_off)): os.system(turn_off[i])

    time.sleep(off_time_tot)

"""
---------------------------------------------------------------------------------------------------------
execution
---------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    app()
