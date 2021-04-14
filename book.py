import math

class Book:
  def __init__(self, name, char_count):
    self._name = name
    self.char_count = char_count
    self._characters = {}
    self._characters_prob = {}
    self._entropy = 0

  def get_name(self):
    return self._name
  
  def set_name(self, name):
    self._name = name
  
  def get_char_count(self):
    return self.char_count

  def set_char_count(self, char_count):
    self.char_count = char_count
  
  def get_characters(self):
    return self._characters

  def set_characters(self, characters):
    self._characters = characters
  
  def char_relative_prob(self):
    for char in self._characters:
      rel_prob = self._characters[char] / self.char_count
      self._characters_prob[char] = rel_prob
  
  def get_characters_prob(self):
    return self._characters_prob

  def calc_entropy(self):
    entropy = 0
    for char, rel_prob in self._characters_prob.items():
      entropy += rel_prob * math.log2(rel_prob)
    entropy *= -1
    self._entropy = entropy
    return entropy
  
  def get_entropy(self):
    return self._entropy
      
  def sort_char_rel_prob(self):
    sorted_chars = sorted(self._characters_prob, key=self._characters_prob.get)
    sorted_chars.reverse()
    sorted_probs_dict = {}

    for char in sorted_chars:
      sorted_probs_dict[char] = self._characters_prob[char]
    return sorted_probs_dict

  def total_char_prob(self):
    total_prob = 0
    for char, char_prob in self._characters_prob.items():
      total_prob += char_prob
    return total_prob