# Task 1
import hashlib

class UserAccount:
    def __init__(self, username, email, password:str):
        self.__encrypted_password = hashlib.new("sha256")
        self.__encrypted_password.update(password.encode())

        self.__email = email
        self.__username = username

    def set_password(self, new_password):
        new_encrypted_password = hashlib.new("sha256")
        while True:
          psd_chk = hashlib.new("sha256")
          psd_chk.update(input().encode())

          if psd_chk.hexdigest() == self.__encrypted_password.hexdigest():
            new_encrypted_password.update(new_password.encode())
            self.__encrypted_password = new_encrypted_password
            print("Password changed successfully")
            break
          else:

            print("Wrong password ", psd_chk.hexdigest(), self.__encrypted_password.h)


    def check_password(self, password_to_check):
        chk = hashlib.new("sha256")
        chk.update(password_to_check.encode())

        if chk.hexdigest() == self.__encrypted_password.hexdigest():
            return True
        else:
            return False

# Task 2

class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_info(self):
        return f"{self._model} {self._make}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self._fuel_type = fuel_type

    def get_info(self):
        res = super().get_info()
        return res + f" {self._fuel_type}"