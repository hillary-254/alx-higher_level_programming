#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slowPtr = *head, *fastPtr = *head, *prev = NULL, *next;
	listint_t *secondPart;
	int isPalindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (isPalindrome);
	while (fastPtr != NULL && fastPtr->next != NULL)
	{
		fastPtr = fastPtr->next->next;
		prev = slowPtr;
		slowPtr = slowPtr->next;
	}
	if (fastPtr != NULL)
		secondPart = slowPtr->next;
	else
		secondPart = slowPtr;
	prev->next = NULL;
	prev = NULL;
	while (secondPart != NULL)
	{
		next = secondPart->next;
		secondPart->next = prev;
		prev = secondPart;
		secondPart = next;
	}
	while (*head != NULL && prev != NULL)
	{
		if ((*head)->n != prev->n)
		{
			isPalindrome = 0;
			break;
		}
		*head = (*head)->next;
		prev = prev->next;
	}
	prev = NULL;
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;

	return (isPalindrome);
}
