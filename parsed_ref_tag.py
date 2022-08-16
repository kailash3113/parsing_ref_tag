from bs4 import BeautifulSoup

url_lst = [r'C:\Users\KAILASH\Desktop\work\BJJ-2018-1580.R3.xml',
           r'C:\Users\KAILASH\Desktop\work\BJJ-2019-0337.R1.xml',
           r'C:\Users\KAILASH\Desktop\work\BJJ-2019-0341.xml',
           r'C:\Users\KAILASH\Desktop\work\BJJ-2019-1060.R3.xml',
           r'C:\Users\KAILASH\Desktop\work\BJJ-2019-1112.R1.xml',
           r'C:\Users\KAILASH\Desktop\work\BJO-2021-0126.xml',
           r'C:\Users\KAILASH\Desktop\work\BJO-2021-0143.xml',
           r'C:\Users\KAILASH\Desktop\work\BJO-2022-0092.R1.xml',
           r'C:\Users\KAILASH\Desktop\work\BJR-2019-0122.R1.xml',
           r'C:\Users\KAILASH\Desktop\work\DTB-2020-000040.xml',
           r'C:\Users\KAILASH\Desktop\work\DTB-2020-000056.xml',
           r'C:\Users\KAILASH\Desktop\work\DTB-2021-000013.xml',
           r'C:\Users\KAILASH\Desktop\work\DTB-2022-000011.xml',
           ]

lst1 = []


for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"journal"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst1.append(sample_ele)       
    
with open('journal_reference_type.xml','wb') as k:
    k.write(str(lst1).encode("utf8"))
    

lst2 = []


for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"confproc"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst2.append(sample_ele)       
    
with open('confproc_reference_type.xml','wb') as k:
    k.write(str(lst2).encode("utf8"))
    

lst3 = []


for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"website"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst3.append(sample_ele)       
    
with open('website_reference_type.xml','wb') as k:
    k.write(str(lst3).encode("utf8"))
    
lst4 = []


for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"thesis"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst4.append(sample_ele)       
    
with open('thesis_reference_type.xml','wb') as k:
    k.write(str(lst4).encode("utf8"))

lst5 = []


for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"book"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst5.append(sample_ele)       
        
with open('book_reference_type.xml','wb') as k:
    k.write(str(lst5).encode("utf8"))
    

lst6 = []

for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"software"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst6.append(sample_ele)       
    
with open('software_reference_type.xml','wb') as k:
    k.write(str(lst6).encode("utf8"))
    

lst7 = []

for i in url_lst:
    sample_url = i
    
    with open(sample_url,'r',encoding="utf8") as f:
        data = f.read()
    
    Bs_data = BeautifulSoup(data, "xml")

    b_unique = Bs_data.find_all("ref",attrs={"data-class":"jrnlRefText"})

    b_unique = str(b_unique)

    element_data = BeautifulSoup(b_unique,"lxml")

    sample_ele = str(element_data.find_all("element-citation",attrs={"publication-type":"report"}))

    sample_ele = sample_ele.replace("[","")

    sample_ele = sample_ele.replace("]","")
    
    
    lst7.append(sample_ele)       
    
with open('report_reference_type.xml','wb') as k:
    k.write(str(lst7).encode("utf8"))
