from django.db import models

class USER_DATA(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hospital = hosp[1],
	lat : float(hosp[0][11]),
	lng : float(hosp[0][12]),
	hospital_address : hosp[0][10],
	hospital_phone : hosp[0][8]
	wait_time :float(max_length=15)
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'USER_DATA',
            'USER': 'deanrexines',
            'PASSWORD': 'findmyhealth17',
            'HOST': 'findmyhealth-dev.elasticbeanstalk.com',
            'PORT': '3306',
        }
    }
