from tortoise import Model, fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=200, null=False)
    is_verified = fields.BooleanField(default=False)
    date_created = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'users'

    def __str__(self):
        return f'{self.username}-{self.email}'


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=50, null=False, unique=True)
    city = fields.CharField(max_length=100, null=False, default='')
    country = fields.CharField(max_length=100, null=False, default='')
    description = fields.TextField(default='')
    logo = fields.CharField(max_length=255, null=False, default='default.jpg')
    owner = fields.ForeignKeyField(User,on_delete=fields.SET_NULL,null=True, related_name='business')
    date_created = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'businesses'

    def __str__(self):
        return f'{self.business_name}'


class Product(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=100, null=False, index=True)
    category = fields.CharField(max_length=100, index=True)
    unit_cost = fields.DecimalField(max_digits=19,decimal_places=2,default=0.00)
    retail_price = fields.DecimalField(max_digits=19,decimal_places=2,default=0.00)
    discount_percentage = fields.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    offer_expired_on = fields.DateField(null=True)
    image = fields.CharField(max_length=255,null=False,default='product.jpg')
    business = fields.ForeignKeyField(Business,on_delete=fields.SET_NULL,null=True,related_name='products')
    date_created = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'products'

    def __str__(self):
        return f'{self.name}-{self.retail_price}'
    
    
user_pydantic = pydantic_model_creator(User,name='User',exclude=('is_verified',))
user_pydantic_in = pydantic_model_creator(User,name='UserIn',exclude_readonly=True)