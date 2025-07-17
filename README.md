# cw-practice
Morse code Python program to help with Practice

# Set up the virtual environment
I use direnv to manage virtual environments.  Be sure direnv is running for your shell.

Then do these steps:
- make .venv-linux # or make .vevn-osx
- direnv allow
- make

# Run the GUI
src/gui.py

# Run Play Morse
src/PlayMorse --WPM 20 "AF6UY"

# Requires PlayAudio to be installed

PlayAudio is a Python package to play audio files 
that requires Ubuntu Package playaudio to be installed.

```bash
apt install portaudio19-dev
```
