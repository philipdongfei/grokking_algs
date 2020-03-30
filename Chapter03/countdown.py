def countdown(i):
    print(i)
    if i <= 0:  # base case
        return
    else:       # recursive case
        countdown(i-1)


if __name__ == "__main__":
    countdown(5)

