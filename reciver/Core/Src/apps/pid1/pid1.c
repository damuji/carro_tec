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
int kp=65;
int ki=5;
int kd=0;
int integral =0;
int deribativa =0;
int proporcional=0;
int objetivo =1300;
int milis = 25;
int total =0;
int antes=0;
void mover();
void pid1(){
	int error =0;
	error = objetivo - getVolante();
	proporcional = (error * kp)/1000;
	integral = (error*25)+integral;
	diferencial = (antes-error)/25;
	antes = error;
	total =(integral*ki)/100000    +  proporcional;
	mover();
}
void mover(){

	if(total>=0){
		if(total>=100)total=100;
		TIM1->CCR1 = total;
		TIM1->CCR2 = 0;
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_2);
	}
	else if(total <=0){
		if(total<=-100)total=-100;
		TIM1->CCR1 = 0;
		TIM1->CCR2 = total*-1;
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_2);
		HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_1);
	}
	else{
		TIM1->CCR1 =0;
		TIM1->CCR2 =0;
	}
}
