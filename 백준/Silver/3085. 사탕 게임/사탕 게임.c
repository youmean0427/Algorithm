#include <stdio.h>
#include <stdlib.h>

void	width(char **arr, int n, int *ans)
{
	int	sub;
	char	flag;
	sub = 0;
	for (int a = 0; a < n; a++)
	{
		int	start = 0;
		flag = arr[a][0];
		for (int b = 1; b < n; b++)
		{
			if (flag != arr[a][b])
			{
				sub = b - start;
				flag = arr[a][b];
				start = b;
				if (sub > *ans)
					*ans = sub;
			}
		}
		sub = n - start;
		if (sub > *ans)
					*ans = sub;
	}

}

void	height(char **arr, int n, int *ans)
{
	int	sub;
	char	flag;
	sub = 0;
	for (int a = 0; a < n; a++)
	{
		int	start = 0;
		flag = arr[0][a];
		for (int b = 1; b < n; b++)
		{
			if (flag != arr[b][a])
			{
				sub = b - start;
				flag = arr[b][a];
				start = b;
				if (sub > *ans)
					*ans = sub;
			}
		}
		sub = n - start;
		if (sub > *ans)
					*ans = sub;
	}
}

int	main(void)
{
	int	n;
	char **arr;

	int	di;
	int	dj;
	char temp;
	int	ans;

	ans = 0;
	scanf("%d", &n);
	arr = (char **)malloc(sizeof(char *) * n);
	for (int i = 0; i < n; i++)
		arr[i] = (char *)malloc(sizeof(char) * n);
	for (int i = 0; i < n; i++)
		scanf("%s", arr[i]);
	
	int	dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int d = 0; d < 4; d++)
			{
				temp = '\0';
				di = i + dir[d][0];
				dj = j + dir[d][1];

				if (di >= 0 && di < n && dj >= 0 && dj < n)
				{
					if (arr[i][j] != arr[di][dj])
					{
						temp = arr[i][j];
						arr[i][j] = arr[di][dj];
						arr[di][dj] = temp;

						width(arr, n, &ans);
						height(arr, n, &ans);

						temp = arr[i][j];
						arr[i][j] = arr[di][dj];
						arr[di][dj] = temp; 
					}
				}
			}
		}
	}
	printf("%d", ans);
}