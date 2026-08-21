class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices =[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             indices.append(i+1)
        #             indices.append(j+1)
        # return indices
        left=sum=0
        right = len(numbers)-1
        while(left<right):
            sum = numbers[left]+numbers[right]
            if sum==target:
                break
            elif sum<target:
                left+=1
            else:
                right-=1
        
        indices.append(left+1)
        indices.append(right+1)
        return indices

        