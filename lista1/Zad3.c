#include <stdio.h>
#include <stdlib.h>
#include <time.h>




typedef struct List_element
{
  int data;
  struct List_element *next;
  struct List_element *previous;

} List_element;


void add_element(int element, List_element *list, int *size);
void rem_element(int index, List_element *list, int *size);
void get_element_by_id(int index, List_element *list, int *size);
int get_value_by_index(int index, List_element *list, int *size);
void *merge(List_element *first_list, List_element *second_list, int *size_1, int *size_2);
void print_list(List_element *list);
List_element *create_list();


List_element *create_list()
{
  List_element *head;
  head = (List_element *)malloc(sizeof(List_element));
  head->data = 0;
  head->next = NULL;
  head->previous = NULL;

  return head;
}

void add_element(int var, List_element *list, int *size)
{
  //kiedy dodajemy pierwszy element
  if(list->next == NULL)
  {
    list->data = var;
    list->next = list;
    list->previous = list;
    *size += 1;

  }
  else
  {
    List_element *current = list;
    while(current->next != list)
    {
      current = current->next;
    }

    List_element *new_element = (List_element *)malloc(sizeof(List_element));
    new_element->data = var;
    new_element->next = list;
    new_element->previous = current;

    current->next = new_element;
    list->previous = new_element;
    *size += 1;

  }

}

void rem_element(int index, List_element *list, int *size)
{
  if(index < 0 || index > *size - 1)
  {
    printf("Nie ma takiego indeksu! \n");
  }
  else if(index == 0 && *size == 1)
  {
    printf("To usunie liste! \n");
  }
  else if(index == 0 && *size > 1)
  {
    List_element *current = list->next;
    list->data = current->data;
    list->next = current->next;

    free(current);
    *size -= 1;

  }

  //druga polowa zbioru
  else if(index > *size/2)
  {
    List_element *current = list;
    List_element* next = list;
    for(int i = (*size-1); i >= index; i--)
    {
      next = current;
      current = current->previous;
    }

    next->previous = current->previous;
    current->previous->next = next;

    free(current);
    *size -= 1;


  }
  else
  {

    List_element *current = list;
    List_element* previous = list;
    for(int i = 1; i <= index; i++)
    {
      previous = current;
      current = current->next;
    }

    previous->next = current->next;
    current->previous = previous;

    free(current);
    *size -= 1;
  }
}



int get_value_by_index(int index, List_element *list, int *size)
{

  if(index >= *size || index < 0)
  {
    printf("Indeks %d nie istnieje!\n", index);
    return -2137;

  }

  else if(index > *size/2)
  {
    List_element *current = list;
    for(int i = (*size-1); i >= index; i--)
    {
      current = current->previous;
    }

    return current->data;
  }

  else
  {
    List_element *current = list;
    for(int i = 0; i < index; i++)
    {
      current = current->next;
    }

    return current->data;
  }

}

/*
  wynik zapisywany w obu listach
*/
void *merge(List_element *first_list, List_element *second_list, int *size_1, int *size_2)
{

  List_element *last_first = first_list->previous;
  List_element *last_second = second_list->previous;
  last_first->next = second_list;
  last_second->next = first_list;
  (*size_1) += (*size_2);
  (*size_2) = (*size_1);


}

void print_list(List_element *list)
{
  List_element *current = list;
  do
  {
    printf("%d ",current->data);
    current = current->next;
  } while(current != list);

  printf("\n");
}


int main()
{
  int size = 0;
  List_element *first = create_list();

   for(int i = 0; i < 10; i++)
   {
     add_element((rand() % 1000), first, &size);

   }



  clock_t my_clock;
  double time_taken = 0.0;


  my_clock = clock();

  for(int i = 0; i < 1000; i++)
  {
    add_element((rand() % 1000), first, &size);

  }

  my_clock = clock() - my_clock;
  time_taken = ((double)my_clock)/CLOCKS_PER_SEC;
  printf("Dodano 1000 elementow w czasie: %f sek\n",time_taken);

  my_clock = clock();

  for(int i = 0; i < 40000; i++)
  {
    get_value_by_index(999, first, &size);

  }
  my_clock = clock() - my_clock;
  time_taken = 1000000/40000*((double)my_clock)/CLOCKS_PER_SEC;
  printf("Sredni czas dostepu procesora do elemenu 999 to: %f mikrosek\n",time_taken);

  my_clock = clock();
  for(int i = 0; i < 40000; i++)
  {
    get_value_by_index(rand() % 1000, first, &size);

  }
  my_clock = clock() - my_clock;
  time_taken = 1000000/40000*((double)my_clock)/CLOCKS_PER_SEC;

  printf("Sredni czas dostepu procesora do losowego elemenu to: %f mikrosek\n",time_taken);

  return 0;
}
