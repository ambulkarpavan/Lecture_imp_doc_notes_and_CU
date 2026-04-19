# Switch Case [15 min] (1)

Whenever we have multiple options and we have a choice.

**For Example:** in an ATM Machine, we have multiple options for Deposit, Withdraw, Changing Pin ,
and others

Every option is connected to some code

| Deposit [ To deposit the money] | Code 1 |
| --- | --- |
| Withdraw | Code 2 |
| Change Pin | Code 3 |
| Default | Code 4 |

In the switch case, there are multiple cases, and with each case, some code is connected.

- **Code 1: Day Schedule**
    
    ```jsx
    var option = 3;
    switch(option)
    {
    case 1 :
    console.log("Day 1 : Scrum + Coding");
    case 2 :
    console.log("Day 2 : Scrum + Coding + Skillathon");
    case 3 :
    console.log("Day 3 : Scrum + Skillathon + Standups");
    default :
    console.log("Holiday");
    }
    ```
    
    - On choosing the option in above code, it will output the code corresponding to the given option and also print the output of all the cases presented below the chosen option.
    - To avoid this, we will use `break`;
    
- **Code 2: Day Schedule [ with Break ]**
    
    ```jsx
    var option = 3;
    switch(option)
    {
    case 1 :
    console.log("Day 1 : Scrum + Coding");
    break;
    case 2 :
    console.log("Day 2 : Scrum + Coding + Skillathon");
    break;
    case 3 :
    console.log("Day 3 : Scrum + Skillathon + Standups");
    break;
    default :
    console.log("Holiday");
    break;
    }
    ```