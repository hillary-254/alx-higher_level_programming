#include "lists.h"

/**
  * insert_node - adds a number to a sorted singly linked list
  * @head: The head of singly linked list
  * @number: value inserted in the singly linked list
  * Return: The singly linked list with the new number added
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = NULL, *newNode = NULL, *tmp = NULL;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	if (*head)
	{
		curr = *head;
		if (number <= curr->n)
		{
			newNode->next = curr;
			*head = newNode;
		}
		else
		{
			while (curr->next)
			{
				if (number <= curr->next->n)
				{
					tmp = curr->next;
					curr->next = newNode;
					newNode->next = tmp;
					return (*head);
				}

				curr = curr->next;
			}
			tmp = curr->next;
			curr->next = newNode;
			newNode->next = tmp;
		}
		return (*head);
	}
	else
	{
		newNode->next = NULL;
		*head = newNode;
		return (*head);
	}
}
