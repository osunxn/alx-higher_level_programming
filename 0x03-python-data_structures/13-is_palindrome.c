#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *stack = NULL;
    
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        /* push the value of slow into the stack */
        stack = add_nodeint_end(&stack, slow->n);
        slow = slow->next;
    }

    /* If the linked list is odd, ignore the middle element */
    if (fast != NULL)
        slow = slow->next;

    while (slow != NULL)
    {
        if (stack == NULL || slow->n != stack->n)
            return 0;
        stack = stack->next;
        slow = slow->next;
    }
    return 1;
}
