from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CircularMaskImage(BoxLayout):
    pass

class NewEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'new_entry_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Add a BoxLayout to hold text input fields dynamically
        self.text_input_layout = BoxLayout(orientation='vertical', spacing=10)
        self.add_widget(self.text_input_layout)

        # Add an initial text input for "Tank ID"
        self.add_text_input("Tank ID")

        # Add an empty widget for spacing
        self.add_widget(Label(size_hint_y=None, height=20))

        # Add a submit button
        submit_button = Button(text='Submit', size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        submit_button.bind(on_press=self.submit_form)
        self.add_widget(submit_button)

    def add_text_input(self, label_text):
        # Helper method to add a new text input field
        label = Label(text=label_text, halign='center')
        text_input = TextInput(multiline=False, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        self.text_input_layout.add_widget(label)
        self.text_input_layout.add_widget(text_input)

    def submit_form(self, instance):
        # Add functionality to handle form submission (e.g., save data)
        # Access entered data from each text input field in the layout
        for i in range(0, len(self.text_input_layout.children), 2):
            label = self.text_input_layout.children[i]
            text_input = self.text_input_layout.children[i + 1]
            print(f"{label.text}: {text_input.text}")





        

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home_screen'
        self.orientation = "vertical"
        self.spacing = 15
        self.padding = [50, 0]  # Adjusting top padding to move the content to the center

        # Adding background image for the home screen
        self.background = Image(source="home_image.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.add_widget(self.background)

        # Logo and Logout button layout
        top_layout2 = BoxLayout(orientation='horizontal', size_hint=(None, None), height=40,
                               pos_hint={'top': 0.93, 'left': 0.98})

        top_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), height=40,
                              pos_hint={'top': 0.85, 'left': 0.98})

        top_layout1 = BoxLayout(orientation='horizontal', size_hint=(None, None), height=40,
                                pos_hint={'top': 0.95, 'right': 1})

        # Add the circular logo image to the top-left corner
        logo = CircularMaskImage(size_hint=(None, None), size=(70, 70))
        logo.add_widget(AsyncImage(source="logo.png", size=(80, 80), allow_stretch=True))
        top_layout2.add_widget(logo)

        # Add a hamburger menu toggle button with an image
        hamburger_button = Button(size_hint=(None, None), size=(40, 40), background_normal="togglebar.PNG")
        hamburger_button.bind(on_press=self.toggle_menu)
        top_layout.add_widget(hamburger_button)

        # Add a logout button to the top-right corner
        self.logout_button = Button(text="Logout", size_hint=(None, None), size=(70, 40))
        top_layout1.add_widget(self.logout_button)
        self.logout_button.bind(on_press=self.go_to_login)

        self.add_widget(top_layout)
        self.add_widget(top_layout1)
        self.add_widget(top_layout2)

        # Create a BoxLayout for the menu items (initially hidden)
        self.menu_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(200, 120),
                                     pos_hint={'center_x': 0.1, 'center_y': 0.68})
        self.menu_layout.opacity = 0  # Initially hidden

        # Add menu items
        home_menu_button = Button(text="Home", size_hint_y=None, height=40)
        home_menu_button.bind(on_press=self.on_menu_button_press)
        self.menu_layout.add_widget(home_menu_button)

        contact_menu_button = Button(text="Contact", size_hint_y=None, height=40)
        contact_menu_button.bind(on_press=self.on_menu_button_press)
        self.menu_layout.add_widget(contact_menu_button)

        help_menu_button = Button(text="Help", size_hint_y=None, height=40)
        help_menu_button.bind(on_press=self.on_menu_button_press)
        self.menu_layout.add_widget(help_menu_button)

        self.add_widget(self.menu_layout)

        # Central transparent square box with a plus button
        center_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(200, 200),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})

        with center_layout.canvas.before:
            Color(0, 0, 0, 0.5)  # Transparent black color
            Rectangle(pos=center_layout.pos, size=center_layout.size)

        plus_button = Button(text="+", size_hint=(None, None), size=(50, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        plus_button.bind(on_press=self.on_plus_button_press)

        center_layout.add_widget(plus_button)
        self.add_widget(center_layout)

    def toggle_menu(self, instance):
        # Toggle the visibility of the menu
        if self.menu_layout.opacity == 0:
            self.menu_layout.opacity = 1
            self.menu_layout.size_hint_x = 0.2  # Adjust the width as needed
            self.menu_layout.pos_hint = {'center_x': 0.1, 'center_y': 0.68}
        else:
            self.menu_layout.opacity = 0
            self.menu_layout.size_hint_x = None
            self.menu_layout.width = 0

    def on_menu_button_press(self, instance):
        # Handle menu item press (add functionality here)
        self.manager.current = 'home_screen'

    def go_to_login(self, instance):
        self.manager.current = 'login_screen'

    def on_plus_button_press(self, instance):
        # Handle the plus button press by switching to the NewEntryScreen
        self.manager.current = 'new_entry_screen'