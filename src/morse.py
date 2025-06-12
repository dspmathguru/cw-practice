#! /usr/bin/env python

class Morse:
  def __init__(self):
    self.morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': "---..", "9": "----.",
        ' ': ' ',  # Space is represented by a single space in Morse code
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.'
    }
    self.reverse_morse_code = {v: k for k, v in self.morse_code.items()}

  def encode(self, text):
    """Encodes a string into Morse code."""
    text = text.upper()
    morse = []
    for char in text:
      if char in self.morse_code:
        morse.append(self.morse_code[char])
      elif char == ' ':
        morse.append(' ')  # Preserve spaces
      else:
        raise ValueError(f"Character '{char}' cannot be encoded in Morse code.")
    return ' '.join(morse)

  def decode(self, morse):
    """Decodes a Morse code string into text."""
    morse_words = morse.split('   ')  # Split words by 3 spaces
    decoded_message = []
    for word in morse_words:
      decoded_chars = []
      for char in word.split():
        if char in self.reverse_morse_code:
          decoded_chars.append(self.reverse_morse_code[char])
        else:
          raise ValueError(f"Morse code '{char}' cannot be decoded.")
      decoded_message.append(''.join(decoded_chars))
    return ' '.join(decoded_message)

  def __str__(self):
    """Returns a string representation of the Morse code dictionary."""
    return '\n'.join(f"{k}: {v}" for k, v in self.morse_code.items())

  def __repr__(self):
    """Returns a string representation of the Morse class."""
    return f"Morse(morse_code={self.morse_code})"

  def __len__(self):
    """Returns the number of characters in the Morse code dictionary."""
    return len(self.morse_code)

  def __contains__(self, item):
    """Checks if a character is in the Morse code dictionary."""
    return item.upper() in self.morse_code or item in self.reverse_morse_code

  def items(self):
    """Returns the items of the Morse code dictionary."""
    return self.morse_code.items()

  def keys(self):
    """Returns the keys of the Morse code dictionary."""
    return self.morse_code.keys()

  def values(self):
    """Returns the values of the Morse code dictionary."""
    return self.morse_code.values()

  def get(self, key, default=None):
    """Returns the Morse code for a character, or a default value if not found."""
    return self.morse_code.get(key.upper(), default)

  def update(self, other):
    """Updates the Morse code dictionary with another dictionary."""
    if isinstance(other, dict):
      self.morse_code.update(other)
      self.reverse_morse_code = {v: k for k, v in self.morse_code.items()}
    else:
      raise TypeError("Argument must be a dictionary.")

  def clear(self):
    """Clears the Morse code dictionary."""
    self.morse_code.clear()
    self.reverse_morse_code.clear()

  def copy(self):
    """Returns a shallow copy of the Morse code dictionary."""
    return Morse.from_dict(self.morse_code)

  @classmethod
  def from_dict(cls, d):
    """Creates a Morse instance from a dictionary."""
    morse_instance = cls()
    morse_instance.morse_code = d
    morse_instance.reverse_morse_code = {v: k for k, v in d.items()}
    return morse_instance

  @staticmethod
  def is_morse_code(morse):
    """Checks if a string is valid Morse code."""
    valid_chars = set('.- ')
    return all(char in valid_chars for char in morse) and morse.strip() != ''

  @staticmethod
  def is_text(text):
    """Checks if a string is valid text for Morse code encoding."""
    return all(char.isalnum() or char.isspace() for char in text)

  @staticmethod
  def morse_to_text(morse):
    """Converts Morse code to text."""
    morse_instance = Morse()
    return morse_instance.decode(morse)

  @staticmethod
  def text_to_morse(text):
    """Converts text to Morse code."""
    morse_instance = Morse()
    return morse_instance.encode(text)

  @staticmethod
  def validate_morse_code(morse):
    """Validates if the input is a valid Morse code string."""
    if not Morse.is_morse_code(morse):
      raise ValueError("Invalid Morse code.")
    return True

  @staticmethod
  def validate_text(text):
    """Validates if the input is a valid text string for Morse code encoding."""
    if not Morse.is_text(text):
      raise ValueError("Invalid text for Morse code encoding.")
    return True

  @staticmethod
  def morse_length(morse):
    """Returns the length of a Morse code string."""
    Morse.validate_morse_code(morse)
    return len(morse.replace(' ', ''))  # Exclude spaces from length calculation

  @staticmethod
  def text_length(text):
    """Returns the length of a text string."""
    Morse.validate_text(text)
    return len(text.replace(' ', ''))  # Exclude spaces from length calculation

  @staticmethod
  def morse_word_count(morse):
    """Returns the number of words in a Morse code string."""
    Morse.validate_morse_code(morse)
    return len(morse.split('   '))  # Count words separated by 3 spaces

  @staticmethod
  def text_word_count(text):
    """Returns the number of words in a text string."""
    Morse.validate_text(text)
    return len(text.split())  # Count words separated by spaces

  @staticmethod
  def morse_character_count(morse):
    """Returns the number of characters in a Morse code string."""
    Morse.validate_morse_code(morse)
    return sum(len(char) for char in morse.split() if char)  # Count characters excluding spaces

  @staticmethod
  def text_character_count(text):
    """Returns the number of characters in a text string."""
    Morse.validate_text(text)
    return len(text)  # Count all characters including spaces


def main():
  morse_instance = Morse()
  print("Morse Code Dictionary:")
  print(morse_instance)

  text = "HELLO WORLD"
  morse_code = morse_instance.encode(text)
  print(f"Encoded '{text}' to Morse code: {morse_code}")

  decoded_text = morse_instance.decode(morse_code)
  print(f"Decoded Morse code '{morse_code}' to text: {decoded_text}")


if __name__ == "__main__":
  main()
