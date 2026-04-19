# Logical Operators [20 min] (1)

In the Last class we learned about conditional statements, which says that if one condition is
true then do X otherwise do Y.

**For Example:** In traffic lights, If the lights are green then Move, and if the lights are red
then Stop.
But In reality, there might be multiple conditions on which some result depends.

**For Example:** Suppose I need to submit some documents in Masai, and the documents
are my PAN card and License ID then only I will get admission.
here, you can observe that I will only get admission when I have the PAN Card
and License ID (Both are important).

### **1. AND Operator:**

| PAN Card | License ID | Admission | Output |
| --- | --- | --- | --- |
| True | False | False | I will not get admission if I have the PAN Card but not the License ID. |
| False | True | False | I will not get admission if I do have not a PAN Card but
have License Id. |
| False | False | False | I will not get the admission if neither I have the PAN Card nor
the License Id. |
| True | True | True | will not get the admission if I have the PAN Card as well as
License Id. |

Similarly, we can have multiple conditions on which, the result is dependent. 

- Our Boolean operators take the input values as boolean and produce the result in boolean.
- In programming, we denote the AND operator in this way `&&`.
- `<Input (Boolean Value) > &&  <Output (Boolean Value)>`

> 💡*When we use logical AND* `**(&&)**`, *Javascript either returns the first falsey value it finds, else if all the operands are truthy, it returns the last truthy value.*
> 

> *in other words, logical AND* **`(&&)`** *is eager to find one falsy value, once it finds it - it happily returns. It does not even look any further. But if it does not find any - with lots of sadness it returns the last truthy value.*
> 

- **Code 1: AND Operator**
    
    ```jsx
    var a = true;
    var b = true;
    var c = a && b;
    console.log(c);
    a = true;
    b = false;
    console.log(a&&b);
    a = false;
    b = true;
    console.log(a&&b);
    a = false;
    b = false;
    console.log(a&&b);
    ```
    
- **Code 2: AND with numbers**
    
    ```jsx
    var a = 5>3;
    var b = 6>3;
    var c = a && b;
    console.log(c);
    ```
    
- **Code 3: if/else**
    
    ```jsx
    // Ist Part: Without AND
    if(5>3)
    {
    if(6>3)
    {
    console.log("Both are true");
    }
    }
    // IInd Part: With AND
    if(5>3 && 6>3)
    {
    console.log("Both are true");
    }
    ```
    
- **Code 4: Combination of multiple statements**
    
    ```jsx
    // Try out on Console
    (5<4) && (3>1) && (2>1) && (4<1)
    ```
    
- **[Student Task] Check whether Rahul passed or not**
    
    ```jsx
    // For English Subject, Check whether Rahul passed or not
    var subject = "english";
    var passing_marks = 70;
    var rahul_marks = 75;
    var rahul_subject = "english";
    if((rahul_subject == subject) && (rahul_marks >= passing_marks))
    Logical Operators 4
    {
    console.log("Rahul Passed");
    }
    else
    {
    console.log("Rahul not passed");
    }
    ```
    
- **Code 5 : [Student Task] Marriage Problem**
    
    
    Gender is male and `age ≥ 21` : He can marry
    Gender is female and `age ≥ 18` : She can marry
    
    ```jsx
    var gender = "male";
    var age = 21;
    if((gender == "male") && (age >= 21))
    {
    console.log("Male : Can Marry");
    }
    else if((gender == "female") && (age >= 18))
    {
    console.log("Female : Can Marry");
    }
    else
    {
    console.log(gender,"Can't get Marry");
    }
    ```
    
- **Code 6 : Differentiate between ,(coma) and +**
    
    ```jsx
    var a = 2;
    var b = 3;
    var c = "hello";
    console.log(a,b,c);
    console.log(a+b+c);
    
    // Case 2 : Integers
    var a = 2;
    var b =. 3;
    console.log(a+b);
    console.log(a,b);
    // Case 3 : Strings
    var a = "Hello";
    var b = "World";
    console.log(a+b);
    // Case 4 : Integer with Strings
    var a = 2;
    var b = "hello";
    console.log(a,b);
    console.log(a+b);
    // Case 5 : "\n"
    var a = 2;
    var b = "hello";
    console.log(a,"\n",b);
    ```
    
- **Code 7:**
    
    **Mom wants to make Palak Paneer, So he sends Sunny to the shop to buy
    palak and paneer.
    Since She asked for palak paneer. In this case, both items palak and paneer are
    required to make palak paneer, if any of the item is not available in the shop then it is
    not possible to make a palak paneer dish.**
    
    ```jsx
    var palak_availaible = false;
    var paneer_availaible = false;
    if(paneer_availaible && palak_availaible)
    {
    console.log("Today, we will have a party");
    }
    else
    {
    Logical Operators 6
    console.log("No Party");
    }
    ```
    
- **Examples**
    
    ```jsx
    let a = 'Prachi';
    let b = 'Vivek';
    let c = 'Rishi';
    
    let z = a && b && c;
    
    console.log(z);
    ```
    
    ```jsx
    let a = 0;
    let b = 'Vivek';
    let c = 'Rishi';
    
    let z = a && b && c;
    
    console.log(z);
    ```
    
    ```jsx
    let bankbalance = 100;
    let accountactive = true;
    
    (bankbalance > 0) && (accountactive) && console.log('active');
    ```
    
    ```jsx
    let bankbalance = 100;
    let accountactive = false;
    
    (bankbalance > 0) && (accountactive) && console.log('not active');
    ```
    

### **2.  OR Operator ||**

If any of the statement is true, then the result will be true

**For Example:** DriveZy is a Renting bike service Startup, If you want to rent a bike then
you need to submit any of the Identity Documents
Aadhar Card or PAN Card or License or voter ID Card

| Aadhar Card | PAN Card | License | Voter ID card | Result |
| --- | --- | --- | --- | --- |
| true | true | true | true | true |
| true | true | true | false | true |
| true | true | false | false | true |
| true | false | false | false | true |
| false | false | false | false | false |

and many more cases are possible

> 💡*When we use logical OR* `**(||)**` *, javascript looks for the first truthy value and returns it as soon as it finds it. If it does not find any truthy value, it returns the last falsy value it finds.*
> 

> *in other words, logical OR* **`(||)`** *is eager to find one truthy value, once it finds it - it happily returns. It does not even look any further. But if it does not find any - with lots of sadness it returns the last falsey value.*
> 

- **Code 8: OR Operator**
    
    ```jsx
    var a = true;
    var b = true;
    var c = a || b;
    console.log(c);
    a = true;
    b = false;
    console.log(a||b);
    a = false;
    b = true;
    console.log(a||b);
    a = false;
    b = false;
    console.log(a||b);
    ```
    
- **Code 9 : [Student Task ] OR Operator**
    
    ```jsx
    1. true || false || true
    2. false || true || false
    3. false || false || true
    ```
    
- **Code 10 :**
    
    Mom wants to prepare something for dinner, but she decide that either the
    will make Potato or Paneer, So she send Sunny to the shop to buy potato or
    paneer.
    
    Since , Either she will prepare potato or panner in the dinner. In this case, if any of the
    item is available in the shop then it is possible to prepare dinner.
    
    ```jsx
    var potato_availaible = true;
    var paneer_availaible = false;
    if(potato_availaible || paneer_availaible)
    {
    console.log("Dinner : Possible");
    }
    else
    {
    console.log("Dinner : Not Possible");
    }
    ```
    
- **Code 11: Marriage Problem**
    
    Male: age≥21
    Female: age≥18
    
    ```jsx
    var gender = "female";
    var age = 18;
    if((gender == "male" && age>=21) || (gender == "female" && age>=18))
    {
    console.log(gender,": Can get Married");
    }
    else
    {
    console.log(gender,": Can't get married");
    }
    ```
    
- **Examples**
    
    ```jsx
    let a = false;
    let b = 0;
    let c = null;
    
    let z = a || b || c;
    
    console.log(z);
    ```
    
    ```jsx
    let a = false;
    let b = 'Vivek';
    let c = 'Rishi';
    
    let z = a || b || c;
    
    console.log(z);
    ```
    
    ```jsx
    let defaultUser = "Vivek";
    let user = "Akash"
    console.log(defaultUser || user)
    ```
    
    ```jsx
    let defaultUser = false;
    let user = "Akash"
    console.log(defaultUser || user)
    ```