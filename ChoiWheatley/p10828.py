class MyStack:
    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self, capacity):
        self.capacity = capacity
        self.__data = [0 for _ in range(capacity)]
        self.__top = -1

    def push(self, x: int):
        if self.__top == self.capacity - 1:
            raise MyStack.Full()
        self.__top += 1
        self.__data[self.__top] = x

    def pop(self) -> int:
        """값을 빼고 출력"""
        if self.__top < 0:
            raise MyStack.Empty()
        ret = self.__data[self.__top]
        self.__top -= 1
        return ret

    def __len__(self) -> int:
        return self.__top + 1

    def empty(self) -> bool:
        return self.__top < 0

    def top(self) -> int:
        """top 변수를 출력"""
        if self.empty():
            raise MyStack.Empty()
        return self.__data[self.__top]


if __name__ == "__main__":
    n = int(input())
    stack = MyStack(n)
    for _ in range(n):
        args = input().split()
        match args[0]:
            case "push":
                stack.push(int(args[1]))
            case "pop":
                try:
                    print(stack.pop())
                except MyStack.Empty:
                    print(-1)
            case "size":
                print(len(stack))
            case "empty":
                print(int(len(stack) == 0))
            case "top":
                try:
                    print(stack.top())
                except MyStack.Empty:
                    print(-1)
