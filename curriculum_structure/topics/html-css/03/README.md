# Installation(VS code)(Basic) (5-10mins)

How to Install Visual Studio Code and Google Chrome on Windows, Linux, and Mac

Installing software across different operating systems involves a variety of steps and methods. For developers or users who work with different operating systems, knowing how to set up essential software like Visual Studio Code (VS Code) and Google Chrome can be invaluable. In this article, we will explore the steps needed to install VS Code and Google Chrome on Windows, Linux, and macOS.

## Installing on Windows

### Visual Studio Code

1. **Download Installer**: Visit the [VS Code website](https://code.visualstudio.com/) and download the Windows installer.
2. **Run Installer**: Double-click on the installer and follow the on-screen instructions. You can accept the default settings for most installations.
3. **Launch**: After the installation is complete, launch VS Code from the Start menu or desktop shortcut.

### Google Chrome

1. **Download Installer**: Visit the [Google Chrome website](https://www.google.com/chrome/) and download the installer.
2. **Run Installer**: Double-click the downloaded file and allow it to run. Follow on-screen instructions.
3. **Launch**: Once the installation is complete, Chrome will launch automatically.

## Installing on Linux (Ubuntu)

### Visual Studio Code

1. **Update Package List**: Open a terminal and run `sudo apt update`.
2. **Install Dependencies**: Run `sudo apt install software-properties-common apt-transport-https`.
3. **Import Microsoft GPG Key**: Run `wget -q <https://packages.microsoft.com/keys/microsoft.asc> -O- | sudo apt-key add -`.
4. **Add Repository**: Run `sudo add-apt-repository "deb [arch=amd64] <https://packages.microsoft.com/repos/vscode> stable main"`.
5. **Install VS Code**: Run `sudo apt update` followed by `sudo apt install code`.

### Google Chrome

1. **Download DEB file**: Visit the [Google Chrome website](https://www.google.com/chrome/) and download the `.deb` installer.
2. **Install DEB**: Run `sudo dpkg -i google-chrome-stable_current_amd64.deb`.
3. **Launch**: Run `google-chrome` from the terminal or find it in your application menu.

## Installing on macOS

### Visual Studio Code

1. **Download Installer**: Visit the [VS Code website](https://code.visualstudio.com/) and download the macOS installer.
2. **Run Installer**: Double-click the downloaded `.zip` file to expand it. Drag and drop the VS Code app into the Applications folder.
3. **Launch**: Open it from the Applications folder or Spotlight.

### Google Chrome

1. **Download Installer**: Visit the [Google Chrome website](https://www.google.com/chrome/).
2. **Run Installer**: Double-click the downloaded `.dmg` file. Drag and drop Chrome into the Applications folder.
3. **Launch**: Open it from the Applications folder or via Spotlight.

And there you have it, you've installed Visual Studio Code and Google Chrome on Windows, Linux, and macOS. With these tools installed, you're well on your way to a streamlined and productive computing experience.

## IDE vs Text Editor: Why Web Developers Should Choose VS Code Over Notepad

When you're just starting your journey in web development, one of the first things you'll need to do is choose an appropriate tool for writing your code. While you can technically write code in any text-editing tool, such as Notepad or TextEdit, there are compelling reasons to opt for an Integrated Development Environment (IDE) like Visual Studio Code (VS Code).

### What is an IDE?

An IDE is an all-in-one development tool that provides multiple utilities for software development. In the case of VS Code, it includes features such as:

1. **Syntax Highlighting**: Colors your code according to the language's syntax, making it easier to read and debug.
2. **Auto-Completion**: Suggests code as you type, making it quicker to write.
3. **Built-in Terminal**: Allows you to run your code within the same window you're writing it.
4. **Extensions**: You can add various plugins that help with debugging, version control, and even language support.
5. **Code Suggestions and Linting**: Helps you write clean, optimized code by providing suggestions and flagging errors.
6. **File and Project Navigation**: Easily jump between files and view the structure of your project.

### What is a Text Editor?

A text editor like Notepad or TextEdit is a simple application that lets you read and write plain text files. While they are lightweight and quick to open, they lack the features needed to write code efficiently, such as syntax highlighting and error detection.

### The Importance of Using an IDE for Web Development

When you're working on web development projects, an IDE can help you write better code more quickly and avoid common mistakes:

1. **Speed**: Auto-completion and code suggestions speed up the development process.
2. **Debugging**: Built-in debuggers help you locate errors in your code faster.
3. **Collaboration**: Features like integrated Git support make it easier to collaborate with other developers.
4. **Learning**: For beginners, the guidance provided by an IDE's linting and error messages can be educational.
5. **Multi-language Support**: If your project includes different languages (HTML, CSS, JavaScript, etc.), an IDE can handle them all seamlessly.

### Warning: Don't Use Word Processors

Some newcomers might think using a word processor like Microsoft Word (or Apple Text Edit in rich text mode) is acceptable for coding. This is a significant mistake for a couple of reasons:

1. **Formatting Issues**: Word processors add extra formatting to the text, which can result in errors when your code runs.
2. **Non-ASCII Characters**: Word processors may insert non-ASCII characters, such as curly quotes, which can break your code.
3. **File Types**: Word processors save files in formats that are not compatible with web development.

In conclusion, while you can technically use a simple text editor for web development, you'll be doing yourself a disservice by not taking advantage of the powerful tools that an IDE like VS Code offers. And always remember, steer clear of using word processors like MS Word for coding. Choose the right tool for the job, and you'll find that the task becomes easier, more efficient, and more enjoyable.

##