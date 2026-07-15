# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

 

# Example 1:


# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
# Example 2:

# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
 

# Constraints:

# The number of the nodes in the given list is in the range [1, 105].
# 1 <= Node.val <= 105

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.linklist import LinkList

class Solution:

    def remove_nodes(self, head):
        if head is None:
            return head
        stack = []
        temp = head

        while temp is not None:
            while len(stack) and temp.val > stack[-1].val:
                stack.pop()
            
            stack.append(temp)
            temp = temp.next

        next = None
        for i in range(len(stack) -1, -1, -1):
            node = stack[i]
            node.next = next
            next = node

        return next


head = [5,2,13,3,8]
head = [1,1,1,1]
head = [1,2,3,4,5]
sol_obj = Solution()

list = LinkList()
list.makeListFromArr(head)
new_head = sol_obj.remove_nodes(list.head)

new_list = LinkList(new_head)
new_list.printlist()