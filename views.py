from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import *
from datetime import date
from random import randint

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.POST:
        uname=request.POST["uname"]
        psw=request.POST["psw"]
        user=authenticate(username=uname,password=psw)
        
        print(user)
        if user:
            userdata=CustomUser.objects.get(username=uname)
            if userdata.usertype == "supervisor":
                    request.session["email"]=uname
                    return redirect("/superhome")
            elif userdata.is_superuser == 1:
                    return redirect("/adminhome")
           
            elif userdata.usertype == "customer":
                    request.session["email"]=uname
                    r = Registration.objects.get(email=uname)
                    request.session["id"]=r.id
                    request.session["name"]=r.name
                    return redirect("/userhome")
            

                   
            elif userdata.usertype == "expert":
                    request.session["email"]=uname
                    r = Expert.objects.get(email=uname)
                    request.session["id"]=r.id
                    request.session["name"]=r.name
                    return redirect("/experthome")
           
        else:
            messages.info(request,"User dosent exist")
    return render(request,"login.html")


def register(request):
    if request.POST:
        name=request.POST["name"]
        con=request.POST["con"]
        email=request.POST["email"]
        add=request.POST["add"]
        psw=request.POST["psw"]
        user=Registration.objects.filter(email=email,psw=psw).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=email,email=email,password=psw,usertype="customer")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Registration.objects.create(name=name,con=con,email=email,psw=psw,add=add,user=u)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request,"register.html")

def expreg(request):
    if request.POST:
        name=request.POST["name"]
        con=request.POST["con"]
        email=request.POST["email"]
        add=request.POST["add"]
        psw=request.POST["psw"]
        lic=request.FILES["lic"]
        user=Registration.objects.filter(email=email,psw=psw).exists()
        if user:
            messages.info(request,"User already exists")
        else:
            try:
                u=CustomUser.objects.create_user(username=email,email=email,password=psw,usertype="expert")
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                try:
                    s=Expert.objects.create(name=name,con=con,email=email,psw=psw,lic=lic,add=add,user=u)
                    s.save()
                except Exception as e:
                    messages.info(request,e)
                else:
                    messages.info(request,"Registered successfully")
    return render(request,"expertreg.html")


def adminhome(request):
    return render(request,"adminhome.html")

def adminraw(request):
    data=Raw.objects.all()
    if request.POST:
        name=request.POST["uname"]
        ing=request.POST["ing"]
        url=request.POST["url"]
       
        user=Raw.objects.filter(title=name).exists()
        if user:
            messages.info(request,"Recipe already exists")
        else:
            try:
                u=Raw.objects.create(title=name,link=url,ing=ing)
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                messages.info(request,"Added successfully")
    return render(request,"adminraw.html",{"data":data})

def admincooked(request):
    data=Cooked.objects.all()
    if request.POST:
        name=request.POST["uname"]
        ing=request.POST["ing"]
        url=request.POST["url"]
       
        user=Cooked.objects.filter(title=name).exists()
        if user:
            messages.info(request,"Recipe already exists")
        else:
            try:
                u=Cooked.objects.create(title=name,link=url,ing=ing)
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                messages.info(request,"Added successfully")
    return render(request,"admincooked.html",{"data":data})

def adminex(request):
    dta=Videos.objects.all()
    if request.POST:
        name=request.POST["uname"]
        ing=request.FILES["file"]
       
        user=Videos.objects.filter(title=name).exists()
        if user:
            messages.info(request,"Video already exists")
        else:
            try:
                u=Videos.objects.create(title=name,file=ing)
                u.save()
            except Exception as e:
                messages.info(request,e)
            else:
                messages.info(request,"Added successfully")
    return render(request,"adminex.html",{"dta":dta})

def adminuser(request):
    data=Registration.objects.all()
    return render(request,"adminuser.html",{"data":data})

def userhome(request):
    return render(request,"userhome.html")

def experthome(request):
    return render(request,"experthome.html")

def superhome(request):
    return render(request,"superhome.html")

def expertvreq(request):
    uid=request.session["id"]
    data=Request.objects.filter(expert=uid)
    return render(request,"expertvreq.html",{"data":data})

def exppyramid(request):
    exid=request.session["id"]
    exp=Expert.objects.get(id=exid)
    id=request.GET.get("id")
    data=Request.objects.get(id=id)

    if request.POST:
            br=request.POST["br"]
            dn=request.POST["dn"]
            ln=request.POST["ln"]
            bcal=request.POST["bcal"]
            dcal=request.POST["dcal"]
            lcal=request.POST["lcal"]
       
       


            try:
                u=Pyramid.objects.create(breakfast=br,bcal=bcal,lcal=lcal,dcal=dcal,lunch=ln,dinner=dn,user=data.user,req=data)
                u.save()
            except Exception as e:

                messages.info(request,e)
            else:
                messages.info(request,"Added successfully")
                data.status = "Processed"
                data.save()
                return redirect("/expertvreq")

    return render(request,"exppyramid.html")



def inchat(request):
    sender = request.session['email']
    receiver=request.GET.get("email")
    print(receiver)
    print(sender)
    dates=date.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
 
    r=Chat.objects.all()
    return render(request,"inchat.html",{"messages":r,"sender":sender, "receiver": receiver}  )



def sfChatPer(request):
    sender = request.session['email']
    receiver = request.GET['email']
    dates=date.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
   
    r=Chat.objects.all()
    # for i in  r:

    return render(request, "sfChatPer.html", {"messages":r,"sender":sender, "receiver": receiver})  




def usercooked(request):
    data=Cooked.objects.all()
    return render(request,"usercooked.html",{"data":data})

def userraw(request):
    data=Raw.objects.all()
    print(data)
    return render(request,"userraw.html",{"data":data})
def userexercise(request):
    data=Videos.objects.all()
    return render(request,"userexercise.html",{"data":data})

def userreq(request):
    data=Expert.objects.all()
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)','Coffee','Milk','Dosa','Idli','Chappati']
    fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas','Asparagus Cooked','Bagels made in wheat','Brocolli','Brown Rice','Cauliflower','American cheese','Beef sticks','Rice Pudding']
    ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-caloriesorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar','Berries','Dark chocolates','Milk','Pasta canned with tomato sauce','Tuna Salad','Tuna Fish','French Fries','Chocolate Doughnuts','Chappati','Bhaji Pav','Dal Makhani','Sweet Potatoes cooked','Boiled Potatoes','Goat meat','Steak Fries','Pork cooked','Bacon cooked','Chicken Popcorn','Turkey cooked','Vanilla Ice cream']


    if request.POST:
        weight=request.POST["weight"]
        height=request.POST["height"]
        age=request.POST["age"]
        exid=request.POST["exp"]
        exp=Expert.objects.get(id=exid)
        select=request.POST["select"]
        gender=request.POST["gender"]
        height=int(height)
        height=height/100
        h2=height**2
        weight=int(weight)
        BMI=weight/h2
        BMI=round(BMI,2)
        print(BMI)
        if BMI < 16.0:
            health="Severly underweight"
        elif BMI < 17.0:
            health=" underweight"
        elif BMI < 18.5:
            health="Normal underweight"
        elif BMI < 24.9:
            health="Healthy weight"
        elif BMI < 29.9:
            health="Healthy weight"
        elif BMI < 34.9:
            health=" obesity"
        elif BMI < 39.9:
            health="Obesity"
        elif BMI > 40.0 :
            health="Heavy Obesity"

        if gender == 'Male':
            calories = float()
            calories = 88.362 + (13.397*float(weight)) + (4.799*float(height)) - (5.677*float(age))
            print ("Calories:",calories)
        elif gender == 'Female':
            calories = float()
            calories = 447.593 + (9.247*float(weight)) + (3.098*float(height)) - (4.330*float(age))

        if select == 'Super Light (little or no exercise)':
            calories = calories*1.2

        elif select == 'Lightly active (1-3 days/week)':
            calories = calories*1.375

        elif select == 'Moderately active (3-5 days/week)':
            calories = calories*1.55

        elif select == 'Very active (6-7 days/week)':
            calories = calories*1.725

        elif select == 'Super active (twice/day)':
            calories = calories*1.9

        if calories<1500:
            l6 = f"Breakfast:{protein[randint(0, 4)]},{fruit[randint(0, 5)]}"
            l8 = f"Lunch:{protein[randint(0, 4)]},{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]} "
            l9 = f"Snack:{ps[randint(0, 4)]},{vegetable[0]}"
            l10 = f"Dinner:{protein[randint(0, 4)]},'2 '+{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]}"
            l11= f"Snack:{fruit[randint(0, 5)]}"
        elif calories<1800:
            l6 = f"Breakfast:{protein[randint(0, 4)]},{fruit[randint(0, 5)]}"
            l8 = f"Lunch:{protein[randint(0, 4)]},{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]} "
            l9 = f"Snack:{ps[randint(0, 4)]},{vegetable[0]}"
            l10 = f"Dinner:{protein[randint(0, 4)]},'2 '+{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]}"
            l11= f"Snack:{fruit[randint(0, 5)]}"
        elif calories<2200:
            l6 = f"Breakfast:{protein[randint(0, 4)]},{fruit[randint(0, 5)]}"
            l8 = f"Lunch:{protein[randint(0, 4)]},{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]} "
            l9 = f"Snack:{ps[randint(0, 4)]},{vegetable[0]}"
            l10 = f"Dinner:{protein[randint(0, 4)]},'2 '+{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]}"
            l11= f"Snack:{fruit[randint(0, 5)]}"
        elif calories>=2200:
            l6 = f"Breakfast:{protein[randint(0, 4)]},{fruit[randint(0, 5)]}"
            l8 = f"Lunch:{protein[randint(0, 4)]},{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]} "
            l9 = f"Snack:{ps[randint(0, 4)]},{vegetable[0]}"
            l10 = f"Dinner:{protein[randint(0, 4)]},'2 '+{vegetable[0]},'Leafy Greens '+{grains[randint(0,4)]},{taste_en[randint(0,5)]}"
            l11= f"Snack:{fruit[randint(0, 5)]}"
        r=Request.objects.create(user=user,bmi=BMI,height=height,weight=weight,breakfast=l6,lunch=l8,snack=l9,dinner=l10,esnack=l11,healthstat=health,expert=exp,status="requested")
        r.save()
        messages.info(request,"Submitted")
        
    return render(request,"userreq.html",{"data":data})

def userfeed(request):
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    if request.POST:
        feed=request.POST["msg"]
        f=Feedback.objects.create(con=feed,sender=user)
        f.save()
    return render(request,"userfeed.html")


def userpyramid(request):
    uid=request.session["id"]
    id=request.GET.get("id")
    data=Pyramid.objects.get(req__id=id)
    return render(request,"userpyramid.html",{"data":data})


def superfeed(request):
    data=Feedback.objects.all()
    return render(request,"superfeed.html",{"data":data})


def userviewreq(request):
    uid=request.session["id"]
    data=Request.objects.filter(user__id=uid)

    return render(request,"userviewreq.html",{"data":data})