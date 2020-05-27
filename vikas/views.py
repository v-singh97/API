from django.shortcuts import render
from .models import User, Activity_period
from django.http import JsonResponse
import json


# Create your views here.

def verify(request):
    if request.method=="POST":
        name = request.POST['username']
        pwd = request.POST['pwd']
        if name=='vikas' and pwd =='1234':
            user = User.objects.all()
            
            return render(request,'user.html',{"user":user})
        else:
            msg='Wrong password'
            return render(request,'admin.html',{'msg':msg})
def admin(request):
    return render(request,'admin.html')

def delete_user(request):
    if request.method=="POST":
        r = request.POST
        uid = r['userid']
        c = User.objects.get(user_id=uid)
        c.delete()
        user = User.objects.all()    
        return render(request,'user.html',{"user":user})
def add(request):
    if request.method=="POST":
        r = request.POST
        uid = r['userid']
        name = r['name']
        tz = r['tz']
        st1 = r['start1'].replace('T',' ')
        et1 = r['end1'].replace('T',' ')
        st2 = r['start2'].replace('T',' ')
        et2 = r['end2'].replace('T',' ')
        st3 = r['start3'].replace('T',' ')
        et3 = r['end3'].replace('T',' ')
        print(st1)
        try:
            c = User(user_id=uid, real_name=name, time_zone=tz)
            c.save()
            l = Activity_period(user_id_id=uid,start_time1 = st1, end_time1 = et1,start_time2 = st2, end_time2 = et2,start_time3 = st3, end_time3 = et3)
            l.save()
            
        except Exception as r:
            print(r)
            pass
        user = User.objects.all()    
        return render(request,'user.html',{"user":user})
def update(request):
    if request.method=="POST":
        uid = request.POST['user']
        print(uid)
        data = Activity_period.objects.get(user_id=uid)
        return render(request,'data.html',{"data":data,"user":uid})
def update_user(request):
    if request.method=="POST":
        r = request.POST
        uid = r['userid']
        st1 = r['start1']
        et1 = r['end1']
        st2 = r['start2']
        et2 = r['end2']
        st3 = r['start3']
        et3 = r['end3']
        data = Activity_period.objects.get(user_id=uid)
        data.start_time1 = st1
        data.end_time1 = et1 
        data.start_time2 = st2
        data.end_time2 = et2
        data.start_time3 = st3
        data.end_time3 = et3
        data.save()
        data = Activity_period.objects.get(user_id=uid)
        return render(request,'data.html',{"data":data,"user":uid})
def time(t):
    d ={
        '01':"Jan", '02':"Feb", '03':"Mar", '04':"Apr", '05':"May",
        '06':"Jun", '07':"Jul", '08':"Aug", '09':"Sep", '10':"Oct",
        '11':"Nov", '12':"Dec"
    }
    t=t.split(' ')
    date = t[0].split('-')
    date[1] = d.get(date[1])
    date = "%s %s %s "%(date[1],date[2],date[0])
    time = t[1].split(':')
    val="AM"
    if int(time[0]) >=12:
        val="PM"
        time[0]=int(time[0])-12
    time1 = "%i:%s%s"%(int(time[0]),time[1],val)
    return "%s %s"%(date,time1)

def index(request):
    p = User.objects.all()
    members=[]
    for i in p:
        
        try:    
            x = Activity_period.objects.get(user_id=i.user_id)
            members.append({
                "id": "%s"%i.user_id,
                "real_name": "%s"%i.real_name,
                "tz": "%s"%i.time_zone,
                "activity_periods":[
                    {"start_time": "%s"%time(str(x.start_time1)),
                        "end_time": "%s"%time(str(x.end_time1))
                    },
                    {"start_time": "%s"%time(str(x.start_time2)),
                        "end_time": "%s"%time(str(x.end_time2))
                    },
                    {"start_time": "%s"%time(str(x.start_time3)),
                        "end_time": "%s"%time(str(x.end_time3))
                    }

                ]
            }
            )
        except Exception as e:
            print(e)
            pass
        
    li = {
        	"ok": True,
	"members": members
    }
    print(li)
    return JsonResponse(li)