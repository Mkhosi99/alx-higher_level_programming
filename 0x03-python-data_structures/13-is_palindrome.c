#include "lists.h"
#include <string.h>
#include <stdlib.h>

/**
 * is_palindrome - function checks if a list is a palindrome
 * @head: points to head of the list
 * Return: 0 if list not a palindrome 1 if True
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int ndes = 0, x = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		ndes++;
		temp = temp->next;
	}
	arr = malloc(sizeof(int) * ndes);
	temp = *head;
	while (temp)
	{
		arr[x++] = temp->n;
		temp = temp->next;
	}
	for (x = 0; x < ndes / 2; x++)
	{
		if (arr[x] != arr[ndes - 1 - x])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
