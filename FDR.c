#include <stdio.h>
#include <math.h>

double s1(double r),s2(double r),s3(double r),f1(double r),f2(double r),f3(double r);
void normSimpson(double l, double *p1, double *p2, double *p3);

int main()
{
    double l,p1,p2,p3;

    //pedimos el limite superior de integracion
    printf("Introduce el valor del limite:\n");
    scanf("%lf",&l);

    //hallamos la normalizacion y la mostramos
    normSimpson(l,&p1,&p2,&p3);
    printf("La FDR para s1 es: 4pi(r^2)/(%lf)*|exp(-r/2)|^2\n"
           "La FDR para s2 es: 4pi(r^2)/(%lf)*|(2-r)/sqrt(32)*exp(-r/2)|^2\n"
           "La FDR para s2 es: 4pi(r^2)/(%lf)*|(6-6*r+r^2)*exp(-r/22)|^2",p1,p2,p3);

    return 0;
}

//Definimos los orbitales y el integrando
double s1(double r)
{
    double s1;

    s1 = exp(-r/2.);

    return s1;
}

double f1(double r)
{
    double f1 = 4.*M_PI*pow(r,2)*pow((s1(r)),2);    //Integrando

    return f1;
}

double s2(double r)
{
    double s2;

    s2 = (2.-r)/sqrt(32.)*exp(-r/2.);

    return s2;
}

double f2(double r)
{
    double f2 = 4.*M_PI*pow(r,2)*pow((s2(r)),2);    //Integrando

    return f2;
}

double s3(double r)
{
    double s3;

    s3 = (6.-6.*r+pow(r,2))/sqrt(972.)*exp(-r/2.);

    return s3;
}

double f3(double r)
{
    double f3 = 4.*M_PI*pow(r,2)*pow((s3(r)),2);    //Integrando

    return f3;
}

//Definimos la funcion normalizadora
void normSimpson(double l, double *p1, double *p2, double *p3)
{
    double a;

    *p1 = 0.;     //Punteros almacenan la suma de la integral a intervalos [a,b]
    *p2 = 0.;
    *p3 = 0.;

    for(a=0;a<=l;a+=0.1)
    {
        double b;   //Limite superior del intervalo de integracion

        b = a+0.1;
        *p1 = (*p1)+(b-a)/6*(f1(a)+f1(b)+4.*f1((a+b)/2.));  //Integral segun regla de Simpson, que guardamos en el puntero
        *p2 = (*p2)+(b-a)/6*(f2(a)+f2(b)+4.*f2((a+b)/2.));
        *p3 = (*p3)+(b-a)/6*(f3(a)+f3(b)+4.*f3((a+b)/2.));
    }

    return;
}
