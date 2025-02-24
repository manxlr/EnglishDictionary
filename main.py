import dearpygui.dearpygui as dpg
import sqlite3
import threading

class DictionaryApp:
    def __init__(self):
        # SQLite connection with thread safety
        self.conn = sqlite3.connect("dictionary.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()  # Thread lock for safe database access
        
        # Setup Dear PyGui
        dpg.create_context()
        dpg.create_viewport(title="Modern English Dictionary", width=900, height=600)
        
        # Modern theme
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (40, 40, 40), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (50, 100, 200), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (70, 120, 220), category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 10)
        
        dpg.bind_theme(global_theme)
        
        # Main window
        with dpg.window(label="English Dictionary", tag="primary_window", no_close=True):
            dpg.add_text("English Dictionary", color=(255, 255, 255))
            dpg.add_separator()
            
            # Search input and buttons
            with dpg.group(horizontal=True):
                dpg.add_input_text(hint="Enter a word...", width=400, callback=self.search_word_on_enter, tag="search_input")
                dpg.add_button(label="Search", width=120, callback=self.search_word)
                dpg.add_button(label="Show All", width=120, callback=self.show_all_words)
            
            # Results display (copyable)
            dpg.add_text("Results:", color=(200, 200, 200))
            with dpg.child_window(height=-1, autosize_x=True, border=True, tag="results_window"):
                dpg.add_input_text(
                    default_value="",
                    multiline=True,
                    width=-1,
                    height=-1,
                    tag="results_text",
                    readonly=True  # Prevents editing but allows copying
                )
        
        # Initial display
        self.show_all_words()
        
        # Finalize setup
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def search_word_on_enter(self, sender, app_data):
        self.search_word(sender, app_data)
    
    def search_word(self, sender, app_data):
        search_term = dpg.get_value("search_input").strip().lower()
        if not search_term:
            dpg.set_value("results_text", "Please enter a word to search!")
            return
        
        with self.lock:  # Thread-safe database access
            self.cursor.execute(
                "SELECT word, wordtype, definition FROM entries WHERE word = ?",
                (search_term,)
            )
            result = self.cursor.fetchone()
        
        if result:
            word, wordtype, definition = result
            display_text = f"Word: {word}\nType: {wordtype}\nDefinition: {definition}"
            dpg.set_value("results_text", display_text)
        else:
            dpg.set_value("results_text", f"No definition found for '{search_term}'")
    
    def show_all_words(self, sender=None, app_data=None):
        with self.lock:  # Thread-safe database access
            self.cursor.execute("SELECT word, wordtype, definition FROM entries ORDER BY word")
            words = self.cursor.fetchall()
        
        display_text = []
        for word, wordtype, definition in words:
            display_text.append(f"Word: {word}\nType: {wordtype}\nDefinition: {definition}\n{'-'*50}")
        
        dpg.set_value("results_text", "\n".join(display_text) if display_text else "No entries found.")
    
    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    app = DictionaryApp()