#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void aceleracion(double **r, double **ah, double *m, int n);
void posicion(double **r, double **v, double **a, double h, int n);
void velocidad(double **r, double **v, double **a, double **ah, double h, int n);
void copyVector(double **v1, double **v2, int n);
double distancia(double **r, int i, int k);
double moduloCuadrado(double **v1, int i);
double eCinetica(double **v, double *m, int n);
double ePotencial(double **r, double *m, int n);

int main()
{
    int i,j,iter,n,N = 20000001;
    double h = 0.0001;
    FILE *f1,*f2;

    f1 = fopen("Datos_Iniciales.txt", "r");  //Datos_Iniciales.txt
    f2 = fopen("Posiciones.txt", "w");

    fscanf(f1,"%d",&n); //lee el numero de cuerpos del sistema

    //creamos los punteros a punteros (matrices) que contienen la info dinamica
    double **r = (double **)malloc(n*sizeof(double *));
    double **v = (double **)malloc(n*sizeof(double *));
    double **a = (double **)malloc(n*sizeof(double *));
    double **ah = (double **)malloc(n*sizeof(double *));
    double *m = (double *)malloc(n*sizeof(double));
    for(i=0;i<n;i++)
    {
        r[i] = (double *)malloc(2*sizeof(double));
        v[i] = (double *)malloc(2*sizeof(double));
        a[i] = (double *)malloc(2*sizeof(double));
        ah[i] = (double *)malloc(2*sizeof(double));
    }

    //leemos del fichero las condiciones iniciales de la posicion y la velocidad
    for(i=0;i<n;i++)
    {
        fscanf(f1,"%lf\t%lf\t%lf\t%lf\t%lf",r[i],r[i]+1,v[i],v[i]+1,&m[i]);
    }

    //aumentamos un 15% la velocidad inicial de los planetas
    /*for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            r[i][j] = r[i][j]-r[3][j];
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            v[i][j] = v[i][j]-v[3][j];
        }
    }*/
    //calculamos el valor inicial de las aceleraciones
    aceleracion(r,ah,m,n);

    //implementamos el algoritmo de Verlet con todas las funciones que hemos definido
    for(iter=0;iter<N;iter++)
    {
        posicion(r,v,ah,h,n);
        copyVector(a,ah,n);
        aceleracion(r,ah,m,n);
        velocidad(r,v,a,ah,h,n);
        /*for(i=0;i<n;i++)
        {
            for(j=0;j<2;j++)
            {
                r[i][j] = r[i][j]-r[3][j];
            }
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<2;j++)
            {
                v[i][j] = v[i][j]-v[3][j];
            }
        }*/
        //guardamos en un fichero las sucesivas posiciones de los cuerpos
        if(iter%1000 == 0)
        {
            for(i=0;i<n;i++)
            {
                fprintf(f2,"%lf\t%lf",r[i][0]-r[3][0],r[i][1]-r[3][1]);   //escribimos en un fichero las sucesivas posiciones de los planetas

                if(i==n-1)
                {
                    fprintf(f2,"\t%lf\t%lf\n",eCinetica(v,m,n),ePotencial(r,m,n));
                }
                else
                {
                    fprintf(f2,"\t");
                }

            }
        }
    }

    //liberamos el espacio en memoria
    free(r);
    free(v);
    free(a);
    free(ah);

    return 0;
}


double distancia(double **r, int i, int k)
//calcula la distancia entre los cuerpos i y k
{
    double mod,temp = 0;
    int j;

    if(k!=i)
    {
        for(j=0;j<2;j++)
        {
            temp = temp + pow((r[i][j] - r[k][j]),2);
        }
    }

    mod = sqrt(temp);

    return mod;
}


void aceleracion(double **r, double **ah, double *m, int n)
//calcula la aceleracion de cada cuerpo
{
    int i,j,k;

    for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            ah[i][j] = 0.;
        }
    }

    for(i=0;i<n;i++)    //aceleracion del objeto i
    {
        for(j=0;j<2;j++)    //componente j de la aceleracion
        {
            for(k=0;k<n;k++)        //debida al cuerpo k
            {
                if(k!=i)
                {
                    ah[i][j] = ah[i][j] - m[k] * (r[i][j] - r[k][j])/pow(distancia(r,i,k),3); //actualizamos a(t+h)
                }
                else
                {
                    continue;
                }
            }
        }
    }
}

void copyVector(double **v1, double **v2, int n)
//copia en v1 los valores guardados en el puntero de punteros v2
{
    int i,j;

    for(i=0;i<n;i++)    //puntero de puntero i
    {
        for(j=0;j<2;j++)    //puntero j
        {
            v1[i][j] = v2[i][j];
        }
    }
}


void posicion(double **r, double **v, double **ah, double h, int n)
//calcula la posicion de los distintos cuerpos
{
    int i,j;

    for(i=0;i<n;i++)    //posicion del objeto i
    {
        for(j=0;j<2;j++)    //componente j de la posicion
        {
            r[i][j] = r[i][j] + h * v[i][j] + pow(h,2)/2. * ah[i][j];
        }
    }
}

void velocidad(double **r, double **v, double **a, double **ah, double h, int n)
//calcula la velocidad de los distintos cuerpos
{
    int i,j;

    for(i=0;i<n;i++)    //velocidad del objeto i
    {
        for(j=0;j<2;j++)    //componente j de la velocidad
        {
            v[i][j] = v[i][j] + h/2. * (a[i][j] + ah[i][j]);
        }
    }
}

double moduloCuadrado(double **v1, int k)
{
    int i;
    double value = 0.;

    for(i=0;i<2;i++)
    {
        value = value + pow(v1[k][i],2);
    }

    return value;
}


double eCinetica(double **v, double *m, int n)
{
    int i,j;
    double temp = 0.0, eCin = 0.0;

    for(i=0;i<n;i++)
    {
        for(j=0;j<2;j++)
        {
            temp = temp + pow(v[i][j],2);
        }
        eCin = eCin + 1./2*m[i]*temp;
    }

    return eCin;
}


double ePotencial(double **r, double *m, int n)
{
    int i,j;
    double ePot = 0.0;

    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            ePot = ePot - m[i]*m[j]/distancia(r, i, j);
        }
    }

    return ePot;
}
