# sumcheck

This python script is a tool for finding duplicate files in your filesystem.

## Usage
To search for duplicate files in current directory:
`python sumcheck.py`

To search for duplicate files in /var/log, traversing all subdirectories:
`python sumcheck.py /var/log -r`


To search for duplicate files in ~/downloads, using md5:
`python sumcheck.py ~/Downloads --hash md5`
