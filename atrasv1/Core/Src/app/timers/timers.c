/*
 * timer.c
 *
 *  Created on: Oct 19, 2023
 *      Author: damuj
 */
#include "timers.h"
#include "../carro/carro.h"
#include "../diferencial/diferencial.h"
extern TIM_HandleTypeDef htim10;
extern DAC_HandleTypeDef hdac;
int timepoAnterior[2] = {0,0};
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim){ // completar
	if (htim == &htim10){

		calVelcidad(); // se calcula la velocdiad deseada
		calDiff(); // se calcula la


		// Calcular PID
		HAL_DAC_SetValue(&hdac, DAC_CHANNEL_1, DAC_ALIGN_12B_R, 0);
		HAL_DAC_SetValue(&hdac, DAC_CHANNEL_2, DAC_ALIGN_12B_R, 0);
		// Aplicar PID

		// se reiniica el timer
		HAL_TIM_Base_Start_IT(&htim10);

	}

}
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim){ // tomando 28 pulsos por revolicion
	int tiempo = 0;
	int lapso = 0;
	if (htim->Channel == HAL_TIM_ACTIVE_CHANNEL_3){
		tiempo = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_3);
		lapso  = tiempo - timepoAnterior[0];
		timepoAnterior[0] = tiempo;
		setvelocidadIzquierda(lapso/28);

	}
	if (htim->Channel == HAL_TIM_ACTIVE_CHANNEL_4){
		tiempo = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_4);
		lapso  = tiempo - timepoAnterior[0];
		timepoAnterior[0] = tiempo;
		setvelocidadDerecha(lapso/28);
		}
}


