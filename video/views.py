from django.http import HttpResponse
from django.shortcuts import render

import json
import qiniu.conf
import qiniu.rs
import qiniu.io

BUCKET_NAME = "idcard"
qiniu.conf.ACCESS_KEY = "vTlIBSb6E3VCaL6dH13lye9iWkHpkSDN4_UhzRTK" 
qiniu.conf.SECRET_KEY = "8v9NMvJJry5z-alc918uip50SMJFhn5550cg4uyQ" 
def index(request):
    return render(request, 'demo/index.html')

def uptoken(request):
    policy = qiniu.rs.PutPolicy(BUCKET_NAME)
    token = policy.token()
    data = {'uptoken': token}
    return HttpResponse(json.dumps(data), content_type="application/json")
