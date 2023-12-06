#include "lists.h"
#include <stdio.h>

/**
 * split_list - slipt a linked list
 * @fast: fast pointer
 * @slow: slow poiter
 * Return: pointer to the start of the second line
 */
listint_t *split_list(listint_t *fast, listint_t *slow)
{
	listint_t *start_2;

	if (fast == NULL || fast->next == NULL)
	{
		start_2 = slow->next;
		slow->next = NULL;
		return (start_2);
	}

	return (split_list(fast->next->next, slow->next));
}

/**
 * reverse - reverse a linked list
 * @head: pointer to the hea
 * Return: reverse linked list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head node
 * Return: 0 if its not a palindrome and 1 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *start_2 = NULL;

	if (*head == NULL)
		return (1);

	start_2 = split_list(fast, slow);
	start_2 = reverse(start_2);


	while (start_2 != NULL && *head != NULL)
	{
		if (start_2->n != (*head)->n)
		{
			return (0);
		}
		start_2 = start_2->next;
		*head = (*head)->next;
	}

	return (1);
}
