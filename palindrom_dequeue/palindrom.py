from collections import deque
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from decorators.error_handler import input_error

class Palindrom:
  def __init__(self):
    self.queue = deque()

  @input_error
  def run(self, word):
    if word is None:
      raise ValueError("Word to check as palindrome cannot be null.")
    if not isinstance(word, str):
      raise ValueError("Word to check as palindrome must be a string.")
    
    word = word.strip().casefold()
    if len(word) <= 1 or  not word.isalpha():
      raise ValueError("Word to check as palindrome cannot be empty, one character or does not contain any letter.")
    
    print("Checking if the word is a palindrome...")

    for char in word:
      if char.isalpha():
        self.queue.append(char)

    while len(self.queue) > 1:
      if self.queue.popleft() != self.queue.pop():
        return False
    return True


if __name__ == "__main__":
  palindrom = Palindrom()
  word = input("Enter a word to check as a palindrome: ")
  print(palindrom.run(word))
