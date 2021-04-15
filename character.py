class Character:
  def __init__(self, name, probability):
    self._name = name
    self._probability = probability
    self._code = ""
  

  def get_name(self):
    return self._name
  
  def set_name(self, name):
    self._name = name

  def get_probability(self):
    return self._probability

  def set_probability(self, probability):
    self._probability = probability

  def get_code(self):
    return self._code

  def append_code(self, code):
    self._code += code
  
  


