# PomoTimer
a Pomodoro timer for the Linux Command line

Functions
setup
  downloads the necessary software to use the default set-up of the timer

timer

  required parameters
    on_time: how long it will be turned on for
    off_time: how long it will be turned off for
    iterations: how many times it will go through the cycle
    
  optional parameters
    turn_on: what action it does for the "work" part of the timer, defaults to turning on music using playerctl
    turn_off: what action it does for the "break" part of the timer, defaults to pausing the music using playerctl
