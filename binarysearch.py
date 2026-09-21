class Solution:
    def search(self,arr,target):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if target==arr[mid]:
                return mid
            elif target<arr[mid]:
                r=mid-1
            else:
                 l=mid+1
        return-1

        
