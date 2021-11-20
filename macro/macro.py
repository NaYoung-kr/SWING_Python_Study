from selenium import webdriver

path = "C:/Users/msi/PycharmProjects/python/SWING_Python_Study/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://zzzscore.com/1to50/")

for i in range(1,51):
    for j in range(1,26):
        btn = driver.find_element_by_xpath('//*[@id="grid"]/div[' + str(j) + ']')
        if (str(i) == btn.text):    # 일치하면 해당 버튼을 클릭한 뒤, 첫 번째 버튼으로 초기화
            btn.click()
            j = 1
