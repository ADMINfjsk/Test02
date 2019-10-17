import app
import logging

class UserLogin:
    def login(self,session,mobile,password):
        mydata= {"mobile":mobile,
                 "password":password
                 }
        logging.info("执行登录测试")
        return session.post(app.BASE_URL+"login",json=mydata)