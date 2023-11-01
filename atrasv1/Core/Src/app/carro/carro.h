/*
 * carro.h
 *
 *  Created on: Oct 23, 2023
 *      Author: damuj
 */

#ifndef SRC_APP_CARRO_CARRO_H_
#define SRC_APP_CARRO_CARRO_H_


int getvelocidadIzquierda();
int getvelocidadDerecha();
void setvelocidadIzquierda(double vel);
void setvelocidadDerecha(double vel);
int getPedal();
void setPedal(int valor);
int getAngulo();
void setAngulo(int ang);

#endif /* SRC_APP_CARRO_CARRO_H_ */
