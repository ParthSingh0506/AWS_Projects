# This web app predicts whether a patient's cancer is Benign or Malignant and it is deployed on AWS.
### If you don't know about AWS or you want to understand this project in depth refer this article that I wrote:- https://www.analyticsvidhya.com/blog/2022/05/creating-an-ml-web-app-and-deploying-it-on-aws/
## __Follow these steps for deploying and running this

1. First create an EC2 instance 
2. Download these all files using wget and place them inside your ec2 like this
   "wget https://raw.githubusercontent.com/ParthSingh0506/AWS_Projects/main/ML-WebApp/web_app.py"
 (You can also put all these files in S3 and copy them inside your EC2, but it is very time consuming.)
 
 ![image](https://user-images.githubusercontent.com/36064077/166891354-5ed22be3-6033-45b9-95ed-e5b913aadd44.png)

3. ## Install this python library
   pip install streamlit -y
 
4. ## After library is installed succefully run this
  streamlit run web_app.py
  ![image](https://user-images.githubusercontent.com/36064077/166892016-0dedb11d-214b-4dbd-aa23-a47b5518fabe.png)
  
## The web site is now running on two IP's copy any IP and paste that in new tab.
![image](https://user-images.githubusercontent.com/36064077/166892597-76721653-d8a3-4d79-b0ce-532c774c42c0.png)
