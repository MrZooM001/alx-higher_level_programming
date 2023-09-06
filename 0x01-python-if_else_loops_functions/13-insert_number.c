#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to listint_t struct
 * @number: an integer
 *
 * Return: the address of the new node,
 * or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current_node, *previous_node;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}
new_node->n = number;
new_node->next = NULL;
if (*head == NULL || number <= (*head)->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}
previous_node = NULL;
current_node = *head;
while (current_node != NULL && current_node->n < number)
{
previous_node = current_node;
current_node = current_node->next;
}
previous_node->next = new_node;
new_node->next = current_node;

return (new_node);
}
