#include "ADC.h"
#include "stm32f4xx_hal.h"

void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc){
	adc_val = HAL_ADC_GetValue(&hadc1);

	datos[0] = 1;
	datos[1] = (adc_val >> 8) ;
	datos[2] = adc_val ;
	datos[3] = 'o';
	datos[4] = 'k';
	HAL_UART_Transmit_IT(&huart4, datos,5);
}

