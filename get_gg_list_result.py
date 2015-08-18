import time
from splinter import Browser

def splinter(url,browser):
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    browser.find_by_id('idInput').fill('xxxxxx')
    browser.find_by_id('pwdInput').fill('xxxxx')
    #click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(8)
    #close the window of brower
    
def getAll(browser):
    element_list = browser.find_by_id("ires")
    rel = element_list.find_by_tag('h3')
    for i in rel:
        print i.find_by_tag("a").text
        e = i.find_by_tag("a")
        print  e['href']   #ok!!
        data.append(e["href"])

def visitGG(url,text):
    browser.visit(url)
    time.sleep(2)
    browser.fill('q',text)
    browser.find_by_name('btnK').click()
    if browser.is_text_present(text):
        print 'yes, found it'
    else:
        print 'no. didn t find it'
        
    getAll(browser)
    print data
    print "next page ========="
    #next page
    browser.find_by_id('pnnext').click()
    time.sleep(2)
    if browser.is_text_present(text):
        print 'yes, found it'
    else:
        print 'no. didn t find it'
    getAll(browser)
    print data
    
def visitFB(url):
    #1. visit
    browser.visit(url)
    time.sleep(2)
    #2. common
    

if __name__ == '__main__':
    data=[]

    browser = Browser('chrome')
    text = "pet site:facebook.com"
    visitGG("http://www.google.com",text)
    
    time.sleep(2)
    
    for i in data:
        print "start action"
        visitFB(i)
        
          
    #websize3 ='http://www.126.com'
    #splinter(websize3)
    
    #browser.quit()
