import random
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import PhotoImage
import json

class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Chat App - Client")
        self.root.resizable(False, False) # At least for now, i don't want to deal with resizing and weights yet

        # Important tkinter widgets
        self.username_label = None # Set this to whatever is saved in the JSON file
        self.server_name_label = None # Retrieve this from server
        self.chat_log = None # The server will send this to the client to be appended to the chat_log
        self.entry_box = None # The messages that the client sends to the server
        
        # Icons
        # refresh icon is from https://www.flaticon.com/packs/font-awesome by Dave Gandy
        # TODO: lets try and only use icons from the font-awesome library, also we need to update the README for icon attribution mentions
        self.refresh_icon = PhotoImage(file="img\\refresh.png")

        # Build the GUI
        self.build_window()

    def build_menu(self, frame):
        '''
            Builds and returns the menu bar for the application.
            The menu bar will contain basic controls/settings for the application.
            @param _frame: The root frame of the application.
            @return: The menu bar for the application.
        '''
        # These are all currently dummy menus
        # TODO: Change these to actual relevent menus
        _menu_frame = tk.Menu(frame)
        file_menu = tk.Menu(_menu_frame, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")
        file_menu.add_command(label="Close")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        _menu_frame.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(_menu_frame, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        edit_menu.add_command(label="Delete")
        edit_menu.add_command(label="Select All")
        _menu_frame.add_cascade(label="Edit", menu=edit_menu)
    
        help_menu = tk.Menu(_menu_frame, tearoff=0)
        help_menu.add_command(label="Help Index")
        help_menu.add_command(label="About...")
        _menu_frame.add_cascade(label="Help", menu=help_menu)

        return _menu_frame

    def build_server_info(self, frame):
        '''
            Builds and returns the server info frame for the application.
            Server information will be retrieved from the connected server and updated periodically
            @param _frame: The root frame of the application.
            @return: The profile frame for the application.	
        '''
        return tk.Frame(frame, width=200, height=150, bd=2, relief=tk.RAISED) 

    def build_server_view(self, frame):
        '''
            Displays the status of the servers saved in the local file.
            This will display connection status, server name, and other serves information. 
            @param _frame: The root frame of the application.
            @return: The server view frame for the application.
        '''
        _server_list = tk.Frame(frame, width=200, height=350)

        # Just a label so the user knows that this is a list of servers
        server_label = tk.Label(_server_list, text="Saved Servers", anchor='w', height=1)
        server_label.grid(column=0, row=0, sticky='NSW')
        
        # Refresh server list button
        server_refresh_button = tk.Button(_server_list, text="", image=self.refresh_icon)
        server_refresh_button.grid(column=1, row=0, sticky='NSEW', pady=2)

        # The list of servers with nested information
        server_list = ttk.Treeview(_server_list, columns=("Status"), show="tree")
        server_list.column("#0", width = 100)
        server_list.column("Status", width=100)

        
        server = server_list.insert("", 0, text="[Server Name]", value="Unknown")
        server_list.insert(server, 0, text="IP Address:", value="N/A")
        server_list.insert(server, 1, text="Users:", value="N/A")
        
        scrollbar = ttk.Scrollbar(_server_list, orient="vertical", command=server_list.yview)
        scrollbar.grid(column=1, row=1, sticky='NES')

        server_list.configure(yscrollcommand=scrollbar.set)

        server_list.grid(column=0, row=1, sticky='NSEW')
        return _server_list

    def build_chat_log(self, frame):
        '''
            Builds and returns the chat log frame for the application.
            @param frame: The root frame of the application.
            @return: The chat log frame for the application.
        '''
        _chat_frame = tk.Frame(frame, width=200, height=450)

        # Label to display current server's name
        # TODO: Replace "Server Name" string with variable call to retrieve the server name
        self.server_name_label = tk.Label(_chat_frame, text="[Server Name]", anchor='w')
        self.server_name_label.grid(column=0, row=0, sticky='NEW')

        # Messages sent to/from the server
        # The state is set to DISABLED to prevent editing on the client side
        # When the server sends a message, it will need to be set to NORMAL, add the new message, then reset it to DISABLED
        self.chat_log= scrolledtext.ScrolledText(_chat_frame, width=50, height=20, state=tk.DISABLED)# height is in characters, not pixels -_-
        self.chat_log.grid(column=0, row=1, sticky='SEW')

        return _chat_frame

    def build_text_entry(self, frame):
        '''
            Builds and returns the text entry frame for the application.
            This will create a text entry frame for the chat log.
            After the send/Enter button is pressed, it will send the text entered to the server.
            @param _frame: The root frame of the application.
            @return: The text entry frame for the application.
        '''
        _text_entry = tk.Frame(frame, width=400, height=20)
        
        # Label to display client's Username
        name_box = tk.Label(_text_entry, text="[Username]", width=10)
        name_box.grid(column=0, row=0, sticky='NSW')

        # Entry box to type message to send to server
        # This should take focus right after connecting to a server
        entry_box = tk.Entry(_text_entry, width=50)
        entry_box.grid(column=1, row=0, sticky='NS',pady=2)

        # Button to send the message from the entry box to the server
        # Enter key should also send the message to the server
        send_button = tk.Button(_text_entry, text="Send")
        send_button.grid(column=2, row=0, sticky='NSE', padx=4)
        return _text_entry

    def build_window(self):
        menu_bar = self.build_menu(self.root)
        self.root.config(menu=menu_bar)

        info_frame = tk.Frame(self.root, width=204, height=504, bd=2, relief=tk.SUNKEN)
        info_frame.grid(row=0, column=0, sticky='NSW')
        #info_frame.grid_propagate(False)

        chat_frame = tk.Frame(self.root, width=404, height=504, bd=2, relief=tk.SUNKEN)
        chat_frame.grid(row=0, column=1, sticky='NSE')
        #chat_frame.grid_propagate(False)

        profile_frame = self.build_server_info(info_frame)
        profile_frame.grid(row=0, column=0, sticky='NEW')

        server_frame = self.build_server_view(info_frame)
        server_frame.grid(row=1, column=0, sticky='SEW')

        chat_log_frame = self.build_chat_log(chat_frame)
        chat_log_frame.grid(row=0, column=0, sticky='NEW')

        text_entry_frame = self.build_text_entry(chat_frame)
        text_entry_frame.grid(row=1, column=0, sticky='SEW')

        self.root.mainloop()

if __name__ == '__main__':
    chat_app = ChatApp()
