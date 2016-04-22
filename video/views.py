from django.http import HttpResponse
from django.shortcuts import render

import json
import qiniu.conf
import qiniu.rs
import qiniu.io

BUCKET_NAME = ""
qiniu.conf.ACCESS_KEY = "" 
qiniu.conf.SECRET_KEY = "" 
def index(request):
    return render(request, 'demo/index.html')

def uptoken(request):
    policy = qiniu.rs.PutPolicy(BUCKET_NAME)
    token = policy.token()
    data = {'uptoken': token}
    return HttpResponse(json.dumps(data), content_type="application/json")
