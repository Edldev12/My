/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(x) : val(x), next(nullptr) {}
 *     ListNode(x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <vector>
#include <unordered_set>

class Solution {
public:
    int numComponents(ListNode* head, std::vector<int>& nums) {
        // Store vector elements in a hash set for O(1) lookups
        std::unordered_set<int> num_set(nums.begin(), nums.end());
        int components = 0;
        ListNode* current = head;
        
        while (current != nullptr) {
            // Check if current node is in nums, and it is the end of a contiguous segment
            if (num_set.count(current->val) && 
               (current->next == nullptr || !num_set.count(current->next->val))) {
                components++;
            }
            current = current->next;
        }
        
        return components;
    }
};
