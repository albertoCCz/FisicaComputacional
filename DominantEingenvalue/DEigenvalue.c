#include <stdio.h>

int main()
{
    int n,i,j,iter;
    double x0[3] = {1.,1.,1.};   //creamos el vector propio en aproximacion cero

    printf("Orden de A:\n"); //creamos la matriz A de orden n*n
    scanf("%d",&n);
    double a[n][n];

    printf("Valores de A:\n");  //pedimos los valores para la matriz
    for(i=0;i<=n-1;i++)
    {
        for(j=0;j<=n-1;j++)
        {
            printf("Introduce el valor de a%d%d:\t",i,j);
            scanf("%lf",&a[i][j]);
        }
    }

    printf("Numero de iteraciones (mayor numero mayor precision):\t");
    scanf("%d",iter);

    return 0;
}


