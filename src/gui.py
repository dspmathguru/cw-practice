#! /usr/bin/env python

import asyncio
import os
import sys
from nicegui import ui
from morse import Morse
from PlayMorse import PlayMorse

class MorseApp:
  def __init__(self):
    self.morse = Morse()
    self.play_morse = PlayMorse()
    self.setup_ui()

  def setup_ui(self):
    with ui.card().classes('w-full max-w-2xl mx-auto p-6 bg-gray-100 shadow-lg rounded-lg').style('margin-top: 50px;'):
      ui.label('Morse Code Translator').classes('text-h3')
      self.input_text = ui.input(label='Enter text to translate', placeholder='Type here...')
      self.output_text = ui.label('').classes('text-h5')
      self.play_button = ui.button('Play Morse Code', on_click=self.play_morse_code)
      self.translate_button = ui.button('Translate to Morse', on_click=self.translate_text)
      self.clear_button = ui.button('Clear', on_click=self.clear_fields)
      self.input_text.on('input', self.update_output)
      self.output_text.classes('text-monospace')
      self.input_text.classes('w-full')
      self.output_text.classes('w-full')
      self.play_button.classes('bg-blue-500 text-white')
      self.translate_button.classes('bg-green-500 text-white')
      self.clear_button.classes('bg-red-500 text-white')

  def translate_text(self):
    text = self.input_text.value
    if text:
      morse_code = self.morse.text_to_morse(text)
      self.output_text.set_text(morse_code)
    else:
      self.output_text.set_text('')

  async def play_morse_code(self):
    morse_code = self.input_text.value
    if morse_code:
      await self.play_morse.play(morse_code)
    else:
      ui.notify('No Morse code to play', color='red')

  def clear_fields(self):
    self.input_text.set_value('')
    self.output_text.set_text('')

  def update_output(self, event):
    text = self.input_text.value
    if text:
      morse_code = self.morse.text_to_morse(text)
      self.output_text.set_text(morse_code)
    else:
      self.output_text.set_text('')


if __name__ in {"__main__", "__mp_main__"}:
  app = MorseApp()
  if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  ui.run(title='Morse Code Translator', port=8084, reload=True)
