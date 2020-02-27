# include <stdio.h>
#include <math.h>

double s1(double r),s2(double r),s3(double r),f1(double r);
void normSimpson(double l, double *p);

int main()
{
    double l,p;

    //pedimos el limite superior de integracion
    printf("Introduce el valor del limite:\n");
    scanf("%lf",&l);

    //hallamos la normalizacion y la mostramos
    normSimpson(l,&p);
    printf("%lf",p);

    return 0;
}

//Definimos los orbitales
double s1(double r)
{
    double s1;

    s1 = exp(-r/2.);

    return s1;
}

double f1(double r)
{
    double f1 = pow((4.*M_PI*r*s1(r)),2);    //Integrando

    return f1;
}
/*
double s2(double r)
{
    double s2;

    s2 = (2.-r)/sqrt(32.)*exp(-r/2.);

    return s2;
}

double s3(double r)
{
    double s3;

    s3 = (6.-6.*r+pow(r,2))*exp(-r/2.);

    return s3;
}
*/
//Definimos la funcion normalizadora
void normSimpson(double l, double *p)
{
    double a,b;

    b = a+0.1;   //Limite superior del intervalo de integracion
    *p = 0.;     //Puntero va almecenar la suma de la integral a intervalos [a,b]

    for(a=0;a<=l;a+=0.1)
    {
        *p = (*p)+(b-a)/6*(f1(a)+f1(b)+4.*f1((a+b)/2.));  //Integral segun regla de Simpson, que guardamos en el puntero
        printf("%lf",*p);
    }

    return;
}
