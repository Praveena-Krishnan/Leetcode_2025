/**
 * LeetCode Problem 24: Swap Nodes in Pairs
 *
 * Problem Description:
 * Given a linked list, swap every two adjacent nodes and return its head.
 * You must solve the problem without modifying the values in the list's nodes
 * (i.e., only nodes themselves may be changed).
 *
 * Example 1:
 * Input: head = [1,2,3,4]
 * Output: [2,1,4,3]
 *
 * Example 2:
 * Input: head = []
 * Output: []
 *
 * Example 3:
 * Input: head = [1]
 * Output: [1]
 *
 * Constraints:
 * - The number of nodes in the list is in the range [0, 100].
 * - 0 <= Node.val <= 100
 */
 /**
 /*Definition for singly-linked list.*/
 struct ListNode {
     int val;
     struct ListNode *next;
  };
 
struct ListNode* swapPairs(struct ListNode* head) {
    if(!head || !head->next) return head; //If there are less than 2 nodes in the given nodes, then no need to do anything just return the list as it is.
		
        struct ListNode dummyNode;
        
        struct ListNode* prevNode = &dummyNode;
        struct ListNode* currNode = head;
        
        while(currNode && currNode->next){
            prevNode->next = currNode->next;
            currNode->next = prevNode->next->next;
            prevNode->next->next = currNode;
            
            prevNode = currNode;
            currNode = currNode->next;
        }
        
        return dummyNode.next;
    }


    
