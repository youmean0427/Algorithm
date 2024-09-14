#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char	p_n[11];
	char	p_s[3];
	int		p_d;
	int		s_check[2]; // F, M
	char	**ans;

	scanf("%s", p_n);
	scanf(" %s", p_s);
	scanf(" %d", &p_d);

	
	s_check[0] = 0;
	s_check[1] = 0;

	for (int i = 0; i < 2; i++)
	{
		if (p_s[i] == 'F')
			s_check[0] = 1;
		if (p_s[i] == 'M')
			s_check[1] = 1;
	}

	int	t;
	int	i;

	scanf("%d", &t);
	i = 0;
	ans = (char **)malloc(sizeof(char *) * t );
	while (i < t)
	{
		ans[i] = (char *)malloc(sizeof(char));
		i++;
	}

	int	idx;
	idx = 0;
	for (int i = 0; i < t; i++)
	{
		char	n[11];
		char	s[3];
		int		d;
		char	flag;

		s[0] = 0;
		s[1] = 0;
		s[2] = 0;

		scanf("%s", n);
		scanf(" %s", s);
		scanf(" %d", &d);
		
		flag = 'N';
		if ((s[0] == 'F' && s_check[0]) || (s[1] == 'M' && s_check[1]))
			flag = 'Y';
		if ((s[0] == 'M' && s_check[1]) || (s[1] == 'F' && s_check[0]))
			flag = 'Y';
		
		if (p_d >= d && flag == 'Y')
			flag = 'Y';
		else
			flag = 'N';


		if (flag == 'Y')
		{
			ans[idx] = strdup(n);
			idx++;
		}
	}
	ans[idx] = NULL;

	
	int	j;
	char *temp;

	i = 0;
	j = 0;
	
	for (i = 0; i < idx - 1; i++)
	{
		for (j = i + 1; j < idx; j++) 
		{
			if (strcmp(ans[i], ans[j]) > 0)
			{
				temp = ans[i];
				ans[i] = ans[j];
				ans[j] = temp;
			}
		}
	}

	idx = 0;
	if (ans[idx] == 0)
		printf("No one yet");
	else
	{
		while (ans[idx])
		{
			printf("%s\n", ans[idx]);
			idx++;
		}
	}
}