#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function reverses a singly-linked listint_t list
 * @head: points to starting node of the list to reverse.
 *
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nde = *head, *nextNde, *before = NULL;

	while (nde)
	{
		nextNde = nde->next;
		nde->next = before;
		before = nde;
		nde = nextNde;
	}

	*head = before;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: points to the head of the linked list
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *revrse, *midle;
	size_t sze = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		sze++;
		temp = temp->next;
	}

	temp = *head;
	for (x = 0; x < (sze / 2) - 1; x++)
		temp = temp->next;

	if ((sze % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	revrse = reverse_listint(&temp);
	midle = revrse;

	temp = *head;
	while (revrse)
	{
		if (temp->n != revrse->n)
			return (0);
		temp = temp->next;
		revrse = revrse->next;
	}
	reverse_listint(&midle);

	return (1);
}
