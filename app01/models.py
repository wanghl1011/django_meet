from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=128,verbose_name="密码")

    def __str__(self):
        return self.username

class TimeSlot(models.Model):
    """
    时间段表
    """

    time_area = models.CharField(max_length=32,verbose_name="时间段")
    col = models.IntegerField(verbose_name="该时间段在表格中是第几列", default=1)

    def __str__(self):
        return self.time_area

class MeetingRoom(models.Model):
    """
    会议室表
    """
    name = models.CharField(max_length=32,verbose_name="会议室名称")
    num = models.IntegerField(verbose_name="容纳人数")
    des = models.CharField(max_length=64,verbose_name="会议室介绍",null=True,blank=True)
    row = models.IntegerField(verbose_name="该会议室在表格中是第几行",default=1)

    def __str__(self):
        return self.name


class OrderRecord(models.Model):
    """
    会议室预约记录表
    """
    account = models.ForeignKey("UserInfo",verbose_name="用户",on_delete=models.CASCADE)
    meet_room = models.ForeignKey("MeetingRoom",verbose_name="会议室",related_name="record",on_delete=models.CASCADE)
    order_time = models.DateField(verbose_name="预定日期")
    time_slot = models.ForeignKey("TimeSlot",on_delete=models.CASCADE,related_name="record")

    col = models.IntegerField(verbose_name="列",blank=True,null=True)
    row = models.IntegerField(verbose_name="行",blank=True,null=True)


    # def save(self,*args,**kwargs):
    #     self.col = self.time_slot.col
    #     self.row = self.meet_room.row



    def __str__(self):
        return self.meet_room.name

    class Meta:
        unique_together = (
            ("meet_room","order_time","time_slot")
        )

# 		用户表：
# 			ID     姓名
# 			 1     放景洪
# 			 2     放景洪2
#
# 		会议室表：
# 			ID     名称
# 			1     马尔代夫
# 			2     塞班
# 			3     沙河
#
# 		时间段表：
# 			1      8:30 - 9:30
# 			2      9:30 - 10:30
# 			....
#
# 		预定表：
# 			用户     会议室         日期          时间段
# 			 1         1         2018-03-27         1
# 			 1         1         2018-03-28         1
# 			 1         2         2018-04-28         3
# 			 ...
# 			 联合唯一