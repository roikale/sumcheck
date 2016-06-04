# sumcheck

This python script is a tool for finding duplicate files in your filesystem.
It can take quite a while to check a directory with lots of huge files, but this seems to be more bottlenecked by I/O than CPU power. MD5 and SHA1 are comparable in speed, SHA256 is quite a bit slower.

### Usage
To search for duplicate files in current directory:
`python sumcheck.py`

To search for duplicate files in /var/log, traversing all subdirectories:
`python sumcheck.py /var/log -r`


To search for duplicate files in ~/downloads, using md5:
`python sumcheck.py ~/Downloads --hash md5`

Sample output:
```
% sumcheck images --hash sha256
Indexing files, this may take a while...
21 files indexed out of 21    
 212865 	  images/2016-04-24--1461457586_1280x800_scrot.png
 212865 	  images/2016-04-24--1461457576_1280x800_scrot.png

 d8bbc2 	  images/2016-04-24--1461457592_1280x800_scrot.png
 d8bbc2 	  images/2016-04-24--1461457593_1280x800_scrot.png
 d8bbc2 	  images/2016-04-24--1461457595_1280x800_scrot.png

 7ef3c1 	  images/2016-04-24--1461457583_1280x800_scrot.png
 7ef3c1 	  images/2016-04-24--1461457584_1280x800_scrot.png
```
