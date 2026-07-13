# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.linklist import LinkList

class Solution:
    def remove_duplicates(self, head):
        if head is None:
            return []
        prev = None
        temp = head

        while temp is not None:
            if prev is not None and prev.val == temp.val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next

        return head

head = [1,1,2,3,3]
head = [1,2,2]
head = [1,2,2,3,3,3,4,4,4,4,5,6,7,7]

list = LinkList()
list.makeListFromArr(head)

sol_obj = Solution()
new_head = sol_obj.remove_duplicates(list.head)

new_list = LinkList(new_head)
new_list.printlist()

