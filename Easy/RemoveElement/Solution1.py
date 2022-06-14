class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        idx = 0
        while idx < len(nums) :
            item = nums[idx]
            print(idx, item)
            if item == val :
                print('Array before deletion : {}'.format(nums))
                del nums[idx]
                print('Array after deletion : {}'.format(nums))
                nums.append('_')
                print('Array after updation : {}'.format(nums))
                idx -= 1
            elif item != val and item != '_' :
                print('Nothing to change')
                count += 1
            idx += 1
        print(count, nums)
        return count
