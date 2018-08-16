from django.shortcuts import render
import memcache
from cacheapp.models import Cake


def memcached_getdata(request, cake_id):
    mc = memcache.Client(["127.0.0.1:11211"])  # 可以设置多个ip+port，因为是分布式系统
    value = mc.get('cake_' + cake_id)  # key为动态
    print(value)
    print(type(value))
    if value:
        return render(request, 'cake.html', {'msg': '恭喜，缓存命中！', 'cake': value})
    else:
        cake = Cake.objects.get(id=cake_id)
        mc.set('cake_' + cake_id, cake, 30)
        return render(request, 'cake.html', {'msg': '这是从MySQL中查到的……', 'cake': cake})
