from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date') #獲取數據
    paginator = Paginator(cars, 2) # 創建分頁物件，每頁顯示10筆 cars的資料
    page = request.GET.get('page')#從請求裡獲取當前的頁面號碼
    #處理分頁異常 如果頁碼不是整數或超出範圍 則補獲相應的異常並進行處理
    #try ... except
    try:
        paged_cars = paginator.get_page(page) #獲取當前頁面物件
    except PageNotAnInteger: #如果頁碼不是整數 顯示第一頁
        paged_cars = paginator.page(1)
    except EmptyPage: #如果頁碼超出範圍 顯示最後一頁
         paged_cars = paginator.page(paginator.num_pages)

    data ={
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    #取得單一卡片資料
    single_car = get_object_or_404(Car, pk=id)
    context = {
        'single_car': single_car
    }
    return render(request,'cars/car_detail.html', context)

def search(request):
    #取的卡片資料
    cars = Car.objects.order_by('-created_date')

    #做關鍵字判斷
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars =cars.filter(description__icontains=keyword)#description欄位關鍵字

    context = {
        'cars':cars,
    }
    return render(request, 'cars/search.html',context)
    