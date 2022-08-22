#include "lists.h"

/**
 * check_cycle - check if a linked list contain a cycle
 * @list: linked list to check
 *
 * Return: 1 if the link has a cycle
 * Otherwise: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	if (!list)
	{
		return (0);
	}
	while (slower && faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
		if (slower == faster)
		{
			return (1);
		}
	}
	return (0);
}
