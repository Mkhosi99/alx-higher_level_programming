#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts node in a linked list
 * @head: double pointer to the head of the linked list
 * number: info for the new node
 * Return: pointer to new node ,NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nde = *head, *newNde;

	newNde = malloc(sizeof(listint_t));
	if (newNde == NULL)
		return (NULL);
	newNde->n = number;

	if (nde == NULL || nde->n >= number)
	{
		newNde->next = nde;
		*head = newNde;
		return (newNde);
	}

	while (nde && nde->next && nde->next->n < number)
		nde = nde->next;

	newNde->next = nde->next;
	nde->next = newNde;

	return (newNde);
}
