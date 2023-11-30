/*
 * variables.c
 *
 *  Created on: Nov 15, 2023
 *      Author: damuj
 */

#include "variables.h"
#include "stm32f4xx_hal.h"

int pedal =0;
uint16_t angulo =0;
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
	angulo = (valor+ 796)/239;
}
int getAngulo(){
	return angulo;
}



void setVolante(int valor){
	if(valor>(volante+25))volante = valor;
	if(valor<(volante-25))volante = valor;
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


