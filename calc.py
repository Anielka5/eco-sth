def metraz(size):
    return size/100
def result_calculate(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef
def feedback(calculated):
    if result < 50:
        score = f'Twój wynik: {{caculated}} kWh'
        wydajno = 'Twój dom jest wyjątkowo wydajny, jeśli chodzi o zużycie energii!'
    elif result > 70 and result <= 151:
        score = f'Twój wynik: {{caculated}} kWh'
        wydajno = 'Twój dom jest bardzo wydajny, jeśli chodzi o zużycie energii!'
    elif result >= 151 and result < 300:
        score = f'Twój wynik: {{caculated}} kWh'
        wydajno = 'Efektywność energetyczna Twojego domu jest średnia!'
    elif result >= 300:
        score = 'Twój wynik: {{result}} kWh'
        wydajno = 'Efektywność energetyczna Twojego domu jest poniżej średniej!'
    return score, wydajno
