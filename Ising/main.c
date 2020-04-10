#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int energiaDelta(int **s, int i, int j, int dim);

int main()
{
    int i, j, k, dim = 28, time = 10000, cienPM = dim*dim*100;  //dim^2 = dimension of the net; time = time of execution (in dim^2 units)
    int timeLimit = time*pow(dim,2);    //time limit
    double T = 5.0;
    double c,expt;

    FILE *f1,*f2,*f3;
    f1 = fopen("Systems/28_7531898/RandState_7531898.txt","r");    //Initial random state
    f2 = fopen("Systems/28_7531898/RandPoints_7531898.txt","r");   //Random sample of points of the net
    f3 = fopen("Systems/28_7531898/StateChanges_7531898.txt","w"); //State changes

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

    //pointer containing sigma value to compare with c in the algoritm
    double *sigma = (double *)malloc(timeLimit*sizeof(double));

    //scan data to save it in its pointers
    //scan state
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            fscanf(f1,"%d",s[i]+j);
        }
    }

    //scan points and sigma
    for(i=0;i<timeLimit;i++)
    {
        for(j=0;j<2;j++)
        {
            fscanf(f2,"%d",p[i]+j);
        }
        fscanf(f2,"%lf",&sigma[i]);

    }

    //Metropolis' algorthim
    for(i=0;i<timeLimit;i++)
    {
        expt = exp(-energiaDelta(s,p[i][0],p[i][1],dim)/(T));
        c = (1. <= expt) ? 1. : expt;
        s[p[i][0]][p[i][1]] = sigma[i] < c ? -s[p[i][0]][p[i][1]] : s[p[i][0]][p[i][1]];

        if((i!=0) & (i%cienPM==0))
        //write the new state after each MC step
        {
            //fprintf(f3,"%d\t%d\n",p[i][0],p[i][1]);
            fprintf(f3,"paso: %d\n",i/cienPM);

            for(j=0;j<dim;j++)
            {
                for(k=0;k<dim;k++)
                {
                    fprintf(f3,"%d",s[j][k]);

                    if((k+1)%dim == 0)
                    {
                        fprintf(f3,"\n");
                    }
                    else
                    {
                        fprintf(f3,"\t");
                    }
                }
            }
            //printf("200");
        }

    }

    //free space and close files

    free(s);
    free(p);
    free(sigma);

    fclose(f1);
    fclose(f2);
    fclose(f3);

    return 0;
}


int energiaDelta(int **s, int i, int j, int dim)
//energy increase
{
    int eD;

    eD = 2*(s[i][j])*(s[(i+1)%dim][j] + s[i-1<0 ? dim-1 : i-1][j] + s[i][(j+1)%dim] + s[i][j-1<0 ? dim-1 : j-1]);

    return eD;
}
