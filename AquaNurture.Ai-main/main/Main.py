from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from home.Home_Screen import HomeScreen, NewEntryScreen
from signup.Signup_Screen import SignupScreen
from login.Login_Screen import LoginScreen
from kivy.uix.dropdown import DropDown
from kivy.uix.filechooser import FileChooserListView

class LoginSignupApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(SignupScreen())
        sm.add_widget(HomeScreen())
        sm.add_widget(NewEntryScreen())
        
        return sm


if __name__ == "__main__":
    LoginSignupApp().run()