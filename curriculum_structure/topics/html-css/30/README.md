# Tailwind (Advanced) (40mins)

### What is Tailwind CSS?

Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to build designs directly in your markup. It's highly customizable, responsive, and aims to make styling websites more efficient.

### Why Tailwind?

Productivity: Write less code and focus on the design.
Consistency: Easily maintain a consistent design across your project.
Flexibility: Customize styles without leaving your HTML.

### Getting started

npm install -D tailwindcss
npx tailwindcss init

Creates tailwind.config.js for customization.

Create a src folder and inside an index.html, index.css

Inside  **`tailwind.config.js`** file

```jsx
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Inside index.css

```jsx
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### **Start the Tailwind CLI build process**

Run the CLI tool to scan your template files for classes and build your CSS.

```jsx
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```

Inside index.html

```jsx
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/dist/output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

Final folder structure

A utility class is a CSS class that provides a specific and single-purpose styling to an HTML element. Utility-first CSS frameworks, like Tailwind CSS, popularized the concept of utility classes. Instead of creating custom styles in a separate stylesheet, utility classes are directly applied to HTML elements to achieve specific styling.

Examples

```html

<div class="bg-blue-500 text-white p-4">
Hello, Tailwind!
</div>
<div
      class="w-200 h-200 bg-blue-500 sm:bg-green-500 md:bg-red-500 lg:bg-yellow-500"
    >
      Responsive Background
    </div>
    <!-- Width and Height -->
    <div class="w-64 h-32 bg-blue-500 text-white p-4">
      Width: 64, Height: 32
    </div>
    <!-- Margin and Padding -->
    <div class="m-4 p-8 bg-green-500 text-white">Margin: 4, Padding: 8</div>
    <!-- Flexbox -->
    <div class="flex justify-center items-center bg-red-500 text-white p-4">
      Centered Flex Container
    </div>
    <!-- Grid -->
    <div class="grid grid-cols-2 grid-rows-2 bg-yellow-500 text-white">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    <!-- Text Color -->
    <p class="text-blue-500">Blue Text</p>
    <!-- Font Size -->
    <p class="text-lg">Large Text</p>
    <!-- Font Weight -->
    <p class="font-bold">Bold Text</p>
    <!-- Text Alignment -->
    <p class="text-center">Centered Text</p>
    <!-- Background Color -->
    <div class="bg-purple-500 text-white p-4">Purple Background</div>
    <!-- Background Opacity -->
    <div class="bg-gray-700 bg-opacity-75 text-white p-4">
      Semi-transparent Background
    </div>
    <!-- Border Color -->
    <div class="border-2 border-blue-500 p-4">Blue Border</div>
    <!-- Border Width -->
    <div class="border-4 border-red-500 p-4">Thick Red Border</div>
    <!-- Border Radius -->
    <div class="rounded bg-orange-500 text-white p-4">Rounded Corners</div>
    <!-- Box Shadow -->
    <div class="shadow-md p-4">Box with Medium Shadow</div>
    <!-- Positioning -->
    <div class="relative w-64 h-64">
      <div class="absolute top-10 left-10 bg-indigo-500 text-white p-4">
        Absolute Positioned
      </div>
    </div>
    <!-- Visibility -->
    <div class="visible bg-green-500 text-white p-4">Visible</div>

    <div class="invisible bg-red-500 text-white p-4">Invisible</div>
    <!-- Interactivity -->
    <div class="cursor-pointer hover:bg-blue-500 text-white p-4">
      Hover Effect
    </div>
    <!-- Responsiveness -->
    <!-- <div class="w-64 h-64 border-2 sm:w-1/2 md:hidden lg:bg-purple-500 text-white p-4">
  Responsive Design
</div> -->
    <!-- Flexbox Alignment -->
    <div class="flex justify-between items-center bg-teal-500 text-white p-4">
      <div>Left</div>
      <div>Right</div>
    </div>
    <!-- Text Decoration -->
    <p class="underline">Underlined Text</p>
    <!-- Background Gradient -->
    <div class="bg-gradient-to-r from-yellow-500 to-red-500 text-white p-4">
      Gradient Background
    </div>
    <!-- Hover Effects -->
    <div
      class="transition-transform transform hover:scale-110 bg-indigo-500 text-white p-4"
    >
      Hover to Scale Up
    </div>
    <!-- Overflow -->
    <div class="overflow-hidden bg-purple-500 text-white p-4">
      Overflow HiddenOverflow Hidden Overflow Hidden
    </div>
    <div class="overflow-hidden">
      <!-- Content that might overflow -->
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
    </div>

    <!-- Transition and Animation -->
    <div
      class="transition-colors duration-500 ease-in-out hover:bg-yellow-500 text-white p-4"
    >
      Color Transition on Hover
    </div>

    <div class="animate-spin bg-blue-500 text-white p-4">
      Spinning Animation
    </div>
    <!-- Placeholder Color -->
    <input
      type="text"
      placeholder="Enter text"
      class="placeholder-blue-500 p-2 m-2 border-2 border-blue-500"
    />

    <!-- Z-Index -->
    <div class="relative bg-yellow-500 text-white p-4">
      <div class="absolute bg-yellow-100 top-10 left-10 z-10">On Top</div>
      Content
    </div>

    <!-- Line Height read more-->
    <p class="leading-loose">Loose Line Height</p>

    <!-- Grid Template -->
    <!-- Grid Template with Height and Width -->
    <div
      class="grid grid-cols-[auto,1fr,auto] h-700 w-full bg-purple-500 text-white p-4"
    >
      <div>Left</div>
      <div>Main</div>
      <div>Right</div>
    </div>
    <!-- Flex Wrap -->
    <div class="flex flex-wrap gap-4 bg-blue-500 text-white p-4 h-700 w-full">
      <div>Item 1</div>
      <div>Item 2</div>
      <div>Item 3</div>
    </div>

    <!-- Truncate Text -->
    <div class="w-24 truncate bg-red-500 text-white p-4">
      This is a long text that will be truncated
    </div>

    <!-- Ring -->
    <button class="ring-2 ring-blue-500 bg-white text-black p-2">
      Click me
    </button>

    <!-- Placeholder Opacity -->
    <input
      type="text"
      placeholder="Enter text"
      class="placeholder-opacity-50 p-2 m-2 border-2 border-blue-500"
    />

    <!-- Skew -->
    <div class="skew-x-6 bg-pink-500 text-white p-4">Skewed Box</div>

    <!-- Object Fit read more-->
    <img
      src="image.jpg"
      class="object-cover h-64 w-full"
      alt="Responsive Image"
    />

    <!-- Divide read more-->
    <div class="divide-x divide-blue-500 p-4">
      <div>Item 1</div>
      <div>Item 2</div>
    </div>

    <!-- Place Content -->
    <div
      class="grid grid-cols-2 grid-rows-2 place-content-center bg-green-500 text-white p-4"
    >
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    <!-- List Style Type -->
    <ul class="list-disc p-4">
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
    <!-- Scroll Snap -->
    <div class="flex overflow-x-auto snap-x snap-mandatory bg-yellow-500 p-4">
      <div class="flex-none w-24 snap-start bg-blue-500 m-2">Item 1</div>
      <div class="flex-none w-24 snap-start bg-red-500 m-2">Item 2</div>
      <div class="flex-none w-24 snap-start bg-green-500 m-2">Item 3</div>
    </div>
    <!-- Scroll Behavior -->
    <div class="overflow-y-auto h-700 scroll-behavior-smooth bg-purple-500 p-4">
      Scroll Smoothly
    </div>
    <!-- Placeholder Size -->
    <input
      type="text"
      placeholder="Enter text"
      class="placeholder-blue-500 placeholder-opacity-75 p-2 m-2 border-2 border-blue-500"
    />
    <!-- Sticky -->
    <div class="sticky top-0 bg-red-500 text-white p-4">Sticky Header</div>
    <div class="p-4">Scroll down to see the effect</div>
    <!-- Word Break -->
    <div class="break-all bg-orange-500 text-white p-4">
      ThisIsAReallyLongWordWithoutSpaces
    </div>
```

### Student task

You are building a basic landing page using Tailwind CSS. The design includes a navigation bar with a logo on the left and navigation links on the right. The logo should have a maximum width of 150 pixels, and the navigation links should be horizontally aligned with some spacing between them.

Your task is to implement the navigation bar using Tailwind CSS classes. Assume that you have an HTML structure like the following:

```jsx
<div class="navbar">
    <div class="logo">Your Logo</div>
    <div class="nav-links">
        <a href="#" class="nav-link">Home</a>
        <a href="#" class="nav-link">About</a>
        <a href="#" class="nav-link">Services</a>
        <a href="#" class="nav-link">Contact</a>
    </div>
</div>
```