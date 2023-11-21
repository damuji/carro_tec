/*
 * timer.c
 *
 *  Created on: Oct 19, 2023
 *      Author: damuj
 */
#include "timers.h"
#include "../variables/variables.h"

extern TIM_HandleTypeDef htim10;
extern UART_HandleTypeDef huart2;
extern ADC_HandleTypeDef hadc1;
extern ADC_HandleTypeDef hadc2;


extern uint32_t valores[2];
char ciclo=0;
int temporal = 0;
extern uint8_t datoss[10];
extern char flag;
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim){ // completar
	pid1();
	if (htim == &htim10){
		if((ciclo>=2) && flag){
			temporal = getPedal();
			datoss[0]=(temporal/1000)+48;
			temporal = temporal%1000;

			datoss[1]=(temporal/100)+48;
			temporal = temporal%100;

			datoss[2]=temporal/10+48;
			temporal = temporal%10;

			datoss[3]=temporal+48;

			datoss[4]=13;
			datoss[5]=10;
			ciclo =0;
			HAL_UART_Transmit_IT(&huart2, datoss,6);

		}
		else ciclo++;

		HAL_TIM_Base_Start_IT(&htim10);
		HAL_ADC_Start_IT(&hadc1);
		HAL_ADC_Start_IT(&hadc2);


	}


}




