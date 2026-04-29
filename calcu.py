def metraz(size):
    return size/100
def result(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef
def feedback(calculated):
    score = 'Twój wynik:',  calculated ,'kWh'
    if calculated < 50:
        wydajno = 'Twój dom jest wyjątkowo wydajny, jeśli chodzi o zużycie energii!'
    elif calculated > 70 and calculated <= 151:
        wydajno = 'Twój dom jest bardzo wydajny, jeśli chodzi o zużycie energii!'
    elif calculated >= 151 and calculated < 300:
        wydajno = f'Efektywność energetyczna Twojego domu jest średnia!'
    elif calculated >= 300:
        wydajno = 'Efektywność energetyczna Twojego domu jest poniżej średniej!'
    return score, wydajno
