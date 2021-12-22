"""
PomoTimer

designed as a Pomodoro Timer system for doing schoolwork
"""

import typer
import time
app = typer.Typer()

"""
---------------------------------------------------------------------------------------------------------
functions
---------------------------------------------------------------------------------------------------------
"""

@app.command()
def timer(on_time: str, off_time: str, iterations: str, turn_on='playerctl play', turn_off='playerctl pause'):
    on_time = float(on_time)
    off_time = float(off_time)
    iterations = int(iterations)

    for i in range(iterations):
        print(turn_on)
        time.sleep(on_time)
        
        print(turn_off)
        time.sleep(off_time)

@app.command()
def setup():
    print('sudo apt install playerctl')

"""
---------------------------------------------------------------------------------------------------------
execution
---------------------------------------------------------------------------------------------------------
"""

if __name__ == "__main__":
    app()
