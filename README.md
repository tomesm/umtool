# umtool
Command line user management tool for linux/unix

## Usage

-U utility Password for changing/setting new password to Linux user.


-u uname Linux/unix user name for which password to be changed.


-x maxdays Maximum days for which user password is valid. Allowed values: '' OR number of days. For example: -x 99999 for never expiry


-E expiry Expire the password on setting when true and forcing the user to change password as part of the first login. Allowed values: true or false.



-G sec_group Linux secondary group to be added,comma(,) separated list,in case of multiple groups (eg gp1,gp2)



-s shell valid Linux/unix shell available (eg /usr/bin/bash)