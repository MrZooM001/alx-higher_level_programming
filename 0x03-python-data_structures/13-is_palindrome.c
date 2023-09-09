#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * reverse_list - reverse a singly linked list
 * @head: pointer to head of list
 *
 * Return: reversed list
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *previous_node, *current_node, *next_node;

previous_node = NULL;
current_node = head;
next_node = NULL;
while (current_node != NULL)
{
next_node = current_node->next;
current_node->next = previous_node;
previous_node = current_node;
current_node = next_node;
}
return (previous_node);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *start, *end, *middle, *previous_start, *first_half, *second_half;
int is_palindrome;

start = *head, end = *head;
previous_start = NULL, middle = NULL;
is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (1);
while (end != NULL && end->next != NULL)
{
end = end->next->next;
previous_start = start;
start = start->next;
}
if (end != NULL)
{
middle = start;
start = start->next;
}
second_half = reverse_list(start);
first_half = *head;
while (second_half != NULL)
{
if (first_half->n != second_half->n)
{
is_palindrome = 0;
break;
}
first_half = first_half->next;
second_half = second_half->next;
}
reverse_list(second_half);
if (middle != NULL)
{
previous_start->next = middle;
middle->next = second_half;
}
else
previous_start->next = second_half;
return (is_palindrome);
}
