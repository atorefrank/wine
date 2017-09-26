from django.forms import ModelForm, Textarea
from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'coffee_roast', 'chocolate_color', 'tart_creamy', 'fruit_pastry', 'herbaceous']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
        labels = {
            "coffee_roast": "Coffee Roast 1-light, 5-dark",
            "chocolate_color": "Chocolate 1-light, 5-dark",
            "tart_creamy": "lime-1 or banana/mango-2",
            "fruit_pastry": "Fruit salad-1 or Pastry-5",
            "herbaceous": "How much do you like smell of morning grass",
        }