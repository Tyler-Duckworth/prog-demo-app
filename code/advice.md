To tune a PID use the following steps:

Set all gains to zero.
Increase the P gain until the response to a disturbance is steady oscillation.
Increase the D gain until the the oscillations go away (i.e. it's critically damped).
Repeat steps 2 and 3 until increasing the D gain does not stop the oscillations.
Set P and D to the last stable values.
Increase the I gain until it brings you to the setpoint with the number of oscillations desired (normally zero but a quicker response can be had if you don't mind a couple oscillations of overshoot)