def backtrack(path):
    i = 0
    if len(path) >= 3:
        print(path)

    for num in [1, 2, 3]:
        if num not in path:
            path.append(num)  # choose
            backtrack(path)  # explore
            path.pop()  # undo


if __name__ == "__main__":
    # Start with an empty path
    backtrack([])
