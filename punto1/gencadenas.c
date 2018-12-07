#include<stdio.h>
#include<omp.h>
#include<stdlib.h>
#include <time.h>
#include <math.h>

double rand01(){
    return (double)rand()/(double)RAND_MAX;
}
double randNormal(double ancho, double centro){
    double d1 = rand01();
    double d2 = rand01();
    if(d1==0){
        return centro;
    }
    else if(d1>0.5){
        return (ancho*log(d2))+centro;
    }
    else{
        return (-ancho*log(d2))+centro;
    }
}
double funcion(double x){
    return (exp((-pow(x,2))/2))/(sqrt(2*M_PI));
}

int main(int argc, char ** argv)
{
    #pragma omp parallel
    {
        double *list;
        int thread_id = omp_get_thread_num();
        if(!(list=malloc(1000 * sizeof(double)))){
            fprintf(stderr, "Problema con la reserva de memoria\n");
            exit(1);
        }
        srand(time(NULL)+thread_id);
        list[0] = rand01()-0.5;
        #pragma omp parallel for
        for(int k=1;k<1000;k++)
        {
            double r = randNormal(0.1,list[k-1]); 
            if(funcion(list[k-1])<funcion(r)||(funcion(r)/funcion(list[k-1]))>rand01()){
                list[k] = r;
            }
            else{
                list[k] = list[k-1];
            }
        }
        FILE *out;
        char a[100];
        sprintf(a, "archivo%d.dat", thread_id);
        if(!(out = fopen(a, "w"))){
            fprintf(stderr, "Problema abriendo el archivo\n");
            exit(1);
        }
        for(int j=0;j<1000;j++){
            fprintf(out, "%f\n", list[j]);
        }   
    }
    return 0;
}
