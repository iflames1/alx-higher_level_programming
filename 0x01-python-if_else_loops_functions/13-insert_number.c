#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts a number into
 *	a sorted singly linked list.
 * @head: head
 * @number: number
 * Return: new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	current = *head;

	if ((*head)->n > number || *head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
