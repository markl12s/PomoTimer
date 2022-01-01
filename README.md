# PomoTimer
a Pomodoro timer for the Linux Command line

Functions
timer
  required parameters
    on_time: how long it will be turned on for
    off_time: how long it will be turned off for in format hour:minutes:seconds*
    iterations: how many times it will go through the cycle
    
  optional parameters
    turn_on: what action it does for the "work" part of the timer, defaults to turning on music using playerctl
    turn_off: what action it does for the "break" part of the timer, defaults to pausing the music using playerctl

*it can be any number of value types, but instead of days:hour:minutes:seconds it's just increments of 60 hours

required software to run this are playerctl and cmatrix, both are terminal programs
