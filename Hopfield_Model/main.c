#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void aExpc(int ***p, double *expVal, int nP, int dim);
void weights(int ***p, double **w, double *expVal, int nP, int dim);
void threshold(int ***p, double **w, double *thHold, int dim);
double energyDelta(int ***p, double **w, int **s, double *thHold, int nP, int dim, int n);
void solapamiento(int ***p, int **s, double *expVal, double *solap, int nP, int dim);


int main()
{
    int i,j,k,nP = 1,dim = 20, N = dim*dim, pasosMC = 20;
    double expt,c,T = 0.0001;
    FILE *f,*g,*h,*l,*o;

    // Open files
    f = fopen("Patterns/Dim20_Num1.txt","r");
    g = fopen("PatternsNoisy/Dim20_Num1_0.3.txt","r");
    h = fopen("Iteraciones/Dim20_pasosMC20.txt","r");
    l = fopen("Results/Dim20_Num1_pasosMC20_States.txt","w");
    o = fopen("Results/Dim20_Num1_pasosMC20_Solap.txt","w");


    // Save space for patterns matrix
    int ***p = (int ***)malloc(nP*sizeof(int **));
    for(i=0;i<dim;i++)
    {
        p[i] = (int **)malloc(dim*sizeof(int *));

        for(j=0;j<dim;j++)
        {
            p[i][j] = (int *)malloc(dim*sizeof(int));
        }
    }

    // Save space for state of the system matrix
    int **s = (int **)malloc(dim*sizeof(int *));
    for(i=0;i<dim;i++)
    {
        s[i] = (int *)malloc(dim*sizeof(int));
    }

    // Save space for weights matrix
    double **w = (double **)malloc(N*sizeof(double *));
    for(i=0;i<N;i++)
    {
        w[i] = (double *)malloc(N*sizeof(double));
    }

    // Save space for random points vector
    int *points = (int *)malloc(pasosMC*N*sizeof(int));

    // Save space for sigma values vector
    double *sigma = (double *)malloc(pasosMC*N*sizeof(double));

    // Save space for threshold array
    double *thHold = (double *)malloc(N*sizeof(double));

    // Save space for expectation value of a
    double *expVal = (double *)malloc(nP*sizeof(double));

    // Save space for solapamiento array
    double *solap = (double *)malloc(nP*sizeof(double));

    // Scan pattern to array p
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

    // Scan initial state to s
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            fscanf(g,"%d",s[i]+j);
        }
    }

    // Scan random points and sigma arrays
    for(i=0;i<pasosMC*N;i++)
    {
        fscanf(h,"%d\t%lf",points+i,sigma+i);
    }


    // Initialize problem: "a" coefficients + Weights + Threshold
    // Calculate "coefficients" a
    aExpc(p,expVal,nP,dim);

    // Calculate weights
    weights(p,w,expVal,nP,dim);

    // Calculates threshold
    threshold(p,w,thHold,dim);


    // Metropolis' algorithm
    for(i=0;i<pasosMC*N;i++)
    {
        expt = exp(-energyDelta(p,w,s,thHold,nP,dim,points[i])/T);
        c = (1. <= expt) ? 1. : expt;
        s[points[i]/dim][points[i]%dim] = sigma[i] < c ? (s[points[i]/dim][points[i]%dim] + 1)%2 : s[points[i]/dim][points[i]%dim];

        if(i%(pasosMC*N/100)==0)
        {
            for(j=0;j<N;j++)
            {
                fprintf(l,"%d",s[j/dim][j%dim]);
                if((j%dim)+1 == dim)
                {
                    fprintf(l,"\n");
                }
                else
                {
                    fprintf(l,"\t");
                }
            }
            fprintf(l,"\n");

        }
        if(i%(pasosMC*N/1000)==0)
        {
            solapamiento(p,s,expVal,solap,nP,dim);  // Calcula el solapamiento del estado del sistema
            for(k=0;k<nP;k++)                       // para la iteracion i-esima con cada patron almacenado
            {
                fprintf(o,"%lf\t%lf",solap[k],1.*i/N);
                if(k+1 == nP)
                {
                    fprintf(o,"\n");
                }
                else
                {
                    fprintf(o,"\t");
                }
            }
        }
    }

    fclose(f);
    fclose(g);
    fclose(h);
    fclose(l);
    fclose(o);

    return 0;
}


void aExpc(int ***p, double *expVal, int nP, int dim)
/*
This function returns the ratio of activated neurons in all patterns
p:      3-d array containing the patterns
nP:     number of patterns
dim:    sqrt of N, the number of neurons in each pattern
*/
{
    int i,j,k,count;

    for(i=0;i<nP;i++)   //for pattern i
    {
        count = 0;
        expVal[i] = 0.;
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
        expVal[i] += (1.*count)/(1.*dim*dim);    //add the ratio for pattern i divided for nP
    }
}


void weights(int ***p, double **w, double *expVal, int nP, int dim)
/*
This function calculates the weight matrix
p:      3-d array containing the patterns
w:      weigth matrix
nP:     number of patterns
dim:    sqrt of N, the number of neurons in each pattern
*/
{
    int i,j,k,N = dim*dim;
    double temp;

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
                    temp += 1./N * (p[k][i/dim][i%dim] - expVal[k]) * (p[k][j/dim][j%dim] - expVal[k]);
                }
                w[i][j] = temp;
            }
        }
    }
}


void threshold(int ***p, double **w, double *thHold, int dim)
/*
This function calculates the threshold, theta, of neuron i
p:      3-d array containing the patterns
w:      weigth matrix
thHold: array keeping the threshold for each neuron
nP:     number of patterns
dim:    sqrt of N, the number of neurons in each pattern
*/
{
    int i,j,N = dim*dim;
    double temp;

    for(i=0;i<N;i++)
    {
        temp = 0.;
        for(j=0;j<N;j++)
        {
            temp += w[i][j];
        }
        thHold[i] = temp/2.;
    }
}


double energyDelta(int ***p, double **w, int **s, double *thHold, int nP, int dim, int n)
/*
This function calculates the energy of the system for some state s
*/
{
    int i,sign,N = dim*dim;
    double temp = 0.;


    // Calculates the energy change
    for(i=0;i<N;i++)
    {
        temp += w[n][i] * s[i/dim][i%dim];
    }

    sign = s[n/dim][n%dim] - (s[n/dim][n%dim] + 1)%2;

    return sign*temp - sign*thHold[n];
}


void solapamiento(int ***p, int **s, double *expVal, double *solap, int nP, int dim)
{
    int i,j,N = dim*dim;
    double temp;

    for(i=0;i<nP;i++)
    {
        temp = 0.;
        for(j=0;j<N;j++)
        {
            temp += (p[i][j/dim][j%dim] - expVal[i]) * (s[j/dim][j%dim] - expVal[i]);
        }
        solap[i] = temp * 1./(N*expVal[i]*(1-expVal[i]));
    }
}
