# easybuy
link:easybuy.pythonanywhere.com
 This is a project with the objective to develop abasic website where a consumer is providedwith a shopping cart application. 
 And also to know about the technologies used todevelop such an application. This document will discuss each ofunderlying technologies to create andimplement an e-commerce website

  admin
*********
tables
:catagory
category includes which type of categories we wants about food.
:products
proucts can add with description, price ,if its available or not
      
django-admin startproject easybuy-
                                 -settings
                                 -urls
                          
django-admin startapp shop-
                          -models
                          -urls
                          -views
                          -admin
django-admin startapp cart-
                          -models
                          -urls
                          -views
                          -admin
                          -contextprocessor
django-admin startapp  account -
                               -urls
                               -views
                               
python maange.py migrate

mk dir template-
               -base.html
               -cart.html
               -index.html
               -item.html
               -login.html
               -register.html
               -search.html      
mk dir static-cr
             -pr
             -hm

