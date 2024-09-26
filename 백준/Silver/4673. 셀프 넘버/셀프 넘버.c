#include <stdio.h>

int	main(void)
{
	int	arr[10001] = {0};
	int	ans = 0;
	int	num = 0;

	for (int i = 1; i <= 10000; i++)
	{
		num = i;
		ans = num;
		while (num > 0)
		{
			ans += num % 10;
			num /= 10;
		}
		if (ans <= 10000)
			arr[ans] = 1;
	}

	for (int i = 1; i <= 10000; i++)
	{
		if (arr[i] == 0)
			printf("%d\n", i);
	}
}