#include <stdio.h>
int main()
{
    int a,s,i,x,p,n,y;
    printf("Please enter a value <= 13 \n");
    scanf("%d",&n);
    i=0;
    for(a=0;a<n;a++)
	{
		i=i+a+1;p=i,y=p;
        for(s=1;s<=n-(a+1);s++)
            printf("   ");
        for(x=0;x<=a;x++)
        {
            if((y--)<10)
                printf(" %d ",p--);
            else
                printf("%d ",p--);
        }
        printf ("\n");
    }
    return 0;
}
/*Please enter a value <= 13
13
                                     1
                                  3  2
                               6  5  4
                           10  9  8  7
                        15 14 13 12 11
                     21 20 19 18 17 16
                  28 27 26 25 24 23 22
               36 35 34 33 32 31 30 29
            45 44 43 42 41 40 39 38 37
         55 54 53 52 51 50 49 48 47 46
      66 65 64 63 62 61 60 59 58 57 56
   78 77 76 75 74 73 72 71 70 69 68 67
91 90 89 88 87 86 85 84 83 82 81 80 79
*/
