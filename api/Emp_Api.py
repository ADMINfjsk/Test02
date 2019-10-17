import app


class EmpCRUD:
    def add(self,session,username,mobile,workNumber):
        myempdata = {"username": username,
                  "mobile": mobile,
                  "workNumber":workNumber}
        return session.post(app.BASE_URL+"user", json=myempdata,
                            headers={"Authorization":"Bearer "+app.TOKEN})

    def update(self,session,userID,username):
        return session.put(app.BASE_URL+"user/"+userID,json = {"username": username},headers={"Authorization":"Bearer "+app.TOKEN})

    def get(self,session,userID):
        return session.get(app.BASE_URL + "user/" + userID,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def delete(self,session,userID):
        return session.delete(app.BASE_URL + "user/" + userID,
                           headers={"Authorization": "Bearer " + app.TOKEN})