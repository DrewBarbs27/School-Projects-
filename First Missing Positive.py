def first_missing_positive(nums):
    n = len(nums)

    # Perform cyclic sort
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

# Example usage:
nums = [3, 4, -1, 1]
result = first_missing_positive(nums)
print(result)  # Output: 2
