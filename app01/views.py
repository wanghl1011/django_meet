from django.shortcuts import render, redirect
from app01.models import UserInfo, MeetingRoom, OrderRecord, TimeSlot
import time
from django.http import JsonResponse
# Create your views here.


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        user = UserInfo.objects.filter(username=name, password=pwd).first()
        if user:
            request.session["user"] = user.pk
            return redirect("/app01/show/")
        else:
            return render(request, "login.html", {"msg": "用户名或密码不正确"})
    else:
        return render(request, "login.html")


def get_room_time_data(time_list, room_list, time_str):

    record_list = OrderRecord.objects.filter(order_time=time_str)
    data_dict = {}
    for item in room_list:
        data_dict[item.pk] = [
            {"name": item.name, "isroom": True},
        ]
    for key, value in data_dict.items():
        for time_obj in time_list:
            dic = {"time_pk": time_obj.pk, "room_pk": key,
                   "order": None, "isbook": False}
            for item in record_list:
                if item.meet_room.pk == key and item.time_slot.pk == time_obj.pk :
                    dic = {
                        "username": item.account.username, "room_name": item.meet_room.name,
                        "time_area": item.time_slot.time_area, "isbook": True
                    }
            value.append(dic)
    return data_dict



def show_meeting_room(request):
    if request.method == "GET":
        time_str = request.GET.get("t")
        if not time_str:
            time_str = time.strftime('%Y-%m-%d', time.localtime())
        else:
            date_list = time_str.split("-")
            time_str = "-".join(reversed(date_list))
        time_list = TimeSlot.objects.all()
        room_list = MeetingRoom.objects.all()
        data_dict = get_room_time_data(time_list,room_list,time_str)
        return render(request, "show_room.html", locals())


def select(request):
    ret = {"msg":"ok"}
    return JsonResponse(ret)

def order(request):
    if request.is_ajax():
        t = request.POST.get("time")
        # now_time = time.strftime('%Y-%m-%d', time.localtime())
        print(t)
        if not t:
            time_str = time.strftime('%Y-%m-%d', time.localtime())
        else:
            date_list = t.split("-")
            time_str = "-".join(reversed(date_list))
        # t_time=time.strptime(time_str, '%Y-%m-%d')
        # n_time=time.strptime(now_time, '%Y-%m-%d')
        # if t_time.tm_mday < n_time.tm_mday :
        #     ret={"code":1001,"msg":"不能预约今天之前的会议室"}
        #     return JsonResponse(ret)
        rpk = request.POST.get("rpk")
        tpk = request.POST.get("tpk")
        user_pk = request.session["user"]
    # if OrderRecord.objects.filter(account_id=user_pk,meet_room_id=room_id,time_slot_id=time_id,order_time=time_str).exists():
    #     pass
    # else:
        OrderRecord.objects.create(account_id=user_pk,meet_room_id=rpk,time_slot_id=tpk,order_time=time_str)
        ret = {"code":1000,"msg":"success"}
        return JsonResponse(ret)



