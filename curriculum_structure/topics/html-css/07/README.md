# Self learning with GEN AI (Advanced) (20mins)

Context

- Role `Act as....`
- Format `tabular, pointwise, withing... DUBX`, use relevant examples, use real-world examples, use simple to visualize analogies
- As Specific as possible
- I am a fresher, Teach it to an 8 years old,

- Prompt engineering basics
- Important considerations
    - Treat it like a mentor not as a cheating buddy
    - Write code yourself until you master them, do not copy paste - else GEN AI will mess up your live coding round, make the code clean and easy to maintain,
    - Please don’t try to use it during any live interviews or evaluations
- Student task - ensure that everyone has an openAI account
- Student tasks - everybody shares their screen and takes the help of GEN AI to master a concept and test their knowledge [optional]

## **ChatGPT's Guide to Engineering Prompts**

🔍 **Code Understanding**

1. **Code Explanation**
    
    Prompt: *"Explain this [language] code: [code example]"*
    
    Example (HTML): "Explain this HTML code: `<nav><ul><li><a href='#'>Home</a></li></ul></nav>`"
    
2. **Question about Code**
    
    Prompt: *"What does this code do: [code example from Stack Overflow]"*
    
    Example (CSS): "What does this CSS code do: `body { font-family: 'Arial', sans-serif; }`?"
    

🕵️‍♂️ **Code Review**

1. **Identify Issues**
    
    Prompt: *"Review this [language] code for potential issues: [code example]"*
    
    Example (Java): "Review this Java code for potential issues: `public static void main(String[] args) { System.out.printn("Hello World!"); }`"
    
2. **Spot Security Flaws**
    
    Prompt: *"Find security risks in this code: [code example]"*
    
    Example (Java): "Find security risks in this Java code: `String password = request.getParameter("password");`"
    

🔧 **Code Refactor**

1. **Enhance Error Handling**
    
    Prompt: *"Improve error handling in this [language] code: [code example]"*
    
    Example (Java): "Improve error handling in this Java code: `int a = 10 / 0;`"
    
2. **Modularity Boost**
    
    Prompt: *"Make this [language] code more modular: [code example]"*
    
    Example (HTML): "Make this HTML code more modular: `<div class='header'><div class='logo'></div><div class='nav'></div></div>`"
    
3. **Performance**
    
    Prompt: *"Optimize this [language] code for better performance: [code example]"*
    
    Example (CSS): "Optimize this CSS code for better performance: `.nav * { margin: 0; padding: 0; }`"
    
4. **Responsiveness**
    
    Prompt: *"Adapt this component for mobile, tablet, and desktop: [code example]"*
    
    Example (CSS): "Adapt this CSS for mobile, tablet, and desktop: `.sidebar { width: 400px; }`"
    
5. **Naming Convention**
    
    Prompt: *"Suggest better names for elements in this code: [code example]"*
    
    Example (Java): "Suggest better names for elements in this Java code: `int a = 5; int b = 10; int c = a + b;`"
    
6. **Simplifying Conditionals**
    
    Prompt: *"Simplify these conditions in the code: [code example]"*
    
    Example (Java): "Simplify these conditions in the Java code: `if(x > 10 && x < 20 && y > 5)`"
    

🐞 **Bug Detection and Fix**

1. **Bug Spotting**
    
    Prompt: *"Locate bugs in this code: [code example]"*
    
    Example (HTML): "Locate bugs in this HTML code: `<a href="www.example.com">Link</a>`"
    
2. **Error Fixing**
    
    Prompt: *"I see [error] in this code: [code example]. How do I solve it?"*
    
    Example (Java): "I see 'NullPointerException' in this Java code: `String name = null; System.out.println(name.length());`. How do I solve it?"