#include <stdio.h>
#include <stdlib.h>
#include <time.h>


typedef struct List_element
{
  int data;
  struct List_element *next;

} List_element;


void add_element(float var, List_element *head);
void set_head(List_element *head);
void print_list(List_element *list);
void remove_by_index(int index, List_element *list);
int get_value_by_index(int index, List_element *list);
void *merge(List_element *first_list, List_element *second_list);
List_element *create_new_list();




List_element *create_new_list()
{
  List_element *element;
  element = (List_element *)malloc(sizeof(List_element));
  element->next = NULL;
  element->data = 0;

  return element;
}

void add_element(float var, List_element *list)
{
  //przypadek kiedy dodajemy pierwszy element
  if(list->next == NULL)
  {
    List_element *new_element = (List_element *) malloc(sizeof(List_element));
    new_element->next = NULL;
    new_element->data = var;

    list->next = new_element;
    list->data = 1;

  }
  else
  {
    List_element *last = list;
    //szukamy ostatniego elementu
    while(last->next != NULL)
    {
      last = last->next;
    }

    List_element *new_element = (List_element *) malloc(sizeof(List_element));
    new_element->next = NULL;
    new_element->data = var;

    last->next = new_element;
    list->data +=1;

  }

}

void print_list(List_element *list)
{
  List_element *counter = list->next;
  while(counter != NULL)
  {
    printf("%d ", counter->data);
    counter = counter->next;

  }
  printf("\n");


}

void remove_by_index(int index, List_element *list)
{
  int size = list->data;
  if(index >= size || index < 0)
    printf("Indeks %d nie istnieje!\n", index);
  else
  {
    List_element *previous = NULL;
    List_element *current = list;

    for(int i = 0; i <= index; i++)
    {
      previous = current;
      current = current->next;
    }

    previous->next = current->next;
    list->data -= 1;

    free(current);
  }
}

int get_value_by_index(int index, List_element *list)
{
  int size = list->data;
  if(index >= size || index < 0)
  {
    printf("Indeks %d nie istnieje!\n", index);
    return -2137;

  }

  else
  {
    List_element *current = list;
    //algorytm szukania elementu
    for(int i = 0; i <= index; i++)
    {
      current = current->next;
    }

    return current->data;
  }

}

/*
  Wynik zapisywany w pierwszej liscie, druga czyszczona
*/
void *merge(List_element *first_list, List_element *second_list)
{
  List_element *last = first_list;
  while(last->next != NULL)
  {
    last = last->next;

  }

  last->next = second_list->next;
  first_list->data += second_list->data;

  second_list->next = NULL;
  second_list->data = 0;

}




int main()
{

  List_element *first = create_new_list();

  clock_t my_clock;
  double time_taken = 0.0;


  my_clock = clock();

  for(int i = 0; i < 1000; i++)
  {
    add_element((rand() % 1000), first);

  }

  my_clock = clock() - my_clock;
  time_taken = ((double)my_clock)/CLOCKS_PER_SEC;
  printf("Dodano 1000 elementow w czasie: %f sek\n",time_taken);

  my_clock = clock();

  for(int i = 0; i < 40000; i++)
  {
    get_value_by_index(999, first);

  }

  my_clock = clock() - my_clock;
  time_taken = 1000000/40000*((double)my_clock)/CLOCKS_PER_SEC;
  printf("Sredni czas dostepu procesora do elemenu 999 to: %f mikrosek\n",time_taken);

  my_clock = clock();

  for(int i = 0; i < 40000; i++)
  {
    get_value_by_index(rand() % 1000, first);

  }
  my_clock = clock() - my_clock;
  time_taken = 1000000/40000*((double)my_clock)/CLOCKS_PER_SEC;
  printf("Sredni czas dostepu procesora do losowego elemenu to: %f mikrosek\n",time_taken);

  free(first);
  return 0;
}
