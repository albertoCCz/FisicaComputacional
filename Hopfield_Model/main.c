#include <stdio.h>
#include <stdlib.h>

double aExpc(int ***p, int nP, int dim);
void weights(int ***p, double **w,int nP, int dim);

int main()
{
    int i,j,k,nP = 1,dim = 2;

    // Save space for patterns' matrix
    int ***p = (int ***)malloc(nP*sizeof(int **));
    for(i=0;i<dim;i++)
    {
        p[i] = (int **)malloc(dim*sizeof(int *));

        for(j=0;j<dim;j++)
        {
            p[i][j] = (int *)malloc(dim*sizeof(int));
        }
    }

    // Save space for weigth's matrix
    double **w = (double **)malloc(dim*dim*sizeof(double *));
    for(i=0;i<dim*dim;i++)
    {
        w[i] = (double *)malloc(dim*dim*sizeof(double));
    }

    // Open pattern's file
    FILE *f;
    f = fopen("Patterns/Dim2_Numprueba.txt","r");


    // Scan pattern to array p (pointer of pointers of pointers)
    for(i=0;i<nP;i++)
    {
        for(j=0;j<dim;j++)
        {
            for(k=0;k<dim;k++)
            {
                fscanf(f,"%d",p[i][j]+k);
            }
        }
    }

    // Calculte the expectation value a of activated neurons
    //printf("%lf",aExpc(p,nP,dim));
    weights(p,w,nP,dim);
    FILE *f_prueba;
    f_prueba = fopen("Patterns/weights_prueba.txt","w");

    for(i=0;i<dim*dim;i++)
    {
        for(j=0;j<dim*dim;j++)
        {
            fprintf(f_prueba,"%lf",w[i][j]);
            if((j+1)%(dim*dim) == 0)
            {
                fprintf(f_prueba,"\n");
            }
            else
            {
                fprintf(f_prueba,"\t");
            }
        }
    }

    free(p);
    fclose(f);

    return 0;
}


double aExpc(int ***p, int nP, int dim)
/*
This function returns the ratio of activated neurons in all patterns
p:      3-d array containing the patterns
nP:     number of patterns
dim:    sqrt of N, the number of neurons in each pattern
*/
{
    double expVal = 0.;
    int i,j,k,count;

    for(i=0;i<nP;i++)   //for pattern i
    {
        count = 0;
        for(j=0;j<dim;j++)  //for row j
        {
            for(k=0;k<dim;k++)  //for colums k
            {
                if(p[i][j][k] == 1) //if neuron(j,k) is activated
                {
                    count ++; //count it
                }
            }
        }
        expVal += (1.*count)/(1.*dim*dim)/(1.*nP);  //add the ratio for pattern i divided for nP
    }

    return expVal;
}


void weights(int ***p, double **w,int nP, int dim)
/*
This function calculates the weight matrix
p:      3-d array containing the patterns
w:      weigth matrix
nP:     number of patterns
dim:    sqrt of N, the number of neurons in each pattern
*/
{
    int i,j,k,N = dim*dim;
    double a,temp;

    a = aExpc(p,nP,dim);

    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(j==i)
            {
                w[i][j] = 0;
            }
            else
            {
                temp = 0;
                for(k=0;k<nP;k++)
                {
                    temp += 1./(a*(1-a)*N) * (p[k][i/dim][i%dim] - a) * (p[k][j/dim][j%dim] - a);
                }
                w[i][j] = temp;
            }
        }
    }
}
