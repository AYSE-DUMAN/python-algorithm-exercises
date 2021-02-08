def index_of_caps(word):
 return [index for index, letter in enumerate(word) if letter.isupper()]

def is_valid_PIN(pin):
    	return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()

def accumulating_list(list):
    return [sum(list[:i+1]) for i in range(len(list))]


if __name__ == "__main__":
    print(index_of_caps("AabyzZ"))
    print(is_valid_PIN("1111"))
    print(accumulating_list([1,5,7]))
  