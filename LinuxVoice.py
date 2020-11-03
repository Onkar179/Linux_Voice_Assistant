import speech_recognition as sr
import pyttsx3
import webbrowser 


pyttsx3.speak('Hey Onkar')
pyttsx3.speak('I Am your personal voice assistant')
pyttsx3.speak('How can I help you')

while True:
   print()
   print("\t \t \t I am listening : ", end='')

   r = sr.Recognizer()

   with sr.Microphone() as source:
      pyttsx3.speak('start saying ...')
      audio = r.listen(source)
      pyttsx3.speak('i got it... please wait..!!')

   ch = r.recognize_google(audio)

   if("hello" in ch) or ("hi" in ch) or ("hey" in ch):
     pyttsx3.speak("Hello Onkar ..How are you  ..?")
   elif("fine" in ch) or ("What" in ch) or ("about" in ch):
     pyttsx3.speak("I am good ...")
   elif("How" in ch) or ("help" in ch) and ("me" in ch):
     pyttsx3.speak("I can help you in following ways..")
     pyttsx3.speak("running linux commands ...")
     print()
     print("*******************************************Linux Commands***********************************************************")
     pyttsx3.speak("running basic networking commands ...")
     print()
     print("*******************************************Networking Commands********************************************************")
     pyttsx3.speak("running docker commands...")
     print()
     print("*******************************************Docker Commands**********************************************************")
     pyttsx3.speak("running Hadoop commands ...") 
     print() 
     print("*******************************************Hadoop Setup*************************************************************")
   elif("command" in ch) or ("date" in ch):
     pyttsx3.speak("Running date command .....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=date")  
   elif("display" in ch) and ("cal" in ch):
     pyttsx3.speak("Running cal command ......")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=cal")  
   elif("ip" in ch) or ("host" in ch):
     pyttsx3.speak("Running ifconfig command .....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=ifconfig")  
   elif("please" in ch) or ("interfaces" in ch):
     pyttsx3.speak("Running netstat command ......")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=netstat")
   elif("amount" in ch) or ("RAM" in ch):
     pyttsx3.speak("Showing the amount of RAM usage ......")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=free%20-m")
   elif("are the httpd" in ch) or ("httpd" in ch):
     pyttsx3.speak("Checking the status of  httpd services ....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=systemctl%20status%20httpd")
   elif("is firewall active " in ch) or ("firewall" in ch):
     pyttsx3.speak("Checking the status of firewall services .....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=systemctl%20status%20firewalld")
   elif("dnf" in ch) or ("packages" in ch):
     pyttsx3.speak("Running dnf list command .....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=dnf%20list")   
   elif("list" in ch) or ("python" in ch) or ("modules" in ch):
     pyttsx3.speak("Running pip3 list command ......")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=pip3%20list") 
   elif("docker is installed" in ch):
     pyttsx3.speak("Running rpm -q command ...")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=rpm%20-q%20docker-ce")
   elif("docker" in ch) or ("status" in ch):
     pyttsx3.speak("Checking the status of docker services ....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=systemctl%20status%20docker")
   elif("show me downloaded " in ch) or ("downloaded" in ch) or ("docker images" in ch):
     pyttsx3.speak("Running docker images command ...")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20images%20-a")
   elif("launch" in ch) or ("centos" in ch):
     pyttsx3.speak("Launching docker container of centos image ....")    
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20run%20-dit%20--name%20os1%20centos")
   elif("verify" in ch):
     pyttsx3.speak("Running docker ps command ....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20ps%20-a")
   elif("details" in ch) or ("give" in ch):
     pyttsx3.speak("Running docker inspect command ....")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20inspect%20os1")
   elif("shut" in ch) or ("down" in ch) :
     pyttsx3.speak("Running docker stop command ...")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20stop%20os1")
   elif("delete" in ch) or ("remove" in ch):
     pyttsx3.speak("Running docker rm command ...")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=docker%20rm%20os1")
   elif("software" in ch) or ("hadoop" in ch) or ("is" in ch) :
     pyttsx3.speak("Hadoop software is installed ...")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=hadoop%20version")
   elif("start" in ch) or ("hadoop" in ch) :
     pyttsx3.speak("Starting hadoop services .......")
     webbrowser.open("http://192.168.43.249/cgi-bin/onkar.py?x=hadoop-daemon.sh%20start%20namenode")
   elif("take" in ch) or ("me" in ch):
     pyttsx3.speak("Taking you to the hadoop web console report......")
     webbrowser.open("http://192.168.43.249:50070")
   else:
     pyttsx3.speak("Ok I hope you like my service ....Have a good day ..")
     
     