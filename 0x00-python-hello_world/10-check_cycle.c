#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it.* @list: list
 * Return: 0 if there is no cycle, 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	while(hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;

		if (hare == tortoise)
		{
			return (1);
		}
	}

	return (0);
}
