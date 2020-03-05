#include <stdio.h>
#include <math.h>

int main()
{
    FILE *f1,*f2;
    int i;
    double p,a,b,n,v1,v2,r,t,di;

    f1 = fopen("Datos.txt","r");
    f2 = fopen("Presiones.txt","w");

    fscanf(f1,"%lf\n%lf\n%lf\n%lf\n%lf\n%lf\n%lf",&a,&b,&n,&v1,&v2,&r,&t);

    di = (v2-v1)/11;    //incremento de volumen

    while(v1<=v2)
    //calculamos la presion para cada valor de V
    {
        p = n*r*t/(v1-n*b)-a*pow(n,2)/pow(v1,2);
        fprintf(f2,"V=%lf --> P=%lf\n",v1,p);
        v1 += di;
    }

    fclose(f1);
    fclose(f2);

    return 0;
}
