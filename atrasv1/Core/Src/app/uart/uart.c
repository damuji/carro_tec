/*
 * uart.c
 *
 *  Created on: Oct 18, 2023
 *      Author: damuj
 */
#include "uart.h"
#include "../carro/carro.h"


char anterior = 0;
char  sync = 0;
int merged = 0;
/*
 * modificar todo esto
 */
extern uint8_t data[10];
extern char cambio;


extern UART_HandleTypeDef huart4;
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
if (sync == 0){
	if (data[0] == 'o'){
		anterior = 'o';
	}
	if ((data[0] == 'k') && anterior == 'o' ){
		sync = 1;
		HAL_UART_Receive_IT(&huart4, data, 3);
	}
	else {
		anterior = 0;
		HAL_UART_Receive_IT(&huart4, data, 1);
	}

}
	else{
		merged = (data[1]<<8)+data[2];

		if (data[0]==1){
			setPedal((data[1]<<8)+data[2]);

		  }
		if(data[0]==2){
			cambio = data[2];

		}
		if (data[0]==3){
			setAngulo((data[1]<<8)+data[2]);
		}
		sync = 0;
		HAL_UART_Receive_IT(&huart4, data, 1);
	}
}

