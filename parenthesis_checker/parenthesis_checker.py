from parenthesis_checker.stack import Stack

class ParenthesisChecker:
  def __init__(self):
    self.stack = Stack()

  def check(self, row):
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    
    for i, char in enumerate(row):
        if char in ["(","[","{"]:
            stack.push(char)
        elif char in [")","]","}"]:
            if not stack.is_empty() and stack.peek() == matching_brackets[char]:
                stack.pop()
    
    if stack.is_empty():
        return f"{"-" * 100}\n{row}: Cиметрично\n{"-" * 100}"
    else:
        return f"{"-" * 100}\n{row}: Не симетрично\n{"-" * 100}"

if __name__ == "__main__":
  pc = ParenthesisChecker()
  word = input("Enter a string to check if it's symmetric: ")
  print(pc.check(word))