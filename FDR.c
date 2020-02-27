# include <stdio.h>
#include <math.h>

int main()
{
    return 0;
}

//Definimos los orbitales

s1(double r)
{
    s1 = exp(-r/2.);
}

s2(double r)
{
    s2 = (2.-r)/sqrt(32.)*exp(-r/2.);
}

double s3(double r)
{
    s3 = (6.-6.*r+pow(r,2))*exp(-r/2.);

    return s3;
}

//Definimos la funcion normalizadora

double normSimpson(double s)
{

}
