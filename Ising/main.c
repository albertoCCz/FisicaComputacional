#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int energiaDelta(int **s, int i, int j, int dim);

int main()
{
    int i, j, dim = 10, time = 100;  //dim^2 = dimension of the net; time = time of execution (in dim^2 units)
    int timeLimit = time*pow(dim,2);    //time limit
    int T = 2;

    FILE *f1,*f2;
    f1 = fopen("RandState_6531898.txt","r");    //Initial random state
    f2 = fopen("RandPoints_6531898.txt","r");   //Random sample of points of the net


    //pointer to pointer containing the initial state
    int **s = (int **)malloc(dim*sizeof(int *));
    for(i=0;i<dim;i++)
    {
        s[i] = (int *)malloc(dim*sizeof(int));
    }

    //pointer to pointer containing the random points
    int **p = (int **)malloc(timeLimit*sizeof(int *));
    for(i=0;i<timeLimit;i++)
    {
        p[i] = (int *)malloc(2*sizeof(int));
    }

    //scan data to save it in its pointers
    //scan state
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            fscanf(f1,"%d",s[i]+j);
        }
    }

    //scan points
    for(i=0;i<timeLimit;i++)
    {
        for(j=0;j<2;j++)
        {
            fscanf(f2,"%d",p[i]+j);
        }
    }

    //Metropolis' algorthim
    for(i=0;i<timeLimit;i++)
    {




    }



    return 0;
}


int energiaDelta(int **s, int i, int j, int dim)
//energy increase
{
    eD = 2*s[i][j](s[(i+1)%dim][j] + s[(i-1)%dim][j] + s[i][(j+1)%dim] + s[i][(j-1)%dim]);

    return eD;
}

