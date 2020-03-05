#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 100 //numero de iteraciones del algoritmo

int main()
{
    double h,t,m,n,r[][3],v[][3];
    FILE *f1,*f2;

    f1 = fopen("Datos_Iniciales.txt","r");
    f2 = fopen("Resultados_Dinamica.txt","w");

    fscanf(f1,"%lf\n%lf\n%lf%lf\n%lf\n%lf%lf\n%lf",&h,&t,&m,&n,&r,&v);

    aceleracion(&r,&m,n); //aceleracion inicial

    for(i=0;i<N;i++)
    {
        posicion(&r, &v, &a, h, n); //calula r(t+h)


    }



    printf("%lf\n",h);
    return 0;
}

void aceleracion(double *r[][3], double m, int n)
{
    double *a[][3];
    int i,j,k;

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(j!=i)
            {
                for(k=0;k<3;k++)
                {
                    a[i][k] = -m[j]*(r[i][k]-r[j][k])/pow(abs(r[i][k]-r[j][k]),3);
                }
            }
        }
    }

    return;
}

void posicion(double *r[][3], double *v[][3], double *a[][3], double h, int n)
{
    int i,j;

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            r[i][j] = r[i][j] + h*v[i][j] + pow(h,2)/2.*a[i][j];
        }
    }
}

void velocidad(double v[][3], double a[][3], double ah[][3], double h, int n)
{
    int i,j;

    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            v[i][j] = v[i][j] + h/2.*(a[i][j]+ah[i][j]);
        }
    }

    return;
}

