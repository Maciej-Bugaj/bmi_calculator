print('KALKULATOR BMI')
bmi = 0

try:
    weight = input('Podaj swoją wagę (kg):  ')
    height = input('Podaj swój wzrost (m): ')
    weight = int(weight)
    height = float(height)
    bmi = weight/(height**2)

    if bmi < 16:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza wygłodzenie')
        
    elif bmi > 16 and bmi < 16.99:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza wychudzenie')

    elif bmi > 17 and bmi < 18.49:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza wychudzenie')

    elif bmi > 18.5 and bmi < 24.99:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza wartość prawidłową')

    elif bmi > 25 and bmi < 29.99:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza nadwagę')

    elif bmi > 30 and bmi < 34.99:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza I stopień otyłości')

    elif bmi > 35 and bmi < 39.99:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza II stopień otyłości')
        
    else:
        print('Twoje bmi to: ',round(bmi,2))
        print('Ten poziom BMI oznacza skrajną otyłość')


except ValueError:
    print('Podane wartości są nieprawidłowe!')

except ZeroDivisionError:
    print('Podane wartości nie mogą być mniejsze lub równe 0!')


input('Naciśnij ENTER aby zakończyć')
    

