/*
 * timers.h
 *
 *  Created on: Oct 19, 2023
 *      Author: damuj
 */

#ifndef SRC_APP_TIMERS_TIMERS_H_
#define SRC_APP_TIMERS_TIMERS_H_

#include "../diferencial/diferencial.h"
#include "stm32f4xx_hal.h"

//void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim);
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim);
#endif /* SRC_APP_TIMERS_TIMERS_H_ */
