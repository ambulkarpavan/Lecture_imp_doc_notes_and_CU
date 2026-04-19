# assignment

### Guidelines:

- create one `.js file` in the `Masai repo` and solve it.
- after solving the assignment push your code to `GitHub`.
- share the `GitHub Link` in the assignment.
- all the `methods` should be attached to the `prototype object` of their respective `constructor functions`.

## Question 1:

Implement a class hierarchy using constructor functions that model a vehicle. The hierarchy should include three constructor functions: **`Vehicle`**, **`Car`**, and **`ElectricCar`**. The **`Car`** constructor should inherit from **`Vehicle`**, and **`ElectricCar`** should inherit from **`Car`**. Each constructor should have its own properties and methods, and all constructors should use the **`.call`** method to properly set the context for inheritance.

Your task is to implement the constructors and demonstrate the inheritance chain by creating instances of each constructor and accessing their properties and methods.

1. **Vehicle:**
    - Properties:
        - Manufacturer: The company that produced the vehicle.
        - Model: The specific model name or number of the vehicle.
        - Year: The manufacturing year of the vehicle.
        - Color: The color of the vehicle.
        - LicensePlate: The license plate number of the vehicle.
        - Mileage: The total mileage of the vehicle.
        - FuelType: The type of fuel the vehicle uses (e.g., gasoline, diesel).
    - Methods:
        - start(): Starts the engine of the vehicle.
        - stop(): Stops the engine of the vehicle.
        - accelerate(speed): Accelerates the vehicle to the specified speed.
        - brake(): Applies the brakes to slow down or stop the vehicle.

1. Car (inherits from Vehicle):
    - Additional properties:
        - NumDoors: The number of doors the car has.
        - NumSeats: The number of seats available in the car.
    - Additional methods:
        - lock(): Locks the doors of the car.
        - unlock(): Unlocks the doors of the car.
        - adjustSeatPosition(position): Adjusts the position of the seat in the car.
        - playMusic(): Starts playing music in the car.
2. ElectricCar (inherits from Car):
    - Additional properties:
        - BatteryCapacity: The capacity of the electric car's battery.
        - ChargeLevel: The current level of charge in the battery.
    - Additional methods:
        - charge(): Charges the electric car's battery.
        - checkChargeLevel(): Returns the current level of charge in the battery.
        - driveElectric(): Drives the car using electric power.

**Here is the hierarchical tree representation:** 

```jsx
   Vehicle
      |
     Car
      |
 ElectricCar
```

## Question 2:

Create a class hierarchy using constructor functions that model a university system. The hierarchy should include four constructor functions: **`Person`**, **`Student`**, **`Professor`**, and **`TeachingAssistant`**. The **`Student`** constructor should inherit from **`Person`**, and both **`Professor`** and **`TeachingAssistant`** should inherit from **`Person`**. Each constructor should have its own properties and methods, and all constructors should use the **`.call`** method to properly set the context for inheritance. Additionally, each constructor should override the **`toString`** method of **`Person`** to provide a custom string representation. Create instances of each constructor and demonstrate the inheritance chain and custom string representations.

1. Person:
    - Properties:
        - Name: The name of the person.
        - Age: The age of the person.
        - Gender: The gender of the person.
    - Methods:
        - introduce(): Prints a brief introduction of the person.
        - greet(): Prints a greeting from the person.
2. Student (inherits from Person):
    - Additional properties:
        - StudentID: The unique identifier for the student.
        - Major: The field of study or major of the student.
    - Additional methods:
        - enroll(course): Enrolls the student in a particular course.
        - submitAssignment(assignment): Submits an assignment for evaluation.
        - getGrades(): Retrieves the grades of the student.
3. Professor (inherits from Person):
    - Additional properties:
        - EmployeeID: The unique identifier for the professor.
        - Department: The department in which the professor works.
    - Additional methods:
        - teach(course): Conducts a lecture or class for a particular course.
        - gradeAssignment(assignment): Evaluates and assigns grades to an assignment.
        - holdOfficeHours(): Provides a designated time for students to ask questions or seek guidance.
4. TeachingAssistant (inherits from Person):
    - Additional properties:
        - EmployeeID: The unique identifier for the teaching assistant.
        - Course: The course for which the teaching assistant provides assistance.
    - Additional methods:
        - assistProfessor(): Assists the professor during lectures or class activities.
        - provideFeedback(assignment): Provides feedback on an assignment to students.
        - scheduleOfficeHours(): Sets up a schedule for students to visit during office hours.

**Here is the hierarchical tree representation:** 

```jsx
                  Person
                     |
          ---------------------------
          |                          |
          |                    ---------------
          |                    |             |
        Student            Professor   TeachingAssistant  

```

## Question 3:

Implement a class hierarchy using constructor functions that model different types of employees in a company. The hierarchy should include three constructor functions: **`Employee`**, **`Manager`**, and **`Executive`**. The **`Manager`** constructor should inherit from **`Employee`**, and **`Executive`** should inherit from **`Manager`**. Each constructor should have its own properties and methods, and all constructors should use the **`.call`** method to properly set the context for inheritance. Additionally, each constructor should override the **`getSalary`** method of **`Employee`** to provide a custom salary calculation logic. Create instances of each constructor and demonstrate the inheritance chain and custom salary calculations.

1. Employee:
    - Properties:
        - EmployeeID: The unique identifier for the employee.
        - Name: The name of the employee.
        - Age: The age of the employee.
        - Department: The department in which the employee works.
    - Methods:
        - getEmployeeID(): Returns the employee's ID.
        - introduce(): Prints a brief introduction of the employee.
        - performWork(): Simulates the employee performing their work duties.
2. Manager (inherits from Employee):
    - Additional properties:
        - TeamSize: The number of employees managed by the manager.
        - Reports: A list of employees who report to the manager.
    - Additional methods:
        - assignTask(task, employee): Assigns a task to a specific employee.
        - conductMeeting(): Conducts a meeting with the manager's team.
        - reviewPerformance(employee): Reviews the performance of a specific employee.
3. Executive (inherits from Manager):
    - Additional properties:
        - StockOptions: The number of stock options granted to the executive.
        - ExecutiveLevel: The level or rank of the executive within the organization.
    - Additional methods:
        - makeStrategicDecisions(): Makes strategic decisions for the organization.
        - approveBudget(): Reviews and approves the budget for various departments.
        - representCompany(): Represents the company in external meetings or events.

**Here is the hierarchical tree representation:** 

```jsx
                   Employee
                       |
                     Manager          
                       |
                   Executive

```

## Question 4:

Create a class hierarchy using constructor functions that model different types of animals. The hierarchy should include four constructor functions: **`Animal`**, **`Mammal`**, **`Bird`**, and **`Fish`**. The **`Mammal`** constructor should inherit from **`Animal`**, and both **`Bird`** and **`Fish`** should inherit from **`Animal`**. Each constructor should have its own properties and methods, and all constructors should use the **`.call`** method to properly set the context for inheritance. Additionally, each constructor should override the **`sound`** method of **`Animal`** to provide a custom sound representation. Create instances of each constructor and demonstrate the inheritance chain and custom sound representations.

1. Animal:
    - Properties:
        - Species: The species of the animal.
        - Habitat: The natural habitat of the animal.
    - Methods:
        - eat(): Simulates the animal eating.
        - sleep(): Simulates the animal sleeping.
        - makeSound(): Produces the characteristic sound of the animal.
2. Mammal (inherits from Animal):
    - Additional properties:
        - FurColor: The color of the mammal's fur.
        - Diet: The diet or feeding habits of the mammal.
    - Additional methods:
        - giveBirth(): Simulates the mammal giving birth to offspring.
        - nurseOffspring(): Provides nourishment to the mammal's offspring.
        - groom(): Cleans and maintains the mammal's fur.
3. Bird (inherits from Animal):
    - Additional properties:
        - FeatherColor: The color of the bird's feathers.
        - Wingspan: The wingspan of the bird.
    - Additional methods:
        - fly(): Simulates the bird flying.
        - buildNest(): Constructs a nest for breeding or shelter.
        - migrate(): Undertakes seasonal migration for breeding or food.
4. Fish (inherits from Animal):
    - Additional properties:
        - WaterType: The type of water (e.g., freshwater, saltwater) the fish inhabits.
        - Fins: The number and arrangement of fins on the fish.
    - Additional methods:
        - swim(): Simulates the fish swimming.
        - breatheUnderwater(): Utilizes gills to extract oxygen from the water.
        - layEggs(): Deposits eggs for reproduction.

**Here is the hierarchical tree representation:** 

```jsx
                       Animal
                          |
          --------------------------------
          |               |              |
        Mammal            Bird         Fish  

```

## Question 5:

Implement a class hierarchy using constructor functions that model a social media platform. The hierarchy should include five constructor functions: **`User`**, **`RegularUser`**, **`Influencer`**, **`AdminUser`**, and **`SuperAdminUser`**. The **`RegularUser`** constructor should inherit from **`User`**, **`Influencer`** should inherit from **`User`**, **`AdminUser`** should inherit from **`RegularUser`**, and **`SuperAdminUser`** should inherit from **`AdminUser`**. Each constructor should have its own properties and methods, and all constructors should use the **`.call`** method to properly set the context for inheritance.

Your task is to implement the constructors and demonstrate the inheritance chain by creating instances of each constructor and accessing their properties and methods.

This hierarchy is designed to model a social media platform where different types of users have different levels of access and privileges.

1. User:
    - Properties:
        - Username: The username of the user.
        - Email: The email address of the user.
        - Password: The password of the user.
    - Methods:
        - login(): Simulates the user logging into the system.
        - logout(): Simulates the user logging out of the system.
        - updateProfile(): Allows the user to update their profile information.
2. RegularUser (inherits from User):
    - Additional properties:
        - DateOfBirth: The date of birth of the regular user.
        - Interests: A list of the user's interests.
    - Additional methods:
        - postContent(content): Allows the regular user to post content.
        - likePost(post): Allows the regular user to like a post.
        - followUser(user): Allows the regular user to follow another user.
3. Influencer (inherits from User):
    - Additional properties:
        - SocialMediaPlatform: The primary social media platform used by the influencer.
        - Followers: The number of followers the influencer has.
    - Additional methods:
        - createContent(): Allows the influencer to create and publish content.
        - engageWithFollowers(): Engages with the influencer's followers through comments or messages.
        - analyzeMetrics(): Analyzes the performance metrics of the influencer's content.
4. AdminUser (inherits from RegularUser):
    - Additional properties:
        - AdminLevel: The level or rank of the admin user within the system.
        - Permissions: A list of permissions granted to the admin user.
    - Additional methods:
        - approveContent(content): Allows the admin user to approve user-generated content.
        - deleteContent(content): Allows the admin user to delete user-generated content.
        - manageUsers(): Enables the admin user to manage user accounts and permissions.
5. SuperAdminUser (inherits from AdminUser):
    - Additional properties:
        - SuperAdminRole: The specific role or responsibility of the super admin user.
        - SystemAccessLevel: The level of access to the system granted to the super admin user.
    - Additional methods:
        - performSystemMaintenance(): Performs system maintenance tasks.
        - grantPermissions(user, permissions): Grants permissions to other users.
        - generateReports(): Generates reports on system usage and activity.

**Here is the hierarchical tree representation:** 

```jsx
           User
            |
     ------------------
     |                |
 RegularUser     Influencer
     |                
     |         
     |          
 AdminUser   
     |
     |
SuperAdminUser
```