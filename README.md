Bitmessage Trash
=========

This is a simple program written in Python to remove and read messages from the trash

  - You can read messages from the trash
  - You can completely delete messages from trash
  - You can recover (export) trashed messages to text files
  - You can move trashed messages back to inbox
  - This is a version written in one night, anyone can add or change something, just let me know about changes, maybe I'll like :)


What inspired me to create this program? 
No trash and message file occupies _more space_ on disk!

> du -sh messages.dat

> 112M  messages.dat

PyBitmessage has no option for trash management, so when you accidentally move a message to trash, it is effectively lost. With Bitmessage Trash you can re-read and recover those messages.

Version
-

0.03
 - Undeleting messages

0.02
 - Exporting messages

0.01.1
 - External `messages.dat` support

0.01
 - Reading trash
 - purging trash

Installation
--------------

    $ git clone https://github.com/modInfo/Bitmessage-Trash ~/Bitmessage-Trash
    $ mv ~/Bitmessage-Trash/* ~/.PyBitmessage/
    $ cd ~/.PyBitmessage
    $ python2 trash.py

You can now also specify the messages.dat path:

    $ python2 trash.py /path/to/messages.dat

License
-

MIT

*Free Software, Fuck Yeah!*

  

    
