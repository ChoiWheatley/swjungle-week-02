"""
히스토그램에서 가장 큰 직사각형

stack을 써서 cur보다 큰 직사각형들을 pop한다. pop 하면서 길어지는 제거길이를 가로길이로, 높이를 가로범위 중 최솟값으로 설정하여 해당 범위 안의 넓이들을 구할 수 있다.
"""

from sys import stdin


def solve(hist: list[int]) -> int:
    """히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 리턴"""
    hist += [0]  # 가상의 0을 넣어 최우측 평가를 건너뛰는 일을 방지
    stack = [0]
    maxarea = hist[0]
    for i in range(1, len(hist)):
        cur = hist[i]
        while stack and hist[stack[-1]] > cur:
            # 현재 막대기보다 큰 모든 막대기를 pop한다.
            # 연속적으로 pop 수행시, 가장 최근에 pop한 막대기를 기준으로
            # 높이와 너비를 결정한다.
            p_idx = stack.pop()
            top = hist[p_idx]
            left = stack[-1] if stack else -1
            area = top * (i - left - 1)
            maxarea = max(maxarea, area)

            if top < cur:
                stack.append(p_idx)
                break
        stack.append(i)

    return maxarea


if __name__ == "__main__":
    for line in stdin:
        if line.strip() == "0":
            exit(0)
        hist = [int(x) for x in line.split()][1:]
        print(solve(hist))
