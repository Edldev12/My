n = int(input())
if n < 1 or n > 100:
    print("Invalid input. Please enter a number between 1 and 100.")
else:
    layers = []
    for i in range(1, n + 1): 
        if i % 2 != 0:
            layers.append("I hate")
        else:
            layers.append("I love")
    print(" that ".join(layers) + " it")
