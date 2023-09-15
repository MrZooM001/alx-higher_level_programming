#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

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
first_half = *head, is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (1);

while (end != NULL && end->next != NULL)
{
end = end->next->next;
listint_t *temp = start->next;
start->next = previous_start;
previous_start = start;
start = temp;
}
if (end != NULL)
{
middle = start;
start = start->next;
}
second_half = start;
first_half = previous_start;
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
previous_start = NULL;
while (first_half != NULL)
{
listint_t *temp = first_half->next;
first_half->next = previous_start;
previous_start = first_half;
first_half = temp;
}
if (middle != NULL)
{
previous_start = middle;
middle->next = second_half;
}

return (is_palindrome);
}
