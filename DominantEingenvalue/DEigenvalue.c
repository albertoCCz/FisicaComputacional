#include <stdio.h>

int main()
{
    int n,i,j,iter;

    printf("Orden de A:\n"); //creamos la matriz A de orden n*n
    scanf("%d",&n);
    double a[n][n];

    double x0[n][1];   //creamos el vector propio en aproximacion cero
    for(i=0;i<=n-1;i++)
    {
        x0[i][0] = 1.;
    }

    double x[n][1];   //vector propio temporal
    for(i=0;i<=n-1;i++)
    {
        x[i][0] = 0.;
    }

    printf("Valores de A:\n");  //pedimos los valores para la matriz
    for(i=0;i<=n-1;i++)
    {
        for(j=0;j<=n-1;j++)
        {
            printf("Introduce el valor de a%d%d:\t",i,j);
            scanf("%lf",&a[i][j]);
        }
    }

    //comprobamos que la matriz sea simetrica
    for(i=0;i<=n-1;i++)
    {
        for(j=i+1;j<=n-1;j++)
        {
            if(a[i][j]!=a[j][i])
            {
                printf("La matriz no es simetrica\n");
                break;
            }
        }
    }

    printf("Numero de iteraciones (a mayor numero mayor precision):\t"); //numero de iteraciones a realizar
    scanf("%d",&iter);

    for(i=0;i<=n-1;i++) //hacemos el producto de A*x
    {
        for(j=0;j<=n-1;j++)
        {
                x[i][0] += a[i][j]*x0[j][0];
        }
    }

    printf("x es: %lf\t%lf\n",x[0][0],x[1][0]);

    return 0;
}


