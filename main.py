from book import Book
def main():
  quijote = open("el_quijote.txt", "r")
  quijote_data = quijote.read()

  book = Book(quijote.name, len(quijote_data))
  quijote.close()
  print(book.get_name(), book.get_char_count(), book.get_characters())

  for char in quijote_data:
    if char not in book.get_characters():
      book.get_characters()[char] = 1
    else:
      book.get_characters()[char] += 1

  book.char_relative_prob()
  print(book.get_characters_prob())
  print("\n\nEntropy:", book.calc_entropy())

if __name__ == '__main__':
  main()