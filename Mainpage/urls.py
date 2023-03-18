from django.urls import path
from . import views
urlpatterns = [
    path('',views.Homepage,name="Homepage"),
    path('cart/',views.CartManager,name="CartManager"),
    path('product/',views.ProductPage,name="ProductPage"),
    path('men/top/',views.MenTopwear,name="MenTopwear"),
    path("men/bottom/",views.MenBottomwear,name="MenBottomwear"),
    path("men/accessories/",views.MenAccessories,name="MenAccessories"),
    path("men/top/Kurta/",views.KurtasPage,name="KurtasPage"),
    path("men/top/Shirt/",views.ShirtsMenPage,name="ShirtsMenPage"),
    path("men/top/Jacket/",views.JacketPage,name="JacketPage"),
    path("men/bottom/Pyjama/",views.PyjamaMenPage,name="PyjamaMenPage"),
    path("men/bottom/Pents/",views.PentsPage,name="PentsPage"),
    path("men/accessories/Pockets/",views.PocketsPage,name="PocketsPage"),
    path("men/accessories/Shawls/",views.ShawlsPage,name="ShawlsPage"),
    path("women/top/",views.WomenTopwear,name="WomenTopwear"),
    path("women/bottom/",views.WomenBottomwear,name="WomenBottomwear"),
    path("women/accessories/",views.WomenAccessories,name="WomenAccessories"),
    path("women/top/Kurties/",views.KurtiesPage,name="KurtiesPage"),
    path("women/top/Shirt/",views.ShirtsPage,name="ShirtsPage"),
    path("women/top/Dress/",views.DressPage,name="DressPage"),
    path("women/top/Spaghetti/",views.SpaghettiPage,name="SpaghettiPage"),
    path("women/bottom/Skirt/",views.SkirtPage,name="SkirtPage"),
    path("women/bottom/Pyjama/",views.PyjamaPage,name="PyjamaPage"),
    path("women/bottom/Pants/",views.PantsPage,name="PantsPage"),
    path("women/accessories/Bags/",views.BagAccessories,name="BagAccessories"),
    path("women/saree/",views.SareePage,name="SareePage"),
    path("product-detail/<id>/",views.Product_Detail,name="Product_Detail"),
    path("product-detail/<id>/",views.Product_Detail,name="Product_Detail"),
    path("profile/",views.ProfilePage,name="ProfilePage"),
    path("delete-cart/",views.DeleteCartItem,name="DeleteCartItem"),
    path("about/",views.AboutPage,name="AboutPage"),
    path("contact/",views.ContactPage,name="ContactPage"),
    path("edit-profile/",views.Edit_Profile,name="Edit_Profile"),
    path("Review-page/",views.ManageReviews,name="ManageReviews"),
    path("order/",views.OrderPage,name="OrderPage"),
    path("checkout/",views.checkout,name="checkout"),
    path('success/',views.success_page,name="success_page"),
    path('cancle/',views.cancle_page,name="cancle_page"),
    path('logout/',views.Logout,name="Logout"),
]