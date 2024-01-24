# wifiautoflasher
A python program runs on an RPI to automatically flash wifi modules. Just put in your wifi module, press a button, and you're done!

The script uses the arduino cli tool - see here - https://arduino.github.io/arduino-cli/0.35/getting-started/

The script starts by pulling updates the github repository. If there were changes, it recompiles the code. Then it uploads the compiled code to the attached board.
