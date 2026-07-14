# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by 
# continuously following the next pointer. Internally, pos is used to denote the index of the node 
# that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.linklist import LinkList

class Solution:

    def detect_cycle(self, head):
        slow = head
        fast = head.next

        while fast is not None:
            if id(fast) == id(slow):
                return True
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next

        return False


head = [3,2,0,-4]
pos = 1

list = LinkList()
list.makeListFromArr(head)
list.create_cycle(pos=pos)

sol_obj = Solution()
print(sol_obj.detect_cycle(list.head))

