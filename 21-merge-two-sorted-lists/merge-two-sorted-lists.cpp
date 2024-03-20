/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr && list2 == nullptr)
        {
            return nullptr;
        }
        else if(list1==nullptr)
        {
            return list2;
        }
        else if(list2==nullptr)
        {
            return list1;
        }

        if(list1->val <= list2->val)
        {
            ListNode* temp = list1;
            ListNode* temp2 = list2->next;
            ListNode* temp3;
            if(temp->next==nullptr)
            {
                temp->next = list2;
                return list1;
            }
            while(temp->next->val < list2->val)
            {
                temp = temp->next;
                if(temp->next==nullptr)
                {
                    temp->next = list2;
                    return list1;
                }
            } 
            temp3 = temp->next;
            temp->next = list2;
            list2->next = mergeTwoLists(temp3,temp2);
            return list1;

        }
        else
        {
           ListNode* temp = list2;
            ListNode* temp2 = list1->next;
            ListNode* temp3;
            if(temp->next==nullptr)
            {
                temp->next = list1;
                return list2;
            }
            while(temp->next->val < list1->val)
            {
                temp = temp->next;
                if(temp->next==nullptr)
                {
                    temp->next = list1;
                    return list2;
                }
            } 
            temp3 = temp->next;
            temp->next = list1;
            list1->next = mergeTwoLists(temp3,temp2);
            return list2; 
        }

    }
};

