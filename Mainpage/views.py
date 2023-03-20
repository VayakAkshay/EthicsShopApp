from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ProductData,CartItems,ContactData,OrderItem,ReviewData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import stripe
import datetime
from datetime import timedelta

def Homepage(request):
    men_product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").all().values()
    women_product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("pass")
        cpass = request.POST.get("cpass")
        if password == cpass:
            myuser = User.objects.create_user(email,mobile,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = authenticate(username = email,password = password)
            login(request,user)
            messages.success(request,"You are Logged in successfully")
            return redirect("/")
        else:
            messages.warning(request,"Password is not matched ")
            return redirect("/password/")
    return render(request,"Mainpage/index.html",{"men_product_data":men_product_data,"women_product_data":women_product_data})

def ProductPage(request):
    product_data = ProductData.objects.all()
    return render(request,"Mainpage/product.html",{"product_data":product_data})

def MenTopwear(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/top/{}".format(i)
        main_list.append(mydic)
    link = "/men/top/"
    title = "Top Wear for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def MenBottomwear(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Bottom").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/men/bottom/"
    title = "Bottom Wear for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def MenAccessories(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Accessories").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/accessories/{}".format(i)
        main_list.append(mydic)
    link = "/men/accessories/"
    title = "Accessories for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def KurtasPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").filter(product_subcategory = "Kurta").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/top/{}".format(i)
        main_list.append(mydic)
    print(sub_cat_list)
    link = "/men/top/"
    title = "Kurtas for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def ShirtsMenPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").filter(product_subcategory = "Shirt").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/top/{}".format(i)
        main_list.append(mydic)
    print(sub_cat_list)
    link = "/men/top/"
    title = "Shirts for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})


def JacketPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Top").filter(product_subcategory = "Jacket").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/top/{}".format(i)
        main_list.append(mydic)
    print(sub_cat_list)
    link = "/men/top/"
    title = "Jackets for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def PyjamaMenPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Bottom").filter(product_subcategory = "Pyjama").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/men/bottom/"
    title = "Pyjama for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def PentsPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Bottom").filter(product_subcategory = "Pents").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/men/bottom/"
    title = "Pents for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def PocketsPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Accessories").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Accessories").filter(product_subcategory = "Pockets").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/accessories/{}".format(i)
        main_list.append(mydic)
    link = "/men/accessories/"
    title = "Pockets for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def ShawlsPage(request):
    product_data = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Accessories").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Male").filter(product_category = "Accessories").filter(product_subcategory = "Shawls").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/men/accessories/{}".format(i)
        main_list.append(mydic)
    link = "/men/accessories/"
    title = "Shawls for Men"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def WomenTopwear(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/top/{}".format(i)
        main_list.append(mydic)
    link = "/women/top/"
    title = "Top Wear for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def WomenBottomwear(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/women/bottom/"
    title = "Bottom Wear for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def WomenAccessories(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Accessories").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/accessories/{}".format(i)
        main_list.append(mydic)
    link = "/women/accessories/"
    title = "Accessories for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"sub_cat_list":main_list,"link":link,"title":title})

def KurtiesPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").filter(product_subcategory = "Kurties").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/top/{}".format(i)
        main_list.append(mydic)
    link = "/women/top/"
    title = "Kurties for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def ShirtsPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").filter(product_subcategory = "Shirt").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/top/{}".format(i)
        main_list.append(mydic)
    link = "/women/top/"
    title = "Shirts for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})


def DressPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").filter(product_subcategory = "Dress").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/top/{}".format(i)
        main_list.append(mydic)
    link = "/women/top/"
    title = "Dresses for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def SpaghettiPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Top").filter(product_subcategory = "Spaghetti").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/top/{}".format(i)
        main_list.append(mydic)
    link = "/women/top/"
    title = "Kurties for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def SkirtPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").filter(product_subcategory = "Skirt").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/women/bottom/"
    title = "Skirts for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def PyjamaPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").filter(product_subcategory = "Pyjama").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/women/bottom/"
    title = "Pyjama for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def PantsPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").filter(product_subcategory = "Pants").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/women/bottom/"
    title = "Pents for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def SkirtPage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Bottom").filter(product_subcategory = "Skirt").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/bottom/{}".format(i)
        main_list.append(mydic)
    link = "/women/bottom/"
    title = "Kurties for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def BagAccessories(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Accessories").all().values()
    product_datas = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Accessories").filter(product_subcategory = "Bags").all().values()
    sub_cat_list = set()
    for i in product_data:
        sub_cat_list.add(i["product_subcategory"])
    main_list = []
    for i in sub_cat_list:
        mydic = {}
        mydic["sub"] = i
        mydic["link"] = "/women/accessories/{}".format(i)
        main_list.append(mydic)
    link = "/women/accessories/"
    title = "Bags for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_datas,"sub_cat_list":main_list,"link":link,"title":title})

def SareePage(request):
    product_data = ProductData.objects.filter(product_gender = "Female").filter(product_category = "Saree").all().values()
    link = "/women/saree/"
    title = "Sarees for Womens"
    return render(request,"Mainpage/product.html",{"product_data":product_data,"link":link,"title":title})

def Product_Detail(request,id):
    product_data = ProductData.objects.filter(id=id)
    reviews_data = ReviewData.objects.filter(product_id = id).all().values()
    review_list = []
    for i in reviews_data:
        review_dic = {}
        review_dic["id"] = i['id']
        review_dic["customer_id"] = i["user_id"]
        str = ""
        for j in range(i["review_star"]):
            str = str + "a"
        review_dic["stars"] = str
        review_dic["reviewer_name"] = i["reviewer_name"]
        review_dic["review_text"] = i["review_desc"]
        review_list.append(review_dic)
    return render(request,"Mainpage/product-detail.html",{"product_data":product_data,"review_list":review_list})

def CartManager(request):
    if request.user.is_authenticated == True:
        user = request.user
        cart_data = CartItems.objects.filter(user_id = user.id).all().values()
        cartlen = len(cart_data)
        datas = []
        total_price = 0
        for i in cart_data:
            mydic = {}
            prod_id = i["product_id"]
            mydic["cart_id"] = i["id"]
            mydic["product_id"] = prod_id
            product_data = ProductData.objects.filter(id = prod_id).values()[0]
            mydic["name"] = product_data["product_name"]
            mydic["qty"] = i["qty"]
            mydic["price"] = i["qty"] * product_data["product_price"]
            total_price += i["qty"] * product_data["product_price"]
            mydic["product_img"] = product_data["product_img"]
            datas.append(mydic)
        cart_item = CartItems()
        if request.method == "POST":
            product_id = request.POST.get("product_id")
            qtys = int(request.POST.get("qtys"))
            cart_item.product_id = product_id
            cart_item.user_id = user.id
            cart_item.qty = qtys
            cart_item.save()
            return redirect('/cart/')
        return render(request,"Mainpage/cart.html",{"datas":datas,"total_price":total_price,"cartlen":cartlen})
    else:
        return redirect("/login/")

def DeleteCartItem(request):
    if request.method == 'POST':
        cart_id = request.POST.get("cart_id")
        CartItems.objects.filter(id = cart_id).delete()
        messages.success(request,"Item deleted successfully.")
        return redirect("/cart/")
    return redirect("/cart/")

def ProfilePage(request):
    user = request.user
    order_data = OrderItem.objects.filter(user_id = user.id).all().values()
    order_datas = []
    for i in order_data:
        mydic = {}
        product_data = ProductData.objects.filter(id = i["product_id"]).all().values()[0]
        mydic["id"] = i["id"]
        mydic["product_img"] = product_data["product_img"]
        mydic["product_name"] = product_data["product_name"]
        mydic["qty"] = i["qty"]
        mydic["product_price"] = product_data["product_price"]
        today_date = datetime.date.today()
        delivery_date = i["delivery_date"]
        day_diff = abs(today_date - delivery_date).days
        diff = -(today_date - delivery_date).days
        progresses = 100
        if diff<0:
            progresses = 100
        else:
            for i in range(1,diff+1):
                progresses = progresses - 10
        mydic["progress"] = progresses
        order_datas.append(mydic)
    return render(request,"Mainpage/profile.html",{"order_datas":order_datas})

def Edit_Profile(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        User.objects.filter(username = request.user).update(first_name = fname)
        User.objects.filter(username = request.user).update(last_name = lname)
        User.objects.filter(username = request.user).update(username = email)
        messages.success(request,"Your profile succeessfully updated")
        return redirect("/profile/")
    return render(request,"Mainpage/edit_profile.html")

def AboutPage(request):
    return render(request,"Mainpage/about.html")

def ContactPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact_data = ContactData(contact_email = email,contact_message = message)
        contact_data.save()
        messages.success(request,"Thanks for contacting us we will connect you soon.")
        return redirect("/contact/")
    return render(request,"Mainpage/contact.html")

def ManageReviews(request):
    if request.method == "POST":
        stars = request.POST.get("result")
        product_id = request.POST.get("product_id")
        review = request.POST.get("review")
        reviews = ReviewData(product_id = product_id,user_id = request.user.id,reviewer_name = request.user.first_name,review_desc = review,review_star = stars)
        reviews.save()
        return redirect("/product-detail/{}/".format(product_id))
    return redirect("/product/")

def OrderPage(request):
    return render(request,"Mainpage/order.html")

def OrderCancle(request):
    if request.method == "POST":
        id = request.POST.get("order_id")
        OrderItem.objects.filter(id = id).delete()
    return redirect("/profile/")

stripe.api_key = 'sk_test_51MedHmSHJDFuPL5cnRItHVU94xOAzKltL5vuoADjGI0wZfVNRtCwU3I3eKgvtQUF0z3w2yl5IuQ5rRZcOs9m2ytj00YSZRJhjw'
def checkout(request):
    user = request.user
    if request.method == "POST":
        total_price = 0
        cart_data = CartItems.objects.filter(user_id=user.id).all().values()
        line_items = []
        total_price = 0
        for i in range(0,len(cart_data)):
            product_id = cart_data[i]["product_id"]
            product_data = ProductData.objects.filter(id = product_id).all().values()[0]
            total_price = total_price + product_data["product_price"]
            line_items.append(
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': product_data["product_name"],
                    },
                    'unit_amount': int(product_data["product_price"] * 100),
                },
                'quantity': cart_data[i]["qty"],
            })
        session = stripe.checkout.Session.create(
        line_items= line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancle/',
        )
        return redirect(session.url, code=303)
    return redirect('/')


def success_page(request):
    user = request.user
    cart_item = CartItems.objects.filter(user_id = user.id).all().values()
    for i in cart_item:
        order_item = OrderItem()
        order_item.product_id = i["product_id"]
        order_item.qty = i["qty"]
        order_item.user_id = user.id
        today_date = datetime.date.today()
        delivery_date = today_date + timedelta(days=10)
        order_item.delivery_date = delivery_date
        order_item.save()
    CartItems.objects.filter(user_id = user.id).delete()
    return render(request,"Mainpage/success.html")


def cancle_page(request):
    return render(request,"Mainpage/cancle.html")

def Logout(request):
    logout(request)
    return redirect("/")