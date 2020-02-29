#include <stdio.h>
#include <math.h>

int main()
//calcula pi mediante el metodo Monte Carlo
{
    double x,y,r0,r,pi; //coordenadas,distanticia al origen, pi
    FILE *f;
    int p = 0;  //puntero donde se guardan el numero de puntos que caen en el circulo

    f = fopen("RawPoints.txt","r");

    r0 = 1./4.;

    while(fscanf(f,"%lf\t%lf",&x,&y)!=EOF)
    //calcula cuantos puntos caen dentro del area del circulo
    {
        r = pow(x,2) + pow(y,2);
        if(r <= r0)
        {
            p++;
        }
    }

    fclose(f);

    pi = p*4./25996.;

    printf("PI es aproximadamente: %lf\n",pi);

    return 0;
}
