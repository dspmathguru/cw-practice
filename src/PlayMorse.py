#! /usr/bin/env python

from morse import Morse
import sounddevice as sd
import numpy as np
import argparse
import sys
import os


class PlayMorse:
  def __init__(self, wpm=20, Ftone=500):
    """Initializes the PlayMorse class with a specified words per minute (wpm)."""
    self.wpm = wpm
    self.morse = Morse()
    self.t_dit = 1.2 / wpm
    self.t_dah = 3 * self.t_dit
    self.t_intra_char = self.t_dit
    self.t_inter_char = self.t_dit
    self.t_inter_word = 3 * self.t_dit
    self.t_space = 7 * self.t_dit
    self.sample_rate = 44100
    self.Ftone = Ftone

  def __str__(self):
    """Returns a string representation of the PlayMorse class."""
    return f"PlayMorse(wpm={self.wpm})"

  def play(self, text):
    """Encodes text to Morse code and plays it."""
    morse_code = self.morse.encode(text)
    print(f"Playing Morse code for: {text}")
    print(morse_code)
    wave = self.encode(morse_code)
    sd.play(wave, samplerate=44100)
    sd.wait()
    print("Morse code playback finished.")

  def encode(self, morse_code):
    """Encodes Morse code into a waveform."""
    wave = []
    for char in morse_code:
      if char == '.':
        wave.extend(self.generate_tone(self.t_dit))
      elif char == '-':
        wave.extend(self.generate_tone(self.t_dah))
      elif char == ' ':
        wave.extend(self.generate_silence(self.t_space))
      else:
        raise ValueError(f"Invalid Morse code character: {char}")
      wave.extend(self.generate_silence(self.t_intra_char))
    return np.array(wave)

  def generate_tone(self, duration):
    """Generates a tone for the specified duration."""
    t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * self.Ftone * t)
    return tone.tolist()

  def generate_silence(self, duration):
    """Generates silence for the specified duration."""
    return [0.0] * int(self.sample_rate * duration)

  def __repr__(self):
    """Returns a string representation of the PlayMorse class."""
    return f"PlayMorse(wpm={self.wpm}, Ftone={self.Ftone})"

  def stop(self):
    """Stops playing Morse code."""
    print("Stopping Morse code playback.")
    # Here you would add the logic to stop the playback
    sd.stop()

  def set_wpm(self, wpm):
    """Sets the words per minute for Morse code playback."""
    self.wpm = wpm
    self.t_dit = 1.2 / wpm
    self.t_dah = 3 * self.t_dit
    self.t_intra_char = self.t_dit
    self.t_inter_char = self.t_dit
    self.t_inter_word = 3 * self.t_dit
    self.t_space = 7 * self.t_dit
    print(f"WPM set to {self.wpm}")

  def get_wpm(self):
    """Returns the current words per minute setting."""
    return self.wpm

  def get_tone_frequency(self):
    """Returns the current tone frequency."""
    return self.Ftone

  def set_tone_frequency(self, Ftone):
    """Sets the tone frequency for Morse code playback."""
    self.Ftone = Ftone
    print(f"Tone frequency set to {self.Ftone} Hz")

  def get_sample_rate(self):
    """Returns the current sample rate."""
    return self.sample_rate

  def set_sample_rate(self, sample_rate):
    """Sets the sample rate for Morse code playback."""
    self.sample_rate = sample_rate
    print(f"Sample rate set to {self.sample_rate} Hz")

  def get_timing_parameters(self):
    """Returns the timing parameters for Morse code playback."""
    """Returns the timing parameters for Morse code playback."""
    return {
        't_dit': self.t_dit,
        't_dah': self.t_dah,
        't_intra_char': self.t_intra_char,
        't_inter_char': self.t_inter_char,
        't_inter_word': self.t_inter_word,
        't_space': self.t_space
    }
  def set_timing_parameters(self, t_dit=None, t_dah=None, t_intra_char=None,
                            t_inter_char=None, t_inter_word=None, t_space=None):
    """Sets the timing parameters for Morse code playback."""
    if t_dit is not None:
      self.t_dit = t_dit
    if t_dah is not None:
      self.t_dah = t_dah
    if t_intra_char is not None:
      self.t_intra_char = t_intra_char
    if t_inter_char is not None:
      self.t_inter_char = t_inter_char
    if t_inter_word is not None:
      self.t_inter_word = t_inter_word
    if t_space is not None:
      self.t_space = t_space

def main():
  parser = argparse.ArgumentParser(description="Play Morse code from text input.")
  parser.add_argument("text", type=str, help="Text to convert to Morse code")
  parser.add_argument("--wpm", type=int, default=20,
                      help="Words per minute for Morse code (default: 20)")
  parser.add_argument("--Ftone", type=int, default=500, help="Tone frequency in Hz (default: 500)")
  args = parser.parse_args()

  player = PlayMorse(wpm=args.wpm, Ftone=args.Ftone)
  player.play(args.text)
  player.stop()


if __name__ == "__main__":
  main()
  sys.exit(0)
