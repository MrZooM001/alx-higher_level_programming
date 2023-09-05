#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it.
 * @list: pointer to a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *nxt_lst;
	listint_t *prev_lst;

	nxt_lst = list;
	prev_lst = list;

	while (list && nxt_lst && prev_lst)
	{
		if (prev_lst->next == NULL)
		{
			return (0);
		}
		else
		{
			nxt_lst = nxt_lst->next;
			prev_lst = prev_lst->next->next;

			if (nxt_lst == prev_lst)
			{
				return (1);
			}
		}
	}

	return (0);
}
