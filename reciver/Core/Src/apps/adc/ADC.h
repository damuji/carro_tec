/*
 * ADC.h
 *
 *  Created on: Oct 16, 2023
 *      Author: damuj
 */

#ifndef APPS_ADC_H_
#define APPS_ADC_H_
#include "stm32f4xx_hal.h"

void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc);

#endif /* APPS_ADC_H_ */
