def parent(name):
    cash=10
    def play():
        nonlocal cash
        cash=cash-1
        print("Balance cash:",name,":",cash)
    return play
boy=parent("anish")
girl=parent("anisha")
boy()
boy()
boy()
girl()


