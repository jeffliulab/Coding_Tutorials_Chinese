##################################################################
########### 第一部分 Array / String 共24道题 ######################
##################################################################

#####################################################################
# (1) 88. Merge Sorted Array 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """

        # 初始化三个指针
        p1 = m - 1             # 指向 nums1 中最后一个有效元素
        p2 = n - 1             # 指向 nums2 中最后一个元素
        end = m + n - 1        # 指向 nums1 的最后一个位置（合并的尾部）

        # 从后往前进行合并，只要 nums2 还有元素就继续
        while p2 >= 0:
            # 情况一：nums1 还有值，并且当前 nums1 的值更大
            if p1 >= 0 and nums1[p1] > nums2[p2]: # 这里用p1 >=0 是因为当p1 < 0的时候直接比较会导致错误，需要做的其实就是继续把nums2得数组放进来
                nums1[end] = nums1[p1]  # 把较大值放在 nums1 的末尾
                p1 -= 1                # 移动指针
            else:
                # 情况二：nums2 的值更大，或 nums1 已用完（p1 < 0）
                nums1[end] = nums2[p2]  # 拷贝 nums2 的当前值
                p2 -= 1                # 移动指针
            end -= 1                   # 每次都要填一个位置，end 向前移动

        # 注意：当 p2 < 0 时，说明 nums2 合并完了，循环会自动停止
        # 若 p1 剩下还没合并的元素，它们本来就在 nums1 前面，位置已经对了，不需要动

#####################################################################
# (2) 27. Remove Element
"""
注意: 这道题不关心最后剩下的部分, 所以不用考虑最后再设置空值
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # 指向写入新数组的位置

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # 不需要强行写0，因为题目说后面部分不关心
        return k  # 返回新数组的长度


#####################################################################
# (3) 26. Remove Duplicates from Sorted Array

"""
和上道题一样，最后剩下的不重要。
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1  # 第一个元素一定是唯一的，从第二个位置开始写
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

#####################################################################
# (4) 80. Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        """
        删除有序数组中的重复项 II: 保留最多出现两次的元素
        
        算法思路：
        - 使用双指针技巧，一个指针(i)遍历原数组，另一个指针(k)维护新数组
        - 通过巧妙的条件判断，无需额外计数器即可限制每个元素最多出现两次
        
        时间复杂度: O(n) - 只需遍历一次数组
        空间复杂度: O(1) - 原地修改，不使用额外空间
        
        :type nums: List[int] - 输入的有序数组
        :rtype: int - 返回新数组的长度
        """
        # 如果数组为空，直接返回0
        if not nums:
            return 0
            
        # k是新数组的指针，指向下一个要填入的位置
        # 初始值为1是因为第一个元素必然保留（位置0）
        k = 1
        
        # 从位置1开始遍历原数组
        for i in range(1, len(nums)):
            # 判断当前元素是否应该保留：
            # 1. 当k=1时，第二个元素总是可以保留（任何元素至少可以出现一次）
            # 2. 或者当前元素与新数组中倒数第二个元素不同
            #    (这保证了相同元素最多只会出现两次)
            if k == 1 or nums[i] != nums[k-2]:
                # 将当前元素复制到新数组的位置k
                nums[k] = nums[i]
                # 新数组指针前进
                k += 1
                
        # 返回新数组的长度
        return k
    
#####################################################################
# (5) 169. Majority Element1

def majorityElement(nums):
    """
    查找数组中的多数元素（出现次数超过 ⌊n/2⌋ 的元素）
    
    参数:
        nums: 整数数组
    返回:
        多数元素
    
    算法: 摩尔投票算法 (Boyer-Moore Voting Algorithm)
    时间复杂度: O(n) - 只需要遍历数组一次
    空间复杂度: O(1) - 只使用了常数额外空间
    """
    
    # 候选元素
    candidate = None
    # 计数器
    count = 0
    
    # 第一遍遍历: 找到可能的多数元素
    for num in nums:
        # 如果计数器为0，选择当前元素作为新的候选元素
        if count == 0:
            candidate = num
            count = 1
        # 如果当前元素等于候选元素，计数器加1
        elif candidate == num:
            count += 1
        # 如果当前元素不等于候选元素，计数器减1
        else:
            count -= 1
    
    """
    核心思想解释:
    
    1. 摩尔投票算法基于"抵消"的概念
    2. 把每个元素看作+1或-1票:
       - 如果元素等于候选元素，则投+1票
       - 如果元素不等于候选元素，则投-1票
    3. 当计数器为0时，之前的抵消已完成，选择一个新的候选元素
    4. 由于多数元素出现次数 > ⌊n/2⌋，所以它的"票数"一定会比其他所有元素的"票数"总和还多
    5. 最终留下的候选元素必然是多数元素
    
    形象理解:
    - 想象不同元素代表不同阵营的士兵
    - 不同阵营的士兵两两厮杀(抵消)
    - 由于多数元素的"士兵"数量超过总数的一半
    - 因此战斗结束后，战场上剩下的必然是多数元素的士兵
    """
    
    # 因为题目保证多数元素一定存在，所以直接返回候选元素
    # 如果题目不保证多数元素存在，还需要进行第二遍遍历来确认candidate确实出现超过⌊n/2⌋次
    return candidate

#####################################################################
# (6) 189. Rotate Array

def rotate(nums, k):
    """
    旋转数组: 将数组中的元素向右移动k个位置.
    
    使用三次翻转法实现:
    1. 先将整个数组翻转
    2. 再将前k个元素翻转
    3. 最后将剩余元素翻转
    
    例如: 对于数组[1,2,3,4,5,6,7], k=3:
    - 整体翻转后: [7,6,5,4,3,2,1]
    - 前k=3个元素翻转后: [5,6,7,4,3,2,1]
    - 剩余元素翻转后: [5,6,7,1,2,3,4]
    
    时间复杂度: O(n) - 其中n是数组的长度
                    - 我们最多遍历数组3次
    空间复杂度: O(1) - 只使用常数额外空间
                    - 只需要几个临时变量
    
    参数:
        nums: List[int] - 需要旋转的整数数组
        k: int - 向右旋转的步数, 非负整数
    
    返回:
        List[int] - 旋转后的数组
    """
    n = len(nums)
    k %= n  # 处理k大于数组长度的情况, 因为旋转n次等于没旋转
    
    if k == 0:  # 如果k是n的倍数, 等于不旋转, 直接返回
        return nums
    
    # 辅助函数: 翻转数组的指定部分
    def reverse(arr, start, end):
        """
        翻转数组中从start到end的元素
        
        参数:
            arr: List[int] - 要操作的数组
            start: int - 起始索引(包含)
            end: int - 结束索引(包含)
        """
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]  # 交换元素
            start += 1
            end -= 1
    
    # 三次翻转法
    reverse(nums, 0, n-1)    # 步骤1: 翻转整个数组
    reverse(nums, 0, k-1)    # 步骤2: 翻转前k个元素
    reverse(nums, k, n-1)    # 步骤3: 翻转剩余元素
    
    return nums

#####################################################################
# (7) 121. Best Time to Buy and Sell Stock