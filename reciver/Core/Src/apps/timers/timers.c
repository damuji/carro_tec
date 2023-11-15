/*
 * timer.c
 *
 *  Created on: Oct 19, 2023
 *      Author: damuj
 */
#include "timers.h"
#include "../variables/variables.h"

extern TIM_HandleTypeDef htim10;
extern UART_HandleTypeDef huart4;
extern ADC_HandleTypeDef hadc1;
extern ADC_HandleTypeDef hadc2;


extern uint32_t valores[2];
char selecionado =0;
extern uint8_t datos[5];
extern char flag;
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim){ // completar
	if (htim == &htim10){
		setPedal(valores[1]);
		setVolante(valores[0]);




		if (flag){
		switch(selecionado){
		case 0:
			datos[0] = 0;
			datos[1] = (getPedal() >> 8) ;
			datos[2] = getPedal() ;
			datos[3] = 'o';
			datos[4] = 'k';
			selecionado = 1;
			break;
		case 1:
			datos[0] = 1;
			datos[1] = 0;
			datos[2] =  getCambio();
			datos[3] = 'o';
			datos[4] = 'k';
			selecionado = 2;
			break;
		case 2:
			datos[0] = 2;
			datos[1] = (getAngulo() >> 8);
			datos[2] =  getAngulo();
			datos[3] = 'o';
			datos[4] = 'k';
			selecionado = 0;
			break;
		}
		flag =0;
		//HAL_UART_Transmit_IT(&huart4, datos,5);

		}

		HAL_TIM_Base_Start_IT(&htim10);
		HAL_ADC_Start_IT(&hadc1);
		HAL_ADC_Start_IT(&hadc2);


	}


}




