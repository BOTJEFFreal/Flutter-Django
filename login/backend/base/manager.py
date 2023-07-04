from django.contrib.auth.base_user import BaseUserManager

class UserNamager(BaseUserManager):
    def create_user(self,
                    # username,
                    school_id,password = None,**extra_fields):
        if not school_id : #username:
            raise ValueError("SchoolId and/or Username is missing")
        
        user = self.model(
            # username = username, 
            school_id = school_id,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user

    def create_superuser(self,
                        #  username,
                         school_id,password = None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(
            # username,
            school_id,password,**extra_fields)
    
