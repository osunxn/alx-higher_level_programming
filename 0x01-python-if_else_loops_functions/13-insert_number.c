#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

	    if (head == NULL)
    {
        printf("Error: head is NULL\n");
        return (NULL);
    }

    new = malloc(sizeof(listint_t));
    if (new == NULL)
	{
        printf("Error: malloc failed\n");
        return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number <= (*head)->next->n)
	{
		new->next = *head;
		*head = new;
		return(new);
	}

	current = *head;
	while (current && current->next != NULL && current->next->n < number) 
		current = current->next;

	new->next = current->next;
	current->next = new;

	return(new);

}
