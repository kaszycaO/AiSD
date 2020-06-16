#include <stdio.h>
#include <stdbool.h>




int first, last, items, size;

void add_element(int *main_tab, int element);
void remove_element(int *main_tab);
void print_queue(int *main_tab);
bool isEmpty();
bool isFull();

void initialize()
{
  first = -1;
  last = -1;
  items = 0;
}

bool isEmpty()
{
  if ((first == -1 && last == -1) || items == 0)
    return true;
  else
    return false;
}

bool isFull()
{
  if (last == size && items == 0)
  {
    return true;
  }

  else
    return false;
}

void add_element(int *main_tab, int element)
{
  if(isFull())
  {
    printf("Kolejka jest pelna!\n");
    return;
  }

  else if(isEmpty())
  {
    first = 0;
    last = 0;
  }

  main_tab[last] = element;
  items++;
  last++;

}

void remove_element(int *main_tab)
{
  if(isEmpty())
  {
    printf("Kolejka jest pusta!\n");
    first = 0;
    last = 0;
    return;
  }

  main_tab[first] = 0;
  items--;
  first++;
}


void print_queue(int *main_tab)
{
  for(int i = first; i < last; i++)
  {
    if(main_tab[i]!= 0)
      printf("%d ", main_tab[i]);
  }
    printf("\n");

}


int main()
{

  printf("Podaj rozmiar kolejki\n");
  scanf("%i",&size);
  int main_tab[size];
  initialize();

  for(int i = 1; i <=size; i++)
  {
    add_element(main_tab,i);
    print_queue(main_tab);

  }

  for(int i = 1; i < size; i++)
  {
    remove_element(main_tab);
    print_queue(main_tab);

  }




  return 0;
}
