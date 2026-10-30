def search(nums, target):
    def boundary(find_first):
        left, right = 1, len(nums) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                answer = mid

                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return answer
    return [
        boundary(True),
        boundary(False)
    ]


print(search([2,3,4,5,5,6,7,8],6))