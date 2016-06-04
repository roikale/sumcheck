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
