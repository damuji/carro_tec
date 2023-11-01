/*
 * diferencial.c
 *
 *  Created on: Oct 18, 2023
 *      Author: damuj
 */
#include "diferencial.h"
#include "../carro/carro.h"

int velocidad = 0;
int largo = 0; // poner la distancia entre eje trasero y delenatero
int medio = 0; // poner la distancia entre el eje y centro del carro vertical

void calAngulo(){

	return;
}
void calVelcidad(){ // funcion para ligar la posicion del pedal a una velocidad, se tiene que ajustar despues
	int temporal= 0;
	int pedal = getPedal();
	temporal = (pedal*1000)/4095;
	velocidad =  (temporal*4);
}

int caldiff(){
	float radio, radio2 ;
	radio = caltaninv()*largo
	radio2 = radio+medio;
	return 0;
}

int caltaninv(){


	return 0;
}

int calcos(){
	return 0;
}

