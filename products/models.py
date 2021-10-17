from django.db import models

from django.contrib.auth.models import User


ATTITUDE_CHOICES = [
    ('POS', 'Positive'),
    ('NEG', 'Negative')
]

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    
    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    @classmethod
    def get_dict(cls):
        def f(category, category_dict={}):
            category_dict[category] = {}
            
            for c in category.children.all():
                category_dict[category] = f(c, category_dict[category])
            return category_dict

        categories = cls.objects.filter(parent=None)
        d = {}
        for category_parent in categories:
            d[category_parent] = f(category_parent)
        return d

class CategoryTemplate(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    for_filter = models.BooleanField(default=False)
    
    def __str__(self):
        return self.field_name


class CategoryFilterValue(models.Model):
    category_filter = models.ForeignKey(CategoryTemplate, on_delete=models.CASCADE)
    field_value = models.CharField(max_length=100)

    def __str__(self):
        return self.field_value


class Product(models.Model):
    release_date = models.DateField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='images/')

class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    field_value = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        
        category_template_filter = CategoryTemplate.objects.filter(field_name=self.field_name)
        category_template = category_template_filter[0] if category_template_filter else []
        
        if category_template and category_template.for_filter:
            # try:
            print(not CategoryFilterValue.objects.filter(field_value=self.field_value), self.field_value)
            if not CategoryFilterValue.objects.filter(field_value=self.field_value) \
            and self.field_value:
                CategoryFilterValue(category_filter=category_template, field_value=self.field_value).save()
            # except 
            

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    pfp = models.ImageField(upload_to="pfps/")

class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    datetime = models.DateTimeField()
    attitude = models.CharField(choices=ATTITUDE_CHOICES, max_length=10, default=ATTITUDE_CHOICES[0][0])