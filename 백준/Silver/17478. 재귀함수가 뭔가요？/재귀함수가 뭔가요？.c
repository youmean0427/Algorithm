#include <stdio.h>

void line(k, n)
{
	int	idx = 0;
	while (idx <= k - n)
	{
		printf("____");
		idx++;
	}	
}

void recur(n, k)
{
	if (n == 0)
		return;

	line(k, n);
	printf("\"재귀함수가 뭔가요?\"\n");
	
	if (n > 1)
	{
	line(k, n);
	printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
	line(k, n);
	printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
	line(k, n);
	printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
	}
	else 
	{
		line(k, n);
		printf("\"재귀함수는 자기 자신을 호출하는 함수라네\"\n");
	}

	recur(n-1, k);
	line(k, n);
	printf("라고 답변하였지.\n");
}

int	main(void)
{
	int	n;
	int	k;

	scanf("%d", &n);
	k = n;
	printf("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
	printf("\"재귀함수가 뭔가요?\"\n");
	printf("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n");
	printf("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n");
	printf("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n");
	recur(n, k);
	printf("라고 답변하였지.\n");
}
