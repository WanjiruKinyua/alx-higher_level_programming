#include "lists.h"

/**
 * check_cycle - Entry point
 * Description: checks if a singly linked list has a cycle in it
 * @list: pointer to head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *k = list;
	listint_t *p = list;

	while (p != NULL && p->next != NULL)
	{
		k = k->next;
		p = p->next->next;

		if (k == p)
			return (1);
	}

	return (0);
}
