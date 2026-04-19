# assignment

# 1: create a counter app using setInterval like the given image below.

```jsx
font-family: clockicons,sans-serif;
```

![Untitled](../callback%20function-error%20handling%20with%20callback%20%5B12%20cf4e97b75a5342cc88d0b972fc9c3498/assignment%20e1a289cf7a4444a98fc687befdccd73d/Untitled.png)

![Untitled](../callback%20function-error%20handling%20with%20callback%20%5B12%20cf4e97b75a5342cc88d0b972fc9c3498/assignment%20e1a289cf7a4444a98fc687befdccd73d/Untitled%201.png)

## Features:

- The user able to start the counter
- The user able to stop the counter
- The user able to reset the counter

### Create a function called `Multiplier` that will take an `array` ,`value`  & `a callback function` as `parameters` and after 2 seconds return one array of the same length as the input array multiplying each element of the array by the given number.

### Create a function called `findOdd` that will take an `array` & `a callback function` as `parameters` and after 2 seconds return one array having odd elements in it.

### Create a function called `findSum` that will take an `array` & `a callback function` and after 2 seconds return the sum of all the elements in the array.

### Now use all these functions to solve this:

```jsx
 let arr =[1,2,3,4,5,6,7,8];

//First, multiply each item by 3;

[3,6,9,12,15,18,21,24]

//Then filter out the odd elements

[3,9,15,21]

//Now find the sum

48
```

```jsx
function Multiplier(arr,value,callback){
  //write your code here
}

function FindOdd(arr,callback){
    //write your code here
}

function FindSum(arr,callback){
   //write your code here
}

//invocation of all the functions to get the final output
 let arr =[1,2,3,4,5,6,7,8];

Multiplier(arr,3,(value1)=>{
	FindOdd(value1,(value2)=>{
		FindSum(value2,(value3)=>{
			 console.log("My final answer is ",value3)
		})
  })
})

```

### callback with error handling:

 create a function `CodingScoreCheck` that will take a `marks array` of 3 coding evaluations, `cutOfmarks`, and a `callback function.`
it will calculate the `average score` of all the 3 evaluations combined and if the average marks is greater than or equal to the cut-off marks then it will invoke the callback function after `2 seconds` with the average marks as value and null as there is no error. 
If the score is below the cut-off then invoke the callback with `null` as value and  the error message `"Sorry you didn't clear the coding round."`

Create a function called `hukumuScoreCheck` that will take an `array` of marks of 2 HUKUMU interviews,`cutofMarks`, and a `callback function`.
it will calculate the `average score` of all the 2 HUKUMU interviews and if the average mark is greater than or equal to the cut-off marks then it will invoke the callback function after `2 seconds` with the average marks as value and null as there is no error. 
If the score is below the cut-off then invoke the callback with `null` as value and  the error message `"Sorry you didn't clear the HUKUMU round."`

create a function called `UnitMovememtCheck` that will take the `averageCodingScore`, `averageHUKUMUScore`, `cutOfScore`, and a `callback function`.
if the `average` of both coding and HUKUMU is greater than or equal to the cut-off score then invoke the callback function after `2 seconds` with the string `"Congradulation you are getting promoted to the next unit!"` as value and `null` as an error.
else invoke the callback with `null` as value and the string `"Sorry you didn't clear the unit"` as an error message

```jsx

function CodingScoreCheck(codingMarksArray,cutOfmarks,callback){
//Write your code here
}

function hukumuScoreCheck(hukumuMarksArray,cutOfmarks,callback){
//Write your code here
}

function UnitMovememtCheck(averageCodingScore,averageHUKUMUScore,cutOfScore,callback){
//Write your code here
}

//function invocation...
CodingScoreCheck([6,7,6],6,(value1,error)=>{
  if(value1){
    hukumuScoreCheck([5,7],5,(value2,error)=>{
      if(value2){
        UnitMovememtCheck(value1,value2,6.5,(value,error)=>{
          if(value){
            console.log(value);
          }
          else{
            throw new Error(error);
          }
        })
      }
      else{
          throw new Error(error);
      }
    })
  }
  else{
    throw new Error(error)
  }
})
```