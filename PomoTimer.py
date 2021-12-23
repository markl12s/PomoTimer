"""
PomoTimer

designed as a Pomodoro Timer system for doing schoolwork
"""
import typer
import time
app = typer.Typer()

"""
---------------------------------------------------------------------------------------------------------
terminal commands
---------------------------------------------------------------------------------------------------------
"""

@app.command()
def timer(on_time: str, off_time: str, iterations: str, turn_on='playerctl play', turn_off='playerctl pause'):
    on_time_arr = on_time.split(':')
    off_time_arr = off_time.split(':')

    iterations = int(iterations)

    on_time_tot = find_time_tot(on_time_arr)
    off_time_tot = find_time_tot(off_time_arr)

    for i in range(iterations):
        print(turn_on)
        time.sleep(on_time_tot)

        print(turn_off)
        time.sleep(off_time_tot)

@app.command()
def setup():
    print('sudo apt install playerctl')

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
        value = -abs(i)
        final_value = int(time[value]) * multiply[i]

    return final_value


"""
---------------------------------------------------------------------------------------------------------
execution
---------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    app()
