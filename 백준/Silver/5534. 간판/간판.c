#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init_name(char *name)
{
    for (int i = 0; i < 101; i++)
        name[i] = 0;
}


int main(void)
{
    int n;
    char store[26];
    char name[101];
    int ans = 0;

    scanf("%d", &n);
    scanf("%s", store);

    for (int i = 0; i < n; i++)
    {
        init_name(name);
        scanf("%s", name);
    
        int name_idx = 0;
        int store_idx = 1;
        int temp = 0;

        int check = 0;
        int cnt = 1;
        int store_cnt = 0;
     
        while(name[name_idx])
        {
           if (name[name_idx] == store[0])
           {
                cnt = 1;
                temp = name_idx;
                while (cnt < strlen(name))
                {
                    store_cnt = 0;
                    store_idx = 1;
                
                    while (store_cnt < strlen(store) && name[temp+cnt])
                    {
                        if (name[temp+cnt] == store[store_idx])
                        {
                            store_idx++;
                            temp = temp + cnt;
                        }

                        store_cnt++;
                    }

                    if (store_idx == strlen(store))
                    {   
                        check = 1;
                        break;
                    }
                    cnt++;
                    temp = name_idx;
                }
            }
           name_idx++;
        }
        if (check == 1)
            ans += 1;
    }  
    printf("%d", ans);
}
