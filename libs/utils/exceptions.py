class PubErrorCustom(Exception):    def __init__(self,msg):        super(PubErrorCustom,self).__init__()        self.msg = msgclass InnerErrorCustom(Exception):    def __init__(self,code=None,msg=None):        super(InnerErrorCustom,self).__init__()        self.code = code if code else "99999"        self.msg = msg if msg else "请求出错,请稍后再试！"