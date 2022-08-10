# AuthUsersWithInvitesSecondTask
Service for registration, authorization and invitation of users to the system.


### How to deploy a project:

1. Go to AuthUsersWithInvitedSecondTask
``` 
$ cd AuthUsersWithInvitedSecondTask
```
2. Run docker-compose file:
```
$ docker-compose up -d
```
3. Load data to project:
```
$ cd invite_users 
$ python manage.py loaddata db.json
```
4. Open 0.0.0.0:8000 url in browser
