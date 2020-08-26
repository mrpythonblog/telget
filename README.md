# TELGET - getting info about telegram usernames (Ver 1.0.0) .

## a small package for getting info about telegram accounts .

---------------------------------------------------------------

# USAGE 

1 - IMPORT PACKAGE
	``>>> from telget import Username``

2 - MAKE OBJECT 
	``>>> username = "telegram_username"``
	``>>> account = Username(username)``

3 - GET INFO ABOUT USERNAME 
- GET Account TYPE (Channel or Group or ....) -> ``>>> account.getType()``
- GET Bio -> ``>>> account.getBio()``
- GET Members (for channels and groups) -> ``>>> account.getMembers()``
- Download And Save Profile Photo -> ``>>> account.getProfilePhoto(path_to_save)``


Have Fun ... 



