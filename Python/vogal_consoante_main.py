def ver(a):
  vogal = ['a', 'e', 'i', 'o', 'u']

  if a in vogal:
    print("A letra " + a + " é uma vogal.")
  else:
    print("A letra " + a + " é uma consoante.")

if __name__ == '__main__':
  a = input("Digite uma letra: ")
  ver(a)