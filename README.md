# Important Notes

- Git Hub Api has service limit of 60 requests/hour. Every internal request is considered as a new request.
- If you hit the thrushold, the server gives Internal Server Error. (This should be handled but I didn't due to time constaint).
- Given time, I can provide the perfect API endpoint. 

#  API Endpoint

 - test_git_id = 7633377
 - https://l4w6dh6uqi.execute-api.us-east-2.amazonaws.com/dev/github/users/<test_git_id>
 
## Languages and Libraries used
- python
- Flask 
- zappa
- AWS 

## Deployment
- AWS LAMBDA


## Todo (Time Constraint)
- Proper Status Codes 
- Commenting the code
- Testing 
- Proper organizing 


### General Items
- Add cli flag to use local Sqlite DB
- Fix swagger generation to include all urls for a resource not just the first in the list
