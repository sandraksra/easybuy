# easybuy


•	This is a project with the objective to  develop a 
         basic website where a consumer is provided  
         with a shopping cart application.
         
         
•	And also to know about the technologies used to
         develop such an application.
         
         
•	This document will discuss each of 
         underlying technologies to create and 
         implement an e-commerce website.



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
             
             
![home page_sislaf](https://user-images.githubusercontent.com/119956082/207924869-518badfc-c5d6-4a13-9a56-8838b8597f4d.png)
![registration_sislaf](https://user-images.githubusercontent.com/119956082/207925420-6a61d704-bf97-4c9e-a7eb-f97edbcb2ad1.png)
![login_sislaf](https://user-images.githubusercontent.com/119956082/207925807-78be9944-1530-47ae-a394-8bf0915613cb.png)
![cart details_sislaf](https://user-images.githubusercontent.com/119956082/207925884-8f31164c-e677-4216-b01c-a499cdabdbbd.png)
![cart_sislaf](https://user-images.githubusercontent.com/119956082/207925921-61339533-7028-4618-b7e4-d1c082f3d6d5.png)


