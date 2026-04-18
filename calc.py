# Import
from flask import Flask, render_template, request


app = Flask(__name__)
def metraz(size):
    
def result_calculate(size, lights, device):
    # Zmienne umożliwiające obliczenie poboru energii przez urządzenia
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return float(size * home_coef + lights * light_coef + device * devices_coef)
{%if result < 50%}
        <img class="rez__img" src="../../static/img/planet_good.svg" alt="">
        <span>Twój wynik: {{result}} kWh</span>
        <span>Twój dom jest wyjątkowo wydajny, jeśli chodzi o zużycie energii!</span> 
        {%elif result > 70 and result <= 151%}
        <img class="rez__img" src="../../static/img/planet_good.svg" alt="">
        <span>Twój wynik: {{result}} kWh</span>
        <span>Twój dom jest bardzo wydajny, jeśli chodzi o zużycie energii!</span>
        {%elif result >= 151 and result < 300%}
        <img class="rez__img" src="../../static/img/planet_medium.svg" alt="">
        <span>Twój wynik: {{result}} kWh</span>
        <span>Efektywność energetyczna Twojego domu jest średnia!</span>
        
        <span>Chcesz uczynić świat bardziej ekologicznym miejscem? Wypełnij formularz, a my wykonamy dla Ciebie eko-build!</span>
        <a href="{{ url_for('form') }}" class = "main__link">Wypełnij formularz</a>
        {%elif result >= 300%}
        <img class="rez__img" src="../../static/img/planet_bad.svg" alt="">
        <span>Twój wynik: {{result}} kWh</span>
        <span>Efektywność energetyczna Twojego domu jest poniżej średniej!</span>
        <a href="{{ url_for('form') }}" class = "main__link">Wypełnij formularz</a>
# Pierwsza strona
@app.route('/')
def index():
    return render_template('index.html')
# Druga strona
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Trzecia strona
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Obliczenia
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(float(size),
                                                    float(lights), 
                                                    float(device)
                                                    )
                        )
# Formularz
@app.route('/form')
def form():
    return render_template('form.html')

# Wyniki formularza
@app.route('/submit', methods=['POST'])
def submit_form():
    # Zadeklaruj zmienne do gromadzenia danych
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    with open('form.txt', 'a',) as f:
        f.write(name + '\n')
        f.write(email + '\n')
        f.write(address + '\n')
        f.write(date + '\n')
        
    # Możesz zapisać swoje dane lub wysłać je e-mailem
    return render_template('form-result.html', 
                           # Umieść tutaj zmienne
                           name=name,
                           email=email,
                           address = address,
                           date = date,
                           )

app.run(debug=True)

#JSON
# {
#     "name": "Jan",
#     "email": "przyklad@gmail.com",
#     "date": "2024-06-15",
#     "address": " ul przykładowa 12, 00-000 Miasto"
# }
