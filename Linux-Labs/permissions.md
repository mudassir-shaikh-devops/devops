Linux File Permissions

1. Permission types:
- r = read
- w = write
- x = execute

2. Levels:
- Owner
- Group
- Others

3. Commands:
- ls -l → show permissions
- chmod 777 file → full access
- chmod 755 file → safe permission
- chown user:group file → change owner

4. Example:
-rwxr-xr-- means:
Owner → full
Group → read + execute
Others → read only