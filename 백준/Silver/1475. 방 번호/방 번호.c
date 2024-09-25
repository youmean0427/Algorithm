#include <stdio.h>
#include <math.h>

void arr_init(int *arr)
{
	for (int i = 0; i < 10; i++)
		arr[i] = 0;
}

int	main(void)
{
	int	n;
	int	arr[10];
	scanf("%d", &n);

	arr_init(arr);
	while (n > 0)
	{
		arr[n % 10] += 1;
		n /= 10;
	}

	int max_cnt;
	max_cnt = ceil((float)(arr[6] + arr[9]) / 2);
	for (int i = 0; i < 10; i++)
	{
		if (i != 6 && i != 9)
		{
			if (max_cnt < arr[i])
			{
				max_cnt = arr[i];
			}
		}	
	}
	printf("%d", max_cnt);
}
