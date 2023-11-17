/*
 * diferencial.c
 *
 *  Created on: Oct 18, 2023
 *      Author: damuj
 */
#include "diferencial.h"
#include "../carro/carro.h"

int velocidad = 0;
int largo = 1000; // poner la distancia entre eje trasero y delenatero
int medio = 1000 ; // poner la distancia entre el eje y centro del carro vertical *1000 para evitar multiplicaciones
int m1, m2;


int caltan();
void calAngulo(){

	return;
}
void calVelcidad(){ // funcion para ligar la posicion del pedal a una velocidad, se tiene que ajustar despues
	int temporal= 0;
	int pedal = getPedal();
	temporal = ((pedal-1000)*1000)/2200;
	velocidad =  (temporal*5)/10;
}
void normalizacion();

void caldiff(){
	int radio, radio2,radio3;
	int di1,di2;
	if (getAngulo() != 0){
		radio = (caltan()*largo);
		radio2 = radio+medio;
		radio3 = radio-medio;

		di1 = (radio2*100)/radio;
		di2 = (radio3*100)/radio;
		if (getAngulo()>0){
			m1 = velocidad*di1/100;
			m2 = velocidad*di2/100;
			}
		else{
			m2 = velocidad*di1/100;
			m1 = velocidad*di2/100;
		}
	}
	else{
		m1 = velocidad;
		m2 = velocidad;
	}
	normalizacion();
}

int caltan(){
	int tabla[180] = {0, 17, 34, 52, 69, 87, 105, 122, 140, 158, 176, 194, 212, 230, 249,
			267, 286, 305, 324, 344, 363, 383, 404, 424, 445, 466, 487, 509, 531, 554,
			577, 600, 624, 649, 674, 700, 726, 753, 781, 809, 839, 869, 900, 932, 965,
			999, 1035, 1072, 1110, 1150, 1191, 1234, 1279, 1327, 1376, 1428, 1482, 1539,
			1600, 1664, 1732, 1804, 1880, 1962, 2050, 2144, 2246, 2355, 2475, 2605, 2747,
			2904, 3077, 3270, 3487, 3732, 4010, 4331, 4704, 5144, 5671, 6313, 7115, 8144, 9514,
			11430, 14300, 19081, 28636, 57289, 1, -57289, -28636, -19081,
			-14300, -11430, -9514, -8144, -7115, -6313, -5671, -5144, -4704, -4331, -4010, -3732,
			-3487, -3270, -3077, -2904, -2747, -2605, -2475, -2355, -2246, -2144, -2050, -1962,
			-1880, -1804, -1732, -1664, -1600, -1539, -1482, -1428, -1376, -1327, -1279, -1234,
			-1191, -1150, -1110, -1072, -1035, -1000, -965, -932, -900, -869, -839, -809, -781, -753,
			-726, -700, -674, -649, -624, -600, -577, -554, -531, -509, -487, -466, -445, -424, -404,
			-383, -363, -344, -324, -305, -286, -267, -249, -230, -212, -194, -176, -158, -140, -122,
			-105, -87, -69, -52, -34, -17 };

	int salida= 0;
	int an = 0;
	an = getAngulo();
	if (an <=0)an *=-1;
	salida = tabla[180-an];
	return salida;
}


void normalizacion(){

	setSalidaDerecha(m1*8);
	setSalidaIzquierda(m2*8);

}


