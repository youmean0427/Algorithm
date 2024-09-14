#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
        char    one[9];
        char    two[9];
        char    three[9];

        scanf("%s", one);
        scanf("%s", two);
        scanf("%s", three);
        
        int     num;
        if (atoi(one))
            num = atoi(one) + 3;
		else if (atoi(two))
			num = atoi(two) + 2;
		else if (atoi(three))
			num = atoi(three) + 1;

		if (num % 3 == 0 && num % 5 == 0)
			printf("FizzBuzz");
		else if (num % 3 == 0 && num % 5 != 0)
			printf("Fizz");
		else if (num % 3 != 0 && num % 5 == 0)
			printf("Buzz");
		else
			printf("%d", num);
}