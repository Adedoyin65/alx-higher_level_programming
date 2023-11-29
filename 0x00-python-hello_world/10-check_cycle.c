#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - A function in C that checks if a singly linked list has a cycle in it.
 * @list: A pointer.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *dan;
	
	dan = list->next;
	while (dan)
	{
		if (dan == list)
		{
			break;
		}
		dan = dan->next;
	}
	if (dan == NULL)
	{
		return (0);
	}
	return (1);

}
