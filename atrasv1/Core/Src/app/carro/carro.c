/*
 * carro.c
 *
 *  Created on: Oct 23, 2023
 *      Author: damuj
 */

#include "carro.h"

double rps[2] = {0,0};
int pedal = 0;
int angulo = 0;

//


int getvelocidadIzquierda(){
	return rps[0];
}

int getvelocidadDerecha(){
	return rps[1];
}

void setvelocidadIzquierda(double vel){
	rps[0] = vel;
}

void setvelocidadDerecha(double vel){
	rps[1] = vel;
}

int getPedal(){
	return pedal;
}

void setPedal(int valor){
	pedal = valor;
}

int getAngulo(){
	return angulo;
}

void setAngulo(int ang){
	angulo =  ang;
}
