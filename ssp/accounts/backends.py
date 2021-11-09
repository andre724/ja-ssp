from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from accounts.models import SSPUser

class SSPUserBackends(BaseBackend):

    def authenticate(self,request, email=None, password=None):
        if email and password is None:
            return None

        if email is not None:
            try:
                ssp_user= SSPUser.objects.get(email=email)
                
            except SSPUser.DoesNotExist:
                return None
            else:
                if ssp_user.check_password(password) is True:
                    return ssp_user
            
    def get_user(self, user_id):
        try:
            user = SSPUser._default_manager.get(pk=user_id)
        except SSPUser.DoesNotExist:
            return None
        return user 