# OPNSense-Backup

Quick python script hacked together to allow automation of OPNSense backups.

1. Install the os-api-backup plugin if it isn't already installed.

2. You'll want to create a group with limited permissions.  In the OPNsense WebUI, go to System -> Access -> Groups and add a new group (I called mine backup).  Save the group, then edit it.  On the edit screen, under Assigned Privileges, click the edit button, find "Backup API" in the list, and check it.  Leave everything else unchecked and click Save.  Click Save again to return to the Groups screen.

3. Create a user in that group.  Go to System -> Access -> Users and add a new user (I called mine, creatively enough, backup_user).  I generated a long random password using my password manager, and then discarded it--this user will never log in using that password.  Add the user to the backup group and save.  Then edit the user, find the API keys heading, and click + to create a new one.  This will download a small text file containing an API key and a secret, save it someplace convenient.  Click Save to return to the users screen.
