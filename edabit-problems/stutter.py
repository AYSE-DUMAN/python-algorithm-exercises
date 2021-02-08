def stutter(word):
    return word[:2] + "... " + word[:2] +"... "+ word + "?"


if __name__ == "__main__":
    print(stutter("incredible"))