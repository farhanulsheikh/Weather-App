from django.shortcuts import render
import requests
import time
import json
from datetime import datetime, timedelta
import calendar
import os

# Create your views here.
# Home screen
def home (request):
    return render(request,'weather/home.html',{'title':'Home'})

# Make Api Call / Displays weather details
def weather_page(request):
    
    if request.method == "POST":
        city = request.POST['city']
        WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
        
        response = requests.get(url).json()
        if response['cod'] == 200:

                    context={
                        'temperature':int(response['main']['temp']),
                        'pressure':response['main']['pressure'],
                        'condition':response['weather'][0]['main'],
                        'code':str(response['weather'][0]['id']),
                        'name':response['name'],
                        'country':response['sys']['country'],
                        'description':response['weather'][0]['description'],
                        # if current time is between sunrise and sunset set daytime timecode else nighttime code
                        'timecode' : 'd' if time.gmtime(response['sys']['sunrise']) < time.gmtime() and time.gmtime(response['sys']['sunset']) > time.gmtime() else 'n',
                        
                        
                        
                    }


                    # day of the week
                    day2_day_of_the_week=calendar.day_name[(datetime.today()+timedelta(1)).weekday()]
                    day3_day_of_the_week=calendar.day_name[(datetime.today()+timedelta(2)).weekday()]
                    day4_day_of_the_week=calendar.day_name[(datetime.today()+timedelta(3)).weekday()]
                    


                    lat = str(response['coord']['lat'])
                    lon = str(response['coord']['lon'])
                    
                    url2=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,current,minutely,alerts&units=metric&appid={WEATHER_API_KEY}'
                    response2 = requests.get(url2).json()

                    context2={
                        # day_1 data
                        'day1_code':str(response2['daily'][1]['weather'][0]['id']),
                        'day1_description':str(response2['daily'][1]['weather'][0]['description']),
                        'day1_pop':str(round(float(response2['daily'][1]['pop'])*100,2)),
                        'day1_max':str(int(response2['daily'][1]['temp']['max'])),
                        'day1_min':str(int(response2['daily'][1]['temp']['min'])),
                        'day1_temperature':str(int(response2['daily'][1]['temp']['day'])),
                        # day_2 data
                        'day2_code':str(response2['daily'][2]['weather'][0]['id']),
                        'day2_description':str(response2['daily'][2]['weather'][0]['description']),
                        'day2_pop':str(round(float(response2['daily'][2]['pop'])*100,2)),
                        'day2_max':str(int(response2['daily'][2]['temp']['max'])),
                        'day2_min':str(int(response2['daily'][2]['temp']['min'])),
                        'day2_temperature':str(int(response2['daily'][2]['temp']['day'])),
                        'day2_name':day2_day_of_the_week,
                        # day_3 data
                        'day3_code':str(response2['daily'][3]['weather'][0]['id']),
                        'day3_description':str(response2['daily'][3]['weather'][0]['description']),
                        'day3_pop':str(round(float(response2['daily'][3]['pop'])*100,2)),
                        'day3_max':str(int(response2['daily'][3]['temp']['max'])),
                        'day3_min':str(int(response2['daily'][3]['temp']['min'])),
                        'day3_temperature':str(int(response2['daily'][3]['temp']['day'])),
                        'day3_name':day3_day_of_the_week,
                        # day_4 data
                        'day4_code':str(response2['daily'][4]['weather'][0]['id']),
                        'day4_description':str(response2['daily'][4]['weather'][0]['description']),
                        'day4_pop':str(round(float(response2['daily'][4]['pop'])*100,2)),
                        'day4_max':str(int(response2['daily'][4]['temp']['max'])),
                        'day4_min':str(int(response2['daily'][4]['temp']['min'])),
                        'day4_temperature':str(int(response2['daily'][4]['temp']['day'])),
                        'day4_name':day4_day_of_the_week,
                    }












                    r = json.loads(requests.get(url2).content)


                        ############# precipitaion amount for day 1 #############

                    if float(response2['daily'][1]['pop'])>0.15 :

                        #check if snow key exists
                        if 'snow' in r['daily'][1]:

                                if float(response2['daily'][1]['snow'])<1:
                                        context2['day1_precipitation']= "< 1"
                                else:
                                        context2['day1_precipitation']="~"+str(int(response2['daily'][1]['snow']))

                        # check if rain key exists    
                        elif 'rain' in r['daily'][1]:
                                if float(response2['daily'][1]['rain'])<1:
                                        context2['day1_precipitation']= "< 1"
                                else:
                                        context2['day1_precipitation']="~"+str(int(response2['daily'][1]['rain']))
                    else:
                                context2['day1_precipitation']=None
                        
                

                        ## ######### precipitaion amount for day 2 ##############

                    if float(response2['daily'][2]['pop'])>0.15 :

                        

                        #check if snow key exists
                        if 'snow' in r['daily'][2]:

                                if float(response2['daily'][2]['snow'])<1:
                                    context2['day2_precipitation']= "< 1"
                                else:
                                    context2['day2_precipitation']="~"+str(int(response2['daily'][2]['snow']))

                        # check if rain key exists    
                        elif 'rain' in r['daily'][2]:
                                if float(response2['daily'][2]['rain'])<1:
                                    context2['day2_precipitation']= "< 1"
                                else:
                                    context2['day2_precipitation']="~"+str(int(response2['daily'][2]['rain']))
                        else:
                                context2['day2_precipitation']=None
                            
                        ## ######### precipitaion amount for day 3 ##############

                    if float(response2['daily'][3]['pop'])>0.15 :

                        

                        #check if snow key exists
                        if 'snow' in r['daily'][3]:

                                if float(response2['daily'][3]['snow'])<1:
                                    context2['day3_precipitation']= "< 1"
                                else:
                                    context2['day3_precipitation']="~"+str(int(response2['daily'][3]['snow']))

                        # check if rain key exists    
                        elif 'rain' in r['daily'][3]:
                                if float(response2['daily'][3]['rain'])<1:
                                    context2['day3_precipitation']= "< 1"
                                else:
                                    context2['day3_precipitation']="~"+str(int(response2['daily'][3]['rain']))
                        else:
                                context2['day3_precipitation']=None
                            

                    ## ######### precipitaion amount for day 4 ##############

                    if float(response2['daily'][4]['pop'])>0.15 :

                        

                        #check if snow key exists
                        if 'snow' in r['daily'][4]:

                                if float(response2['daily'][4]['snow'])<1:
                                    context2['day4_precipitation']= "< 1"
                                else:
                                    context2['day4_precipitation']="~"+str(int(response2['daily'][4]['snow']))

                        # check if rain key exists    
                        elif 'rain' in r['daily'][4]:
                                if float(response2['daily'][4]['rain'])<1:
                                    context2['day4_precipitation']= "< 1"
                                else:
                                    context2['day4_precipitation']="~"+str(int(response2['daily'][4]['rain']))
                        else:
                                context2['day4_precipitation']=None
                            


                    return render(request,'weather/weather_page.html',{'title':'Weather','data':context,'data2':context2})

        else:
             return render(request,'weather/home.html',{'title':'Home', 'message':"city not found"})
        
    else:

        return render(request,'weather/home.html',{'title':'Home'})



        
    
    