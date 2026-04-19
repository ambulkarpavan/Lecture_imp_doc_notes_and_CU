# Using typescript with existing project

Content goes here

If you have an existing React project and want to add TypeScript, you can install it via npm or Yarn:

```bash
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
```

or

```bash
yarn add typescript @types/node @types/react @types/react-dom @types/jest
```

Then, you can start renaming your **`.js`** or **`.jsx`** files to **`.ts`** or **`.tsx`** (for files containing JSX).

After installation, you'll have a **`tsconfig.json`** in your project directory. This file contains the compiler options required for your project, and you can customize it as needed.