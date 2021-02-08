def combinations(items):
    c = 1
    for i in range(1, items+1):
        c = c*i
    return c



if __name__ == "__main__":
    print(combinations(5))

