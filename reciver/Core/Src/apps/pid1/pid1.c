/*
 * pid1.c
 *
 *  Created on: Nov 15, 2023
 *      Author: damuj
 */
#include "pid1.h"
#include "stm32f4xx_hal.h"
#include "../variables/variables.h"

extern TIM_HandleTypeDef htim1;
int kp  = 60;
int ofset =5;
int ofset2 =10;
int cache =0;
int total = 0;
int b = 0;
void mover();
void pid1(){
	//int error =0;
	//error = objetivo - getVolante();
	//proporcional = (error * kp)/1000;
	//integral = (error*25)/1000+integral;
	//deribativa = (antes-error)/25;
	//antes = error;
	//total =(integral*ki)/100 +  proporcional+(deribativa*kd)/100000;
//	if ((cache-total > 20)|(total -cache) <20){
//		total = cache;
//	}
//	else {
//		cache = total;
//	}
	b = getVolante();
	cache = ((getVolante()-1200)*100)/(2800-1200)-40;
	if ((cache >ofset2)||(cache <ofset2*-1)){
		total = (cache*kp/100);
	}
	else total =0;



	mover();
}
void mover(){

	if(total>=0){
		if(total>=100)total=100;
		TIM1->CCR1 = total+ofset;
		TIM1->CCR2 = 0;
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_2);
	}
	else if(total <=0){
		if(total<=-100)total=-100;
		TIM1->CCR1 = 0;
		TIM1->CCR2 = (total)*-1;
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_2);
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
	}
	else{
		TIM1->CCR1 =0;
		TIM1->CCR2 =0;
	}
}
