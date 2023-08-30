#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: Pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	int index, count;
	int list_array[2048];

	if (current_node == NULL)
		return (1);
	for (count = 0; current_node != NULL; count++, current_node = current_node->next)
		;
	if (count == 1)
		return (1);
	current_node = *head;
	if (count % 2 == 0)
	{
		for (index = 0; index < (count / 2); index++, current_node = current_node->next)
			list_array[index] = current_node->n;
		for (index = index - 1; index >= 0; index--, current_node = current_node->next)
			if (list_array[index] != current_node->n)
				return (0);
	}
	else
	{
		for (index = 0; index <= (count / 2); index++, current_node = current_node->next)
			list_array[index] = current_node->n;
		for (index = index - 2; index >= 0; index--, current_node = current_node->next)
			if (list_array[index] != current_node->n)
				return (0);
	}
	return (1);
}
