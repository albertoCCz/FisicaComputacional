#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double distThirdPow(double **r, int n, int i, int k);
void aceleracion(double **r, double **a, double **ah, double *m, int n);
void posicion(double **r, double **v, double **a, double h, int n);
void velocidad(double **r, double **v, double **a, double **ah, double h, int n);

int main()
{
    int i,iter,n,N = 10000000;
    double h = 0.01;
    FILE *f1,*f2;

    f1 = fopen("Datos_Iniciales.txt", "r");
    f2 = fopen("Posiciones.txt", "w");

    printf("Numero de objetos estelares?\n");
    scanf("%d",&n);

    //creamos los punteros a punteros que contienen la info dinamica
    double **r = (double **)malloc(n*sizeof(double *));
    double **v = (double **)malloc(n*sizeof(double *));
    double **a = (double **)malloc(n*sizeof(double *));
    double **ah = (double **)malloc(n*sizeof(double *));
    double *m = (double *)malloc(n*sizeof(double));
    for(i=0;i<n;i++)
    {
        *(r+i) = (double *)malloc(2*sizeof(double));
        *(v+i) = (double *)malloc(2*sizeof(double));
        *(a+i) = (double *)malloc(2*sizeof(double));
        *(ah+i) = (double *)malloc(2*sizeof(double));
    }

    for(i=0;i<n;i++)
    {
        fscanf(f1,"%lf\t%lf\t%lf\t%lf\t%lf",*(r+i),(*(r+i)+1),*(v+i),(*(v+i)+1),m+i);
    }

    //calculamos el valor inicial de las aceleraciones
    aceleracion(r,a,ah,m,n);

    //implementamos el algoritmo de Verlet con todas las funciones que hemos definido
    for(iter=0;iter<N;iter++)
    {

        posicion(r,v,ah,h,n);
        fprintf(f2,"%lf\t%lf\n",**(r+0),*(*(r+0)+1));
        aceleracion(r,a,ah,m,n);
        velocidad(r,v,a,ah,h,n);

    }

    free(r);
    free(v);
    free(a);
    free(ah);

    return 0;
}


double distThirdPow(double **r, int n, int i, int k)
//calcula la distancia entre los cuerpos i y k y la eleva al cubo
{
    double mod,temp = 0;
    int j;

    if(k!=i)
    {
        for(j=0;j<2;j++)
        {
            temp = temp + pow((*(*(r+i)+j) - *(*(r+k)+j)),2);
        }
    }

    mod = pow(temp,3./2.);

    return mod;
}

void aceleracion(double **r, double **a, double **ah, double *m, int n)
{
    int i,k,j;

    for(i=0;i<n;i++)
    {
        for(k=0;k<n;k++)
        {
            if(k!=i)
            {
                for(j=0;j<2;j++)
                {
                    *(*(a+i)+j) = *(*(ah+i)+j); //copiamos la info de a(t+h) en a(t)
                    *(*(ah+i)+j) = (*(m+k) * (*(*(r+i)+j) - *(*(r+k)+j)))/distThirdPow(r,n,i,k); //actualizamos a(t+h)
                }
            }
        }
    }
}

void posicion(double **r, double **v, double **a, double h, int n)
{
    int i,j;

    for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            *(*(r+i)+j) = *(*(r+i)+j) + h * (*(*(v+i)+j)) + pow(h,2)/2. * (*(*(a+i)+j));
        }
    }
}

void velocidad(double **r, double **v, double **a, double **ah, double h, int n)
{
    int i,j;

    for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            *(*(v+i)+j) = *(*(v+i)+j) + h/2. * (*(*(a+i)+j) + *(*(ah+i)+j));
        }
    }
}
