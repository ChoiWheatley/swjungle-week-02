# class MyStack:
#     class Full(Exception):
#         pass

#     class Empty(Exception):
#         pass

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.__data = [0 for _ in range(capacity)]
#         self.__top = -1

#     def push(self, x: int):
#         if self.__top == self.capacity - 1:
#             raise MyStack.Full()
#         self.__top += 1
#         self.__data[self.__top] = x

#     def pop(self) -> int:
#         """값을 빼고 출력"""
#         if self.__top < 0:
#             raise MyStack.Empty()
#         ret = self.__data[self.__top]
#         self.__top -= 1
#         return ret

#     def __len__(self) -> int:
#         return self.__top + 1

#     def empty(self) -> bool:
#         return self.__top < 0

#     def top(self) -> int:
#         """top 변수를 출력"""
#         if self.empty():
#             raise MyStack.Empty()
#         return self.__data[self.__top]


g_stack = [-1 for _ in range(10_001)]
g_top = 0


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        args = input().split()
        match args[0]:
            case "push":
                g_stack[g_top] = int(args[1])
                g_top += 1
            case "pop":
                if g_top <= 0:
                    print(-1)
                else:
                    print(g_stack[g_top - 1])
                    g_top -= 1
            case "size":
                print(g_top)
            case "empty":
                if g_top <= 0:
                    print(1)
                else:
                    print(0)
            case "top":
                if g_top <= 0:
                    print(-1)
                else:
                    print(g_stack[g_top - 1])
