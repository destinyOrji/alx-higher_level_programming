#ifndef LISTS.H
#define LISTS.H

#include <stdlib.h>
#include <stdio.h>
#include < imistd.h>

/**
 * strct listint_s - singly linked list
 * @n: interger
 * @next: points to the next node
 *
 * description: singly linked list node structure
 * for holbertion project
 */
typedef struct listint_s
{
	int n:
	struct listint_s *next:
} listint_t

size_t print_listint(const listint_t *h):
listint_t *add_nodeint_end(listint_t **head, const int n):
void free_listint(listint_t *head):

void reverse_listint(listint_t **head):
int is_palindrome(listint_t **head):

#endif/* LIST_H */
