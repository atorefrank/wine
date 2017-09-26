from django.db import models
from django.contrib.auth.models import User
import numpy as np
import json

class Wine(models.Model):
    name = models.CharField(max_length=200)
    
    def average_rating(self):
        all_ratings = list(map(lambda x: x.getrating(), self.review_set.all()))
        a = np.array(all_ratings)
        return np.mean(a, axis=0)
        
    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    coffee_roast = models.IntegerField(choices=RATING_CHOICES)
    chocolate_color = models.IntegerField(choices=RATING_CHOICES)
    tart_creamy = models.IntegerField(choices=RATING_CHOICES)
    fruit_pastry = models.IntegerField(choices=RATING_CHOICES)
    herbaceous = models.IntegerField(choices=RATING_CHOICES)
    rating = models.CharField(max_length=200)

    def setrating(self, x):
        self.rating = json.dumps(x)

    # setrating({'coffee_roast':coffee_roast, 'chocolate_color': chocolate_color, 'tart_creamy':tart_creamy, 'fruit_pastry':fruit_pastry, 'herbaceous':herbaceous})

    def getrating(self):
    	result = json.loads(self.rating)
    	return list(result.values())

    # def rating(self):
    # 	results = []
    # 	results.append(self.coffee_roast)
    # 	results.append(self.chocolate_color)
    # 	results.append(self.tart_creamy)
    # 	results.append(self.fruit_pastry)
    # 	results.append(self.herbaceous)
    # 	# "%s/%s" %(self.coffee_roast, self.chocolate_color, self.tart_creamy, self.fruit_pastry, self.herbaceous
    # 	return results

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])