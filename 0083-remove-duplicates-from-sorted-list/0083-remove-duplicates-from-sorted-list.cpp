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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* node=head;
        if (head==NULL ){
            return head;
        }
        while(head!=NULL && head->next!=NULL){
           
            ListNode* nextNode=head->next;
            if (nextNode->val == head->val){
                 ListNode* temp=NULL;
                 temp=nextNode->next;
                 head->next=temp;
                 nextNode->next=NULL;
            }else{
            head=head->next;
            }
        }
        return node;
    }
};