# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)


def Push(Item):
    global Stack, TopOfStack
    if TopOfStack == 7:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return -1
    var = Stack[TopOfStack]
    TopOfStack -=1
    Stack[TopOfStack+1] = -1
    return var

# Exercise 2
def ShowStack():
    global Stack, TopOfStack
    S = ""
    if TopOfStack == -1:
        return ""
    for i in range(TopOfStack, -1, -1):
        S = S + f"{Stack[i]} "
    return S


# Exercise 3
def DecimalToBinary(Number):
    global Stack, TopOfStack
    S = ""
    if Number == 0:
        return "0"
    while Number > 0:
        Push(Number % 2)
        Number = Number // 2
    for i in range(TopOfStack,-1,-1):
        S = S + f"{Stack[i]} "
        Pop()
    return S


# Exercise 4
def Editor(Commands):
    global Stack, TopOfStack
    S = ""
    for i in range(1,len(Commands)):
        everycommand = Commands[i].split(" ")
        if everycommand[0] == "undo":
            Pop()
        else:
            Push(everycommand[1])
        for i in range(TopOfStack+1):
            S = S + Stack[i]
        return S

print(Editor(["type c", "type a", "type r", "undo", "type t"]))

# Exercise 4
def Editor(Commands):
  global Stack, TopOfStack
  TopOfStack = -1  # Added: clears the stack first

  for i in range(
      0, len(Commands)
  ):  # Changed 1 to 0 so the first command isn't skipped
    parts = Commands[i].split(" ")  # Added (" ") to actually run split

    if parts[0] == "undo":  # Added: handles the "undo" command
      Pop()
    else:
      Push(parts[1])  # Changed: pushes just the letter (index 1)

  # Added: builds and returns the final word from the stack
  result = ""
  for i in range(TopOfStack + 1):
    result = result + Stack[i]
  return result
