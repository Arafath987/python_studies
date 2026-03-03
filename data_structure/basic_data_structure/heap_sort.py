# class person:
#     name: str
#     age: int

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# data = {"name": "yaser", "age": "yaser"}
# my_person = person(**data)
# print(
#     f"my person = {my_person.name}\n{person(**data).name}\nperson age:{my_person.age}"
# )


# class Solution:
#     def rob(self, nums):
#         if len(nums) == 1:
#             return nums[0]
#         dp = [nums[0], max(nums[0], nums[1])]
#         for i in range(2, len(nums)):
#             dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
#         return dp


# # Example test
# nums = [1, 2, 3, 4]
# print(nums[0:], "\n", nums[:-1])  # Expected: 12

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1 + amount] * (1 + amount)
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - c])

        return -1 if dp[amount] == (1 + amount) else dp[amount]


# Test your first version
s = Solution()
print(s.coinChange([5, 2, 1], 11))  # Expect 3
print(s.coinChange([2], 3))  # Expect -1
print(s.coinChange([1], 0))
