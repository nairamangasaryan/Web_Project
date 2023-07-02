"""
URL configuration for myFirstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def MyCV_view(request):

    return_html = """
        <html>
        <head>
            <title>CV Naira Mangasaryan</title>
        </head>
        <body style=" background-color: rgb(235, 238, 238);
                        font-size: 15px;">
            <div style="border:2px solid #000; 
                        width: 1020px; 
                        height: 820px;
                        margin-left: auto;
                        margin-right: auto;
                        background-color: #fff;
                        padding: 10px">
                <div style="width: 290px; 
                            height: 800px; 
                            float: left;
                            background-color: rgb(183, 196, 197);
                            padding: 10px;">
                    <img src="https://scontent.fevn7-1.fna.fbcdn.net/v/t1.6435-9/198254972_1657629064431155_2034128988298694889_n.jpg?_nc_cat=110&cb=99be929b-3346023f&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=zpaQYsl-TCoAX_eFcJX&_nc_ht=scontent.fevn7-1.fna&oh=00_AfDFzUZ5WXcuDF0TRZCQ_E-1IMTqho5XqJWKCKBFeQS7Ig&oe=64BBDBC6">
                    <h3 style="color:rgb(57, 74, 95)"><i>Profile</i></h3>
                    <hr>
                    <p style="padding: 10px;"> I am a beginner Python programmer.
                        Now, I am participating in the
                        "Python" course of the AGBU
                        "Women Coders" program, which
                        started on 02.2023. I managed to
                        study: Types and Operations,
                        Functions, Modules, Classes
                        and OOP, Decorator, Iterator and
                        Generator Anonymous
                        Function, File Manipulation.
                    </p>
                    <h3 style="color:rgb(57,74,95)"><i>Contact</i></h3>
                    <hr>
                    <p>email: <i><b>nairamangasaryan@gmail.com</b></i></p>
                    <p>mob:<br> <i><b>+374 93 49 55 44</b></i></p>
                </div>
                <div style="width: 680px; 
                            height: 800px; 
                            overflow: hidden;
                            float: right;
                            background-color: rgb(248, 231, 247);
                            padding: 10px;">

                    <h1 style="color:rgb(68, 23, 53); font-size: 40px;"><i><b>Naira<br>Mangasaryan</b></i></h1>
                    <h3 style="color:rgb(57,74,95); margin-top: 50px;"><i>EDUCATION</i></h3>
                    <hr>
                    <p>
                        Yerevan State University, Faculty of Radiophysics<br>
                        2003-2005<br>
                        Master’s degree<br>
                        <br>
                        Yerevan State University, Faculty of Radiophysics<br>
                        1999 - 2003<br>
                        Bachelor’s degree <br>
                    </p>
                    <h3 style="color:rgb(57,74,95); margin-top: 50px;"><i>WORK EXPERIENCE</i></h3>
                    <hr>
                    <p>
                        Scientist, manager of department<br>
                        Russian-Armenian University<br>
                        Department of Materials Technology and Structure of Electronic Technique<br>
                        2007 – present<br>
                        <br>
                        Research assistant<br>
                        Institute of Applied Problems of Physics of NAS RA<br>
                        2005 - 2007<br>
                    </p>
                    <h3 style="color:rgb(57,74,95); margin-top:50px;"><i>LANGUAGES</i></h3>
                    <hr>
                    <ul>
                        <li> Armenian (native) </li>
                        <li> Russian (good) </li>
                        <li> English (intermediate) </li>
                    </ul>
                </div>
            </div>
        </body>
        </html>
    
    """

    return HttpResponse(return_html)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('MyCV/', MyCV_view)
]
