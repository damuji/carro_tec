/*
 * uart.h
 *
 *  Created on: Oct 18, 2023
 *      Author: damuj
 */

#ifndef SRC_APP_UART_UART_H_
#define SRC_APP_UART_UART_H_
#include "stm32f4xx_hal.h"
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart);

#endif /* SRC_APP_UART_UART_H_ */
