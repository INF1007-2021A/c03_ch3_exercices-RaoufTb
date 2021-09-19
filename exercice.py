#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
p = math.pi


def average(a: float, b: float, c: float) -> float:
    result= (a+b+c)/3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    result = round((angle_degs + angle_mins/60 + angle_secs/3600) * p/180, 2)
    return result


def to_degrees(angle_rads: float) -> tuple:
    result_degre = (angle_rads * 180/p)
    result_minutes = (result_degre % 1) * 60
    result_secondes = (result_minutes % 1 ) * 60
    return int(result_degre), int(result_minutes) , int(result_secondes)
    
    #int(((angle_rads * 180/3.14159265)-int(angle_rads * 180/3.14159265))*60), 
    #int(((((angle_rads * 180/3.14159265)-int(angle_rads * 180/3.14159265))*60) - int(((angle_rads * 180/3.14159265)-int(angle_rads * 180/3.14159265))*60))*60)


def to_celsius(temperature: float) -> float:
    result = round((temperature -32 ) / 1.8, 2)
    return result


def to_farenheit(temperature: float) -> float:
    result = (temperature * 1.8 ) + 32
    return result


def main() -> None:
    print(f"Moyenne des nombres 2.1, 4.3, 6.5: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()