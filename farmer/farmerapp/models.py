from django.db import models

class Farming(models.Model):
    name = models.CharField(max_length=100)
    rotation = models.IntegerField( null=True)
    yellow = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)
    divine = models.IntegerField(default=0)
    map_type = models.CharField(max_length=100)
    map_count = models.IntegerField(default=0)
    profit = models.FloatField(default=0)
    net_profit = models.FloatField(default=0)
    cost = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(default = 0)
    
    
    def save(self, *args, **kwargs):
        
        self.profit = self.yellow / 20000 + self.blue / 100000 + self.red / 100000 + self.divine \
            + self.map_count * 0.8 if self.map_type == '지구라트' \
              else self.map_count * 0.7 if self.map_type == '흉물' or self.map_type == '성채' \
              else self.map_count * 0.9
        self.net_profit = self.profit - self.cost
        if self.end_time and self.start_time:  
            self.duration = int((self.end_time - self.start_time).total_seconds())
        
        super().save()
    # @property는 그냥 객체.profit으로 해서 값을 바로 구할수있는거. 집계함수나 이런걸로 못 씀.
    
    # @property
    # def profit(self):
    #     return self.yellow / 20000 + self.blue / 100000 + self.red / 100000 + self.divine \
    #         + self.map_count * 0.8 if self.map_type == '지구라트' \
    #           else self.map_count * 0.7 if self.map_type == '흉물' or self.map_type == '성채' \
    #           else self.map_count * 0.9
    
    # @property
    # def net_profit(self):
    #     return self.profit - self.cost
    
    # @property
    # def duration(self):
    #     return int(self.end_time - self.start_time)