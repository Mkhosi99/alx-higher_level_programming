#include "lists.h"

/**
 * check_cycle - function will check if a linked list contains acycle
 * @list: linked list that will be checked
 * Return: 1 if the list contains a cycle and 0 if failure
 */
int check_cycle(listint_t *list)
{
	listint_t *lag = list;
	listint_t *quick = list;

	if (!list)
		return (0);

	while (lag && quick && quick->next)
	{
		lag = lag->next;
		quick = quick->next->next;
		if (lag == quick)
			return (1);
	}

	return (0);
}
