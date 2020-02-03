########################         Instructions             #####################################
# cmd0- Facebook/mmt/anything
# cmd1- click fourth link
# cmd2- click linkname
# cmd3- go back
# cmd4- go forward
# cmd5- Reload page
# cmd6- google search ---

from selenium import webdriver
import time
import link
import v2t
import linkname
import t2v
# import getbtn
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chromeoptions)
while True:
    t2v.speechTrans("What do you want to see in browser: ")
    # print("Enter what you want to see in browser: ")
    query = v2t.stot()
    
    if(query!="Voice not recognised Speak again"):
        t2v.speechTrans("You said"+query)
        break
    else:
        t2v.speechTrans("Voice not recognised Speak again")
driver.get("https://www.google.com/?#q="+query)
driver.maximize_window()
numbers=['first','second','third','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th']
nav=["back","forward"]
while True:
    # print("Enter what to do: ")
    t2v.speechTrans("Okay, what next: ")
    ins = v2t.stot()
    if(ins=="Voice not recognised Speak again"):
        t2v.speechTrans("Voice not recognised Speak again")
    else:
        t2v.speechTrans("You said"+ins)
    b=ins.split(' ')
    linkele = linkname.getLinkname(driver)
    linktext = [i.text.lower() for i in linkele]
    # btnsele = getbtn.getBtn(driver)
    # btntext = [i.text.lower() for i in btnsele]
    print(" ".join(b[1:]).lower())
    if 'reload' in b:
        driver.refresh()
    elif 'back' in b:
        driver.back()
    elif 'forward' in b:
        driver.forward()  
    elif " ".join(b[1:]).lower() in linktext:
        linkele[linktext.index((" ".join(b[1:])).lower())].click()
    elif b[1].lower() in numbers:
        link.clickLink(driver,numbers.index(b[1]))
    elif "google search" in " ".join(b).lower():
        driver.get("https://www.google.com/?#q="+" ".join(b[b.index('search')+1:]))
    # elif " ".join(b[1:]).lower() in btntext:
    #     btnsele[btntext.index(" ".join(b[1:]))].click()

    ###Todo-Work on btns
    else:
        t2v.speechTrans("Action Not Recognized")