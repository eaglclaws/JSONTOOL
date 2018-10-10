# JSONTOOL
JSON 파일을 수정하고 불러오는 함수를 정리한 모듈

##사용 방법
###초기화
JSONTOOL은 ProductDatabase 인스턴스를 이용하여 JSON 파일을 수정 및 불러오기르 합니다. 사용은 다음과 같이 합니다.
```
import JSONTOOL
mainDB = ProductDatabase("DB.json")
```
ProductDatabase의 생성자는 사용하 JSON 파일명을 매개변수로 받습니다.
###제품 정보 열람
데이터베이스에 저장되어 있는 정보를 열람하 수 있습니다.

**제품을 dict 객체로 받아오기**
```
product1 = mainDB.getproduct("productname")
```
원하는 제품의 이름에 해당하는 데이터를 dict 객체로 받아옵니다.

**제품의 모든 정보를 str로 받아오기**
```
product1info = mainDB.getinfo("productname")
```

**제품의 특정 정보를 str로 받아오기**
 ```
 product1laundryinfo = mainDB.getinfo("productname", "laundry")
 ```
 
 ###데이터 수정
 **단일 추가**
 ```
 mainDB.additem(item)
 ```
 
 **item 객체의 형식**
 ```
 item = {"name" : "productname", "info" : { "manufacturer" : "companyname", "price" : price, "laundry" : ["code1", "code2"], "allergens" : ["allergen1", "allergen2"]}}
 ```
 
**복수 추가**
```
mainDB.additems(stream.txt)
```

**stream.txt**
```
productname, companyname, price, code1;code2, allergen1;allergen2
productname1, companyname1, price1, code1;code2;code3, allergen1;allergen2;allergen4
```
