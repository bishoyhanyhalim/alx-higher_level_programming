#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - this is a new function
 * @list: very important list
 *
 * Return: return the value of code
 */

int check_cycle(listint_t *list)
{
	listint_t *good_sl, *goods_fa;

	if (!list)
	{
		return (0);
	}

	good_sl = list;
	goods_fa = list->next;

	while (goods_fa && good_sl && goods_fa->next)
	{

		if (good_sl == goods_fa)
		{
			return (1);
		}

		good_sl = good_sl->next;

		goods_fa = goods_fa->next->next;

	}

	return (0);
}
