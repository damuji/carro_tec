/*
 * variables.c
 *
 *  Created on: Nov 15, 2023
 *      Author: damuj
 */

#include "variables.h"


int pedal =0;
int angulo =0;
int volante =0;
char cambio =0;

void setPedal(int valor){
	if(valor>(pedal+10))pedal = valor;
	if(valor<(pedal-10))pedal = valor;
}
int getPedal(){
	return pedal;
}



void setAngulo(int valor){
	angulo = 239*valor + 796;
}
int getAngulo(){
	return angulo;
}



void setVolante(int valor){
	volante = valor;
}
int getVolante(){
	return volante;
}


void setCambio(int valor){
	cambio = valor;
}
char getCambio(){
	return cambio;
}


