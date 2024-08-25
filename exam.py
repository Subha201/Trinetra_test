#Unix
'''1. Copy a file one directory to another directory?'''
Ans:- cp file1.txt file2.txt

'''2. How do you find the process IF(PID) of a running process.'''
Ans:- ps -ef | grep process_name

'''3. difference between chown vs chmod?'''
Ans:- chmod:- change file mode
     chown:-change file owner and group.

'''4. In a directory a find a file name abc.txt?'''
Ans:- ls command use ,ls command means list directory content
       ls file name
    ex:- ls abc.txt

'''5. Why we are using sed command?'''
Ans:-sed command is stream editor use for tranforming & flitering text.

'''6.How to list directories in Unix?'''
Ans:-ls ,ls-lt,ls -lrt, ls-lr command
ls is list directory content  use for list check perpose.


#SQL
'''1.Explain about the DML, DDL, TCL, DQL commands?'''
Ans:-
DML:-DATA MANUPULATING LANGUAGE. which is used for data manipulate purpose.
DDL:-DATA DEFINATION LANUAGE. which is used for data modified purpose.
TCL:-TRANSACTION CONTROL LANGUAGE.
DQL:-DATA QUERY LANUAGE

'''2. What is join, explain about the all joins?'''
Ans:- a join clause is used to combine rows from two or more tables.
==> inner join,left join,right join,full join,self join.

'''3. Difference between Joins vs Subquery?'''
Ans:-An joins statement is used to combine data or rows .
    A subquery is a query that is nested inside a select,update,insert.



'''4. Find 3rd Highest Salary Of employee table ?'''
Ans:- selct max(sal) where sal<
               (select max(salary) where sal<(
                select max(sal)
               ))


'''5. Find the top seller in this month, according to date in customer table?'''
Ans:-

'''6. Difference between Rank vs Dense_rank?'''
Ans:-The RANK() function assigns a unique rank to each distinct value in
the result set, but it leaves gaps in the rank sequence when there are
ties (i.e., rows with the same value).
Example:
Salesperson	Sales	Dense_Rank
ram	        500	       1
sita        400	       2
hari	    400	       2
devil	    300	       3

DENSE_RANK()
Definition: The DENSE_RANK() function assigns a unique rank to each distinct
value without leaving gaps in the rank sequence, even when there are ties.
example:
Salesperson	Sales	Rank
ram	        500	      1
sita        400	      2
hari	    400    	  2
devil	    300	      3



#Python Section:-
'''1. What is decorator , write a decorator?'''
Ans:- decorator:- decorator is a function that can modify
the behaviour of another function or methods.
def add(a, b):
    return a + b
result add(a+b)

'''2. What is lambda expression, write a lambda expression?'''
Ans:-  lamda expression means single line code.
Example:-
def powersum (x,y):
 return x**2 + y**2
print(powerofsum(2,3)) #it's  lengthy process so we use lambda expression:-
#lambda expression on the above code:-
powerofsum = lambda x,y: x**2 + y**2
print(powersum(2,3))

'''3. WAF, S = ‘Hello everyone’, count the occurrence of each char, return those
repetitive character , without using any inbuilt function.'''
Ans:-
s= input("enter your string:-")#'hello everyone'
l = list(s)
print(l)

'''4. WAF , Reverse a string words.
> Input = ‘hello world’ > output:- ‘world hello’, without using inbuilt function'''
Ans:-
str="hello world"
words = string.split("")
output = words[-1::-1]
print(output)

'''5. WAF, input= ‘aaabbaacd’ output= ‘3a2b2a1c1d’'''
Ans:-

'''6. Sort a list integer element without using inbuilt function?'''
Ans:-

'''7. Li = [1,2,3,4], Li2 = [10,20,30]
Result = {1:10,2:20,3:30}
Take a two list a parameter, return dictionary, look like above result.'''
Ans:-

'''8. Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
the csv and print in console bar'''
Ans:-

'''9. What is exception handling , how handel the exception in python , explain with each
block'''
Ans:-

'''10. Difference between Moudle and Packages (3 diff)'''
Ans:-
Module:
1.A module is a single Python file
2.Modules are used to define functions, classes, and
variables that can be imported and used in other modules
package:
1.package is a directory that contains multiple Python modules
and a special _init_.py file
2.Packages are used to together multiple modules
and sub-packages into a single namespace
3.Packages require an _init_.py file in their directory

'''11. Difference between List vs tuple vs set vs dictionary?'''
Ans:-
list:-Ordered, mutable, allows duplicates.
ex- my_list = [7, 2, 0, 4]
tuple:-Tuple: Ordered, immutable, allows duplicates.
ex- my_tuple = (1, 2, 3, 4)
set:-Set: Unordered, mutable, no duplicates.
ex- my_set = {1, 2, 3, 4}
dictionary:-Dictionary: Unordered (conceptually), mutable, unique keys with possible duplicate values
ex- my_dict = {'x': 1, 'y': 2, 'z': 3}


'''12. What is Garbage Collection?'''
Ans:-Garbage Collection  is an automatic memory management process
that recycles and deallocates memory that is no longer in use by a program.

'''13. What is list comprehension , write code in list comprehension?'''
Ans:- list comprehension is a short process syntax.
 ex:-
    fruits = ["apple", "banana", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)


'''14. Difference between Shallow copy vs Deep Copy?'''
Ans:-


'''15. Explain break, continue, pass with code?'''
Ans:-
break:

for i in range(10):
    if i == 5:
        break
        print(i)
print("Loop has to be exit ")
continue:

for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
print("Loop completed")

pass:

for i in range(5):
    if i % 2 == 0:
        pass else:
        print(i)
print("Function and loop completed.")


#Selenium

'''1. What is webdriver?'''
Ans:- webdriver is a tool which is use for automate the web browser functionality.

'''2. How to handel selective dropdown, write a snippet for it?'''
Ans:-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
search_boxes = driver.find_elements(By.XPATH, "//input[@type='text']")
if search_boxes:
   search_box = search_boxes[0]
   search_box.send_keys(" i phone ")


'''3. How to handel auto suggestive dropdown, write a snippet for it.?'''
Ans:-


'''4. How to handel multiple windows and back to current window?'''
Ans:-


'''5. What StaleElementException?'''
Ans:-


'''6. Explain the wait mechanism, write syntax and snippet for it.'''
Ans:- wait mechanism 2 types:-
implicit wait(),explicit wait()



'''7. How to handle dynamic web element, (write at least 3 point)'''
Ans:- By using explicit wait.


'''8. How many locators in selenium'''
Ans:-8 types of locators:-
 ID, Name, Class Name , tag name,
link text , partial link text,
Xpath, css selector


'''9. In web table want to fetch 3rd Column , 3rd row data, write a xpath for it'''
Ans:-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)
table = driver.find_element(By.XPATH,'(//table*[@id="product"])[1]')
#time.sleep(3)
rows = table.find_elements(By.TAG_NAME,value:'tr')
print(len(rows))

heading = table.find_elements(By.TAG_NAME,value:'th')
for v in heading:
    print(v.text)


'''10.Write xpath Steps.1.Navigate to
    https: // www.nseindia.com /'''
Ans:-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//table[@id='livePreTable']/tbody/tr[2]/td[3]").click()
time.sleep(5)
