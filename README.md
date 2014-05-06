py3mail
=======

A plugin to py3status which displays the number of unread mail messages in a gmail inbox on your i3bar.



INSTALL
=======

To install this module, simply call py3status as follows: py3status -i ~/path/to/py3mail.py  (For me, py3mail only works if py3mail.py is in my home directory)
Make sure to add your Gmail username and password or your microsoft account email address (The full address you use to login to outlook.com) and password (in plain text) to py3mail.conf. 
You must also add the service you wish to use right below your password. Your options are "gmail" or "hotmail" for Google mail, and any Microsoft account.

You can create py3mail.conf if there is not already one present.

py3mail.conf should be in the same directory as py3mail.py and should contain only your username, password and service in the following format:

username
password
service

Examples are given in py3mail.conf.example.


Contact:

Sam Barratt - samuel@sbarratt.co.uk
