#include <stdio.h>

void task(int *p)
{
	printf("%d\n", *p);
}

int main(void)
{
	int x = 5;
	task(&x);
}
