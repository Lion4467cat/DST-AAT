class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]


if __name__ == "__main__":
    q = QueueUsingTwoStacks()
    n = int(input().strip())

    for _ in range(n):
        query = input().strip().split()
        if query[0] == '1':
            q.enqueue(int(query[1]))
        elif query[0] == '2':
            q.dequeue()
        elif query[0] == '3':
            print(q.peek())
