from django.db import models
from django.conf import settings
import secrets
from .paystack import PayStack

patrols = (
    ('Adaka MP', 'Adaka MP'),
    ('Aso MP', 'Aso MP'),
    ('Baglina MP', 'Baglina MP'),  
)

designations = (
    ('Skull','Skull'),
    ('BOT','BOT'),
    ('Dechand', 'Deckhand'),
)

drugs = (
    ('No','No'),
    ('Yes','Yes'),
)

food = (
    ('Rice with Assorted Protein','Rice with Assorted Protein'),
    ('Swallow with assorted protein','Swallow with assorted protein'),
)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True)
    norsical = models.CharField(max_length=200, null=True)
    patrol=models.CharField(max_length=200,null=False,choices=patrols)
    designation=models.CharField(max_length=200,null=False,choices=designations)
    Do_You_Use_Hard_Drugs=models.CharField(max_length=200,null=False,choices=drugs)
    Which_Is_Your_Preferred_Meal_For_the_Convaj_Dinner_Your_Choice_Will_Be_Indicated_on_Your_Meal_Ticket=models.CharField(max_length=200,null=False,choices=food, default="")
    passport = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Payment(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    verified=models.BooleanField(default=False)
    ref=models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return f"Payment by :{self.email}"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref =ref
        super().save(*args, **kwargs)

    def amount_value(self) -> int:
        return self.amount * 100
            
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
            if self.verified:
                return True
            return False

