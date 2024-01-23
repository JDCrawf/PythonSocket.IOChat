import tkinter as tk
from tkinter import scrolledtext
import json

widget = {}

# Initialize the root window
def init_root():
		_root = tk.Tk()
		#_root.geometry("600x500")
		_root.title("Python Chat App")
		_root.resizable(False, False)
		
		return _root

def build_menu(_frame):
	'''
		Builds and returns the menu bar for the application.
		The menu bar will contain basic controls/settings for the application.
		@param _frame: The root frame of the application.
		@return: The menu bar for the application.
	'''
	# These are all currently dummy menus
	# TODO: Change these to actual relevent menus
	_menu_frame = tk.Menu(_frame)
	file_menu = tk.Menu(_menu_frame, tearoff=0)
	file_menu.add_command(label="New")
	file_menu.add_command(label="Open")
	file_menu.add_command(label="Save")
	file_menu.add_command(label="Save as...")
	file_menu.add_command(label="Close")
	file_menu.add_separator()
	file_menu.add_command(label="Exit", command=root.quit)
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

def build_profile(_frame):
	'''
		Builds and returns the profile frame for the application.
		Profile information will be retrieved from a local file and displayed in the returned frame.
		This will display the profile information in the returned frame.
		@param _frame: The root frame of the application.
		@return: The profile frame for the application.	
	'''
	return tk.Frame(_frame, width=200, height=150, bd=4, relief=tk.SUNKEN) 

def build_server_view(_frame):
	'''
		Displays the status of the servers saved in the local file.
		This will display connection status, server name, and other serves information. 
		@param _frame: The root frame of the application.
		@return: The server view frame for the application.
	'''
	_server_list = tk.Frame(_frame, width=200, height=350, bd=4, relief=tk.SUNKEN)
	
	# 
	return _server_list

def build_chat_log(_frame):
	'''
		Builds and returns the chat log frame for the application.
		@param frame: The root frame of the application.
		@return: The chat log frame for the application.
	'''
	_chat_frame = tk.Frame(_frame, width=200, height=450)

	# Label to display current server's name
	server_label = tk.Label(_chat_frame, text="Server Name", width=10, anchor='w')
	server_label.grid(column=0, row=0, sticky='NEW')
	widget['server_name'] = server_label

	# Messages sent to/from the server
	# The state is set to DISABLED to prevent editing on the client side
	# When the server sends a message, it will need to be set to NORMAL, add the new message, then reset it to DISABLED
	chat_log= scrolledtext.ScrolledText(_chat_frame, width=50, height=28, state=tk.DISABLED)# height is in characters, not pixels -_-
	chat_log.grid(column=0, row=1, sticky='SEW')
	widget['chat_log'] = chat_log

	return _chat_frame

def build_text_entry(_frame):
	'''
		Builds and returns the text entry frame for the application.
		This will create a text entry frame for the chat log.
		After the send/Enter button is pressed, it will send the text entered to the server.
		@param _frame: The root frame of the application.
		@return: The text entry frame for the application.
	'''
	_text_entry = tk.Frame(_frame, width=400, height=20, bd=1, relief=tk.SUNKEN)
	
	# Label to display client's Username
	name_box = tk.Label(_text_entry, text="Username", width=10)
	name_box.grid(column=0, row=0, sticky='NSW')
	widget['username'] = name_box

	# Entry box to type message to send to server
	# This should take focus right after connecting to a server
	entry_box = tk.Entry(_text_entry, width=50)
	entry_box.grid(column=1, row=0, sticky='NS')

	# Button to send the message from the entry box to the server
	# Enter key should also send the message to the server
	send_button = tk.Button(_text_entry, text="Send")
	send_button.grid(column=2, row=0, sticky='NSE')
	return _text_entry

def build_window(_root):
	'''
		Builds and returns the root window for the application.
		This will create all the subframes for the application.
		@param _root: The root window for the application.
		@return: The root window with the GUI built for the application.
	'''
	menu_frame = build_menu(_root)
	_root.config(menu=menu_frame)
	
	# Create a container frame to hold the profile and the server view frames
	info_frame = tk.Frame(_root, width=200, bd=2, relief=tk.SUNKEN)
	info_frame.grid(row=0, column=0,sticky='NSW')
		
	# create a container frame to hold the chat menu and the text entry frames
	chat_frame = tk.Frame(_root, width=400, bd=2, relief=tk.SUNKEN)
	chat_frame.grid(row=0, column=1, sticky='NSE')
	
	# create a container frame to hold the profile information
	profile_frame = build_profile(info_frame)
	profile_frame.grid(row=0, column=0, sticky='NEW')
		
	# create a container frame to hold the server information
	server_frame = build_server_view(info_frame)
	server_frame.grid(row=1, column=0, sticky='SEW')
	
	chat_log_frame = build_chat_log(chat_frame)
	chat_log_frame.grid(row=0, column=0, sticky='NEW')

	text_entry_frame = build_text_entry(chat_frame)
	text_entry_frame.grid(row=1, column=0, sticky='SEW')

	return _root

# create the tkinter window
root = init_root()
build_window(root)

print(widget)
# main function
def main():
	root.mainloop()

if __name__ == '__main__':
		main()
