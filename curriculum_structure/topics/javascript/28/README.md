# Hoisting [20 min] (1)

[MDN](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

In the compilation/parsing phase (phase-1), We have all the tokens/identifiers available before the execution phase starts. Of course, the assignment happens in the execution phase, but yes, all the variables are available to us, they exist in the memory,  immediately after the parsing phase (phase-1)

- `let`s and `const`s hoist to a block, whereas `var`s hoist to a function.
- In case of `var`, in the compilation/parsing phase, it is initialized to `undefined`
- In case of `let`, in the compilation/parsing phase, a token is created, but it is not initialized at all (TDZ error - uninitialized)

MDN Definition (best one): JavaScript **Hoisting** refers to the process whereby the interpreter appears to move the *declaration* of functions, variables or classes to the top of their “**scope”**, prior to execution of the code.

This means that no matter where functions and variables are declared, they are moved to the top of their scope regardless of whether their scope is global or local. Of note however, is the fact that the hoisting mechanism only moves the **declaration**. The assignment in case of expressions are left in place.

## var VS let VS const

|  | var | let | const |
| --- | --- | --- | --- |
| Scope | function | block | block |
| re-declaration | allowed ✅ | not-allowed❌ | not-allowed❌ |
| accesibility before declaration | accessible ✅ | not accessible ❌ | not accessible ❌ |

## Temporal Dead Zone:

Unlike `var`,  `let` and `const` are not initialized with undefined while hoisting. That is why let and const are not accessible till the point in the block where it is initialized with some value. the area in the block where let and const are not accessible know as `Temporal Dead Zone`.