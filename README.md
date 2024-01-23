# Python Chat App

This is a simple chat application built using Python, Socket.IO, and Tkinter. It allows users to connect to a chat room and exchange messages in real-time.

## Features    

- Real-time messaging using Socket.IO
- User-friendly graphical interface with Tkinter
- Customizable and easy-to-use chat room functionality

### Client Features
- Save profile/application information
	- Username
	- Message Color
	- Prefered Font
  	- Themes
	- etc...
- Save servers for quick access
- Send/Recieve messages with whichever server you connected to

### Server Features
- View messages being sent through your server
- Set Server information
  	- Server Name
  	- Join Message
  	- Message of the Day
  	- etc...
- Send server notices to all connected clients
- Remove/Edit messages sent by clients(will contain notifier that message was edited by server)
- Disconnect/Block troublemaking clients

## Requirements

Make sure you have the following dependencies installed before running the application:
- Python 3.x
- socketio library (install using `pip install python-socketio`)
- tkinter library (install using `pip install tk`)

## Usage
1. Clone the repository:

	```bash
	git clone https://github.com/JDCrawf/PythonSocket.IOChat.git
	```

2. Navigate to the project directory:

	```bash
	cd python-chat-app
	```

### For Server Host
3. Run the application:

	```bash
 	py server.py
 	```

4. The Server app window will open.
	- If this is your first time launching the app, it will ask you to enter a Port number

5. Clients can now connect to your chat server through your IP and Port

### For Clients
3. Run the application:

	```bash
	py client.py
	```

4. The Chat app window will open.
	- If this is your first time launching the app, it will ask you to enter a username which can be changed at any time

5. Connect to a sever by IP or by selecting a saved server from the Server Menu

6. Start chatting with other users in real-time!

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome and accepted push requests will get your name added to this list!

Jacob Crawford - [@JDCrawf](https://github.com/JDCrawf)

##  License

- This project is licensed under the [MIT License](LICENSE).
- Tkinter: Python Software Foundation License (included with Python installations).
- Socket.IO: MIT License. See [Socket.IO License](https://github.com/miguelgrinberg/python-socketio/blob/main/LICENSE) for details.

## Acknowledgments

- Thanks to the Socket.IO and Tkinter communities for providing excellent libraries and resources.

Happy chatting! 🎉
