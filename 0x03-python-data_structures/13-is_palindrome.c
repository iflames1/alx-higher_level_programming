#include "lists.h"

listint_t split_list(listint_t *fast, listint_t *slow)
{
	listint_t *start_1, *start_2;

	if (fast->next == NULL)
	{
		start_2 = slow->next->next;
		return (*start_2);
	}
	if (fast == NULL)
	{
		start_2 = slow->next;
		return (*start_2);
	}
	split_list(fast->next->next, slow->next);
}

listint_t *reverse(listint_t *head)
{
	/* listint_t *prev = NULL, *current = head, *next = NULL; */
	listint_t *p, *q;

	if (head == NULL || head->next == NULL)
		return;

	p = head;
	q = p->next;

	if (q == NULL)
		return;

	p->next = NULL;
	q = reverse(q);
	p->next->next = p;

	return (q);
}

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *start_2;

	*start_2 = split_list(fast, slow);
	start_2 = reverse(start_2);

	while (start_2->next != NULL)
	{
		if (start_2 != *head)
		{
			return (0);
		}
	}

	return (1);
}
