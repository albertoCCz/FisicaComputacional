#include <stdio.h>

int main()
{
    int n,i,j,k,iter;
    double b,nom = 0.,den = 0.,lambda;

    printf("Orden de A:\n"); //creamos la matriz A de orden n*n
    scanf("%d",&n);
    double a[n][n],xA[n][n];

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

    for(k=0;k<iter;k++)
    {
        for(i=0;i<=n-1;i++) //hacemos el producto de A*x
        {
            for(j=0;j<=n-1;j++)
            {
                x[i][0] += a[i][j]*x0[j][0];

                if(i>0)
                //save in b the largest component of x
                {
                    if(x[i][0]>x[i-1][0])
                    {
                        b = x[i][0];
                    }
                }
            }
        }
        for(i=0;i<n;i++)
        //dividimos x entre b
        {
            x0[i][0] = x[i][0]/b;
        }
    }

    for(i=0;i<=n-1;i++) //hacemos el producto de A*x
    {
        for(j=0;j<=n-1;j++)
        {
            xA[i][0] += a[i][j]*x0[j][0];
        }
    }

    for(i=0;i<n;i++) //calulamos lambda mediante el cociente de Rayleight
    {
        nom += x0[i][0]*xA[i][0];
        den += x0[i][0]*x0[i][0];
    }

    lambda = nom/den;
    printf("El autovalor dominante es:\nLambda = %lf\n",lambda);

    return 0;
}


