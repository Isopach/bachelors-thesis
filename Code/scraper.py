import xlsxwriter
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
workbook = xlsxwriter.Workbook("permissions.xlsx")
worksheet = workbook.add_worksheet()


with open("package.txt","r") as package_file:
    package_names = package_file.readlines()

results = {}
row = 0
col = 0
for p_name in package_names:
    row += 1
    col = 0
    id = p_name

    url = "https://play.google.com/store/apps/details?id="+id
    driver.get(url)
    checker = 4
    while (True):
        try:
            element = driver.find_element_by_css_selector(
                "#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > c-wiz:nth-child(" + str(
                    checker) + ") > div > div.JHTxhe > div > c-wiz > div > span > div > span > div > a")
            print ("****************" + str(element.text).strip())
            if (str(element.text).strip() == "View details"):
                print "************Found"
                element.click()
                break
        except:
            checker -= 1
    time.sleep(5)
    new_element = driver.find_element_by_css_selector("#yDmH0d > div.llhEMd.bYEzqc.iWO5td > div > div.g3VIld.LhXUod.t89eC.Up8vH.J9Nfi.iWO5td")

    sttr = new_element.text
    str_list = sttr.split("\n")
    print str_list
    key = "perm"
    results[key] = []
    for i in range(1,len(str_list)):
        list_line = str_list[i].split(" ")
        if(len(list_line) > 1 and not str_list[i].__contains__("&") and
               not str_list[i].__contains__("/") and not str_list[i].__contains__("In-app purchases")
           and not str_list[i].__contains__("Wi-Fi connection information")):
            results[key].append(str_list[i])
        else:
            key = str_list[i]
            results[key] = []
    worksheet.write(row,col,p_name)
    for ke in results:
        col += 1
        new_str = ""
        new_str += (ke + ":   ")
        worksheet.write(row, col, new_str)
        for value in results[ke]:
            col += 1
            worksheet.write(row, col, value)


    results = {}
workbook.close()
driver.close()