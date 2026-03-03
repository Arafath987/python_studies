# arr = [5, -1, -1, -1, 10]
# k = 3
# prefix = [0] * (len(arr))
# prefix[0] = arr[0]

# for i in range(0, len(arr) - 1):
#     prefix[i + 1] = prefix[i] + arr[i + 1]
# max_sum = prefix[k - 1]
# for i in range(0, len(arr) - k):
#     window_sum = prefix[i + k] - prefix[i]
#     max_sum = max(max_sum, window_sum)

# print("max sum =", max_sum)


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

window_sum = sum(arr[0:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(window_sum, max_sum)
print(max_sum)


# arr = [3, 1, 2, 4, 5]
# k = 3

# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum += arr[i] - arr[i - k]
#     max_sum = max(window_sum, max_sum)

# print(max_sum)
