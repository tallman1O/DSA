# Stack Implementation Using List in Python

class stack_using_list:
    def __init__(self):
        self.stack = []

    # 1. Push Method
    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} to stack")

    # 2. Size Method
    def size(self):
        return len(self.stack)

    # 3. isEmpty Method
    def is_empty(self):
        return len(self.stack) == 0

    # 4. Pop Method
    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        return self.stack.pop()

    # 5. Top Method
    def top(self):
        if self.is_empty():
            print("Stack is empty, no top element")
            return None

        # return self.stack[len(self.stack) - 1] OR
        return self.stack[-1]


# Example Usage
if __name__ == "__main__":
    s = stack_using_list()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Top element is: {s.top()}")
    print(f"Stack size is: {s.size()}")
    print(f"Popped element is: {s.pop()}")
    print(f"Is stack empty? {s.is_empty()}")
    print(f"Popped element is: {s.pop()}")
    print(f"Is stack empty? {s.is_empty()}")
    print(f"Popped element is: {s.pop()}")
    print(f"Is stack empty? {s.is_empty()}")