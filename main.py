from book import Book
from character import Character
from tabulate import tabulate

def sum_arr(characters):
  sum = 0
  for char in characters:
    sum += char.get_probability()
  return sum

def print_characters(characters, characters_dict):
  all_data = []

  for char in characters:
    char_data = []
    char_data.append(char.get_name())
    char_data.append(ord(char.get_name()))
    char_data.append(characters_dict[char.get_name()])
    char_data.append(char.get_probability())
    char_data.append(char.get_code())
    all_data.append(char_data)
  
  print(tabulate(all_data, headers=["CARACTER", "UNICODE", "OCURRENCIA", "PROBABILIDAD RELATIVA", "COMPRENSIÓN"]))

def shannon_fano(characters):
  if len(characters) == 1:
    return

  arr1 = []
  arr2 = []
  start = 0
  end = len(characters)-1

  while(start<=end):
    if sum_arr(arr1) <= sum_arr(arr2):
      characters[start].append_code("0")
      arr1.append(characters[start])
      start += 1
    else:
      characters[end].append_code("1")
      arr2.append(characters[end])
      end -= 1

  arr1 = sorted(arr1, key=lambda char : char.get_probability())
  arr2 = sorted(arr2, key=lambda char : char.get_probability())
  arr1.reverse()
  arr2.reverse()
  shannon_fano(arr1)
  shannon_fano(arr2)


def main():
  quijote = open("el_quijote_v2.txt", "r")
  quijote_data = quijote.read()

  book = Book(quijote.name, len(quijote_data))
  quijote.close()

  for char in quijote_data:
    if char not in book.get_characters():
      book.get_characters()[char] = 1
    else:
      book.get_characters()[char] += 1

  book.char_relative_prob()
  # print(book.get_characters_prob())

  sorted_probs = book.sort_char_rel_prob()
  # print("\n\nSorted probs dict:", sorted_probs)
  print("\nBook file name: "+book.get_name())
  print("\nBook total character count: {0}".format(book.get_char_count()))
  print("\nEntropy:", book.calc_entropy())
  print("\nTotal probability:", book.total_char_prob())
  print("\nShannon Fano Results: \n")

  characters = []
  for char, probability in sorted_probs.items():
    character = Character(char, probability)
    characters.append(character)

  shannon_fano(characters)
  print_characters(characters, book.get_characters())
  
  # character1 = Character('A', 0.22)
  # character2 = Character('B', 0.28)
  # character3 = Character('C', 0.15)
  # character4 = Character('D', 0.30)
  # character5 = Character('E', 0.05)

  # test = []
  # test.append(character1)
  # test.append(character2)
  # test.append(character3)
  # test.append(character4)
  # test.append(character5)

  # test = sorted(test, key=lambda char : char.get_probability())
  # test.reverse()
  # shannon_fano(test)
  # print_characters(test)

if __name__ == '__main__':
  main()