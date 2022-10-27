/**
 * @file armstrong.c
 * @author andrea.larghi@heig-vd.ch
 * @date October 2022
 * @note to COMPILE: Use Makefile
 */

/**
 * Check Armstrong number.
 *
 * This program checks if a number is an
 *
 * Example:
 *
 *     ./armstrong --verbose ...
 */
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool is_armstrong(unsigned long long int number) {

    unsigned long long int memNumber = number;

    int digitsNumber = 0;   //A.Larghi | Number of digits
    int digits[100];         //A.Larghi | Individual digit
    unsigned long long int compareNumber = 0;  

    do{ //Size of number and digit isolation
        digits[digitsNumber] = memNumber - (memNumber/10)*10;
        memNumber = memNumber/10;
        digitsNumber++;
    }while(memNumber != 0);

    for(int i = 0; i < digitsNumber ; i++){
        compareNumber = compareNumber + pow(digits[i],digitsNumber);
    }

    if(compareNumber == number){
        return 1;
    }
    else{
        return 0;
    }
}

void help(void){
    printf("Usage: ./armstrong [options] [number]\n");
    printf("[number] can be given through 'stdin'\n\n");
    printf("Check whether or not a number is an Armstrong number.\n");
    printf("Returns 0 for yes and 1 for no.\n\n");
    printf("  --help, -h      display help and quit\n");
    printf("  --version       display version and quit\n");
    printf("  --verbose, -v   display result on stdout\n\n");
}

void version(void){
    printf("Armstrong (c)2022 Larghi Andrea <andrea.larghi@heig-vd.ch>\n");
    printf("Version 1.0.0\n");
}

void error(void){
    printf("Argument error\n");
    printf("For more information, --help or -h\n");
}

int main(int argc, char *argv[]) {
    
    bool verbose = 0;
    unsigned long long int InputNumber = 0;

/****************A.Larghi | Processing of arguments****************/

    if(argc > 1 ) {
                
        for(int i = 1; i < argc; i++){              //A.Larghi | Help or Version check

            if (strcmp(argv[i], "--help") == 0 || strcmp(argv[1], "-h") == 0) {
                help();
                return 0;
            }

            else if (strcmp(argv[i], "--version") == 0) {
                version();
                return 0;
            }
        }

        if(sscanf(argv[1],"%llu", &InputNumber) == 0) { //A.Larghi | Converts the first argument in an int if possible

            if (strcmp(argv[1], "--verbose") == 0 || strcmp(argv[1], "-v") == 0) {
                verbose = 1;
            }

            else {                                     //A.Larghi | Conversion failed and first argument is not a valid option
                error();
                return 2;
            }

            if(argc == 2){                             //A.Larghi | Input through stdin for verbose
                if(fscanf(stdin,"%llu", &InputNumber) == 0) {
                    error();
                    return 2;
                }
            }
            else if(sscanf(argv[2],"%llu", &InputNumber) == 0) {
                error();
                return 2;
            }    
        }
    }

    else if(fscanf(stdin,"%llu", &InputNumber) == 0) {   //A.Larghi | No argument is passed to the program
        error();
        return 2;   
    }

/****************A.Larghi | Number of arguments****************/

    if (argc >3) {
        error();
        return 2;
    }

/****************A.Larghi | Output according to input****************/
    bool result = is_armstrong(InputNumber);

    if (verbose == 1) {
        if (result == 0) {
            printf("The number %llu is not an armstrong number\n", InputNumber);
        }

        else {
            printf("The number %llu is an armstrong number\n", InputNumber);
        }
    }

    return !result;
}
