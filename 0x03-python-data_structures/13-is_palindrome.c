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
listint_t *start, *end, *middle, *previous_start, *frst_half, *scnd_half, *tmp;
int is_palindrome;

start = *head, end = *head;
previous_start = NULL, middle = NULL;
frst_half = *head, is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (1);

while (end != NULL && end->next != NULL)
{
end = end->next->next;
tmp = start->next;
start->next = previous_start;
previous_start = start, start = tmp;
}
if (end != NULL)
middle = start, start = start->next;
scnd_half = start, frst_half = previous_start;
while (scnd_half != NULL)
{
if (frst_half->n != scnd_half->n)
{
is_palindrome = 0;
break;
}
frst_half = frst_half->next, scnd_half = scnd_half->next;
}
previous_start = NULL;
while (frst_half != NULL)
{
tmp = frst_half->next;
frst_half->next = previous_start;
previous_start = frst_half, frst_half = tmp;
}
if (middle != NULL)
{
previous_start = middle, middle->next = scnd_half;
}
return (is_palindrome);
}
