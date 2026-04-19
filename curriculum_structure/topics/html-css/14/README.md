# Forms (Basic) (15mins)

## Forms

Forms are a fundamental aspect of web development and are used to gather information from users. An HTML form is defined using the `<form>` element. Inside the form, you can have various types of input elements to collect different kinds of data.

Here are some commonly used form elements:

### 1. `<input>`

The `<input>` element is the most versatile form control. It can be configured in various ways depending on its `type` attribute. Some popular input types include:

- `text`: For single-line text input.
- `password`: Similar to `text` but hides the characters as they're typed.
- `radio`: Lets users select one option among a set.
- `checkbox`: Lets users select zero or more options of a limited number of choices.
- `submit`: A button to submit the form.
- `reset`: A button to reset the form to its initial state.
- `file`: For file uploads.
- `hidden`: A hidden data field, which doesn't show to the user but can store data to be sent with the form.
- `date`, `time`, `datetime-local`: For date and time input.
- `email`: For email input. It can validate if the inputted text is in the format of an email address.
- `url`: For URL input. Validates the input format as a URL.
- `number`: Input for numbers. You can set minimum, maximum, and step values.

### 2. `<textarea>`

Allows multi-line text input.

### 3. `<select>`

Used to create a drop-down list. The options within the list are defined using `<option>` elements.

### 4. `<button>`

A clickable button.

### 5. `<label>`

Provides a textual description for a form control. It helps in improving accessibility. When a user clicks on a label, it gives focus to the form element it is associated with.

---

Now, let's create a simple registration form using these elements:

### Example Code

![Untitled](Forms%20(Basic)%20(15mins)%2047d8d78e7a4f4cb09b700f184675465e/Untitled.png)

```html
<form>
    <!-- Name field -->
    <label for="fullname">Full Name:</label>
    <input type="text" id="fullname" name="fullname" required>

    <!-- Email field -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <!-- Password field -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>

    <!-- Gender selection using radio buttons -->
    <label>Gender:</label>
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>

    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>

    <!-- Dropdown for choosing a department -->
    <label for="department">Department:</label>
    <select id="department" name="department">
        <option value="hr">Human Resources</option>
        <option value="it">Information Technology</option>
        <option value="finance">Finance</option>
    </select>

    <!-- Textarea for additional comments -->
    <label for="comments">Comments:</label>
    <textarea id="comments" name="comments" rows="4" cols="50"></textarea>

    <!-- Checkbox to agree to terms -->
    <input type="checkbox" id="terms" name="terms" value="agree" required>
    <label for="terms">I agree to the terms and conditions</label>

    <!-- Submit button -->
    <input type="submit" value="Register">
</form>

```

## 🔑 Student activities

- Its very important that students learn to read mdn documentation
- They should read and implement some of the elements
- They should read and implement different validations in a `number` input
- [https://codepen.io/drupalastic/pen/LYMgaLv?editors=1000](https://codepen.io/drupalastic/pen/LYMgaLv?editors=1000)
- solution