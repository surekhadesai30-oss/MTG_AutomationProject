from faker import Faker
import random
import string
class RandomDataUtills:
    def __init__(self):
        self.fake = Faker()

    def get_random_email_id(self)->str:
        return self.fake.email()

    def get_random_pwd(self,length: int=10)->str:
        return self.fake.password(length=length)

    def get_random_phoneNumber(self)->str:
        return self.fake.phone_number()

    def get_random_alphnumeric(self,length:int=10)->str:
        chars= string.ascii_letters+string.digits
        return ''.join(random.choice(chars) for _ in range(length))





