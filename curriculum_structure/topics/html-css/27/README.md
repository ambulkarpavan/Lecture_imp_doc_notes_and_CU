# Pixel Perfect Designing with Figma (Basic) (25-30mins)

Before directly going into what Figma is, let us understand the process that happens or the steps involved in creating a website. What are the different stages involved.

Firstly, why any product or website is developed?

To solve a problem or to serve for some purpose, right?

For example, if we consider the Masai School website itself, what is the purpose of the website here? It can be used as a platform to know about Masai courses are, when the next courses will start, who the instructors are, the whole MASAI Team, alumni, people who are ready to be hired, the investors and so on, right.

So, we are giving all this information through the Masai Website.

Similarly, any application will solve a problem or serve a purpose.

So, the first step is to discover ⇒ what the purpose of the website/application is.

Then we have to define what we want to show in the website.

Let’s say, we have decided that we want to show all the information related to Masai in the website. We have to clearly define what the pages should be, how the total has to be segregated and so on. This is what we mean by define. 

Then comes the design. Design will be done by UI/UX designer who will give work on how the elements have to look wrt user interface and user experience. 

Once the design is completed, the developer will develop the website as per the design.

Finally, once the website is developed, the website is delivered/deployed and that is when public will have access to it.

> From all the steps that we have discussed in order to bring a website to life, Figma is a tool which is used to connect some of the steps involved in this process.
> 

## What is Figma?

Figma is a tool that connects design, product and development. 

Now that we have seen the definition of Figma, let’s see how this helps us, Developers

Till now, how did you develop any layouts. We have given you images and you had to guess or develop the layouts by some trial and error method and build something close to the given picture, right.

With Figma, Developers will have better access to the designs and have the ability to extract information about the layouts/components such as the colors used, the font size, padding, margin, typography and much more.

This is how a Figma file will look.

Let us start with some website that we already know. Masai School website.

If you observe the Masai School Website - the figma file is this: Lets see the investors layout we have built first to understand how easily we can build if we have a Figma file.

Just by looking at the investor box, can we know how much border radius is for each investor? We have done it by trial and error, something we have achieved close to this, right?

Using Figma, from the design, you will be able to see all the CSS properties used as well in the inspect section.

This will be helpful in building pixel perfect layouts, i.e, you should not be able to see the difference between design in Figma and the app you have built. 

So, let’s build a simple component from Figma design.

[https://www.figma.com/file/wGsXaEmYHgo2RPjtJsXUrb/LOGIFY---WEB-LOGIN-UI-KIT-(Community)?node-id=858%3A412&t=Vf17iHPhHG5mIiok-0](https://www.figma.com/file/wGsXaEmYHgo2RPjtJsXUrb/LOGIFY---WEB-LOGIN-UI-KIT-(Community)?node-id=858%3A412&t=Vf17iHPhHG5mIiok-0)

We will build this component from Figma file.

Firstly , let’s create the HTML file.

```jsx
<html>

	<head>
		<title>Figma - Design to Development
		<link rel="stylesheet" href="figma.css" />
	</head>
	<body>
		<div id="container">
			<div id="left-div"></div>
			<div id="right-div"></div>
		</div>
	</body>
</html>
```

vh means ⇒ viewport that means 

CSS File

```jsx
body {
	margin:0;
	padding:0
}

#container {
	width:100%;
	height:100vh;
	display:flex;
}

#container > div {
	width:50%;
}

#left-div {
	background-color:#ecbc76;
	display:flex;
	justify-items:center;
	align-items:center;
}
```

Firstly, till now how did we display images? We copied the image address or from the data we get from backend, we display the image addresses, right. Now we will see how we can display the images present in the local system. 

Firstly, we have to download the image. Let’s see the image that is present in Figma, we can download it by clicking on export, and then we have a lot of formats in which we can download the image. We have already displayed the png/jpeg format of images. So, I will download svg format of image. I will extract this image and copy paste it in the same folder as that of our assignment.

Now for img tag in src, you can mention the address like so.

```jsx
<img src="left.svg" />
```

How to get image to center of the div?

We saw how we can center align wrt both horizontal and vertical axes, right? justify-center, align-center.

Now, let’s do the right side div.

It’s a simple sign up form.

Let’s first see what elements are present in the signup form. It consists of some tags, button, box shadow and so on right. Now if you observe for the button there is some background color, previously I told you that for getting the background color, we used some extension. But were we able to get all the remaining details related to the button. Like the border radius, the font size of text inside the button and so on. Now, are we getting this information?

Now let’s see the box shadow for the whole sign up form. There are some details there, right?

From these details, we should not take everything. We already know that we should not fix the height of any div, right? It has to take the height of the content. But here, you can see the width and the height. So, these are for the screen size of the UI only. We should never create any design for one screen size. So, we will not consider those properties here. We will take only background, box shadow and border radius out of these properties

```jsx
#right-div {
	background:#FFFFFF;
	box-shadow: 0px 4px 35px rgba(0,0,...);
	border-radius:40px;
	margin:70px;
}
```

Now, let’s write the content inside the box.

```jsx
Inside right div

<div id="right-div">
	<p>Welcome to Masai</p>
	<p>Sign Up</p>
	<p class="label">Enter your username or email address</p>
	<input placeholder="Username or email address" />
	<p class="label">Enter your Password</p>
	<input placeholder="Password" />
	<p id="pass">Forgot Password</p>
	<button>Sign In</button>
	<p>No Account ? <span>Sign up</span> </p>
	<p>pr continue with</p>
	<div id="social">
		 <img /> *3 => download and keep them
	</div>
	
</div>

```

For these, now we will add the CSS using combinators

For font family, you have to go to google fonts and copy a few link tags .

If its a normal font style, you don’t have to mention it.

## Example:

## **Pixel Perfect Designing with Figma for HTML & CSS Development**

[https://www.figma.com/file/P728ZEPqIwLTH6OTsqcJcD/Responsive_Template?node-id=0%3A1&t=6TSZQq94XzOnD0i5-0](https://www.figma.com/file/P728ZEPqIwLTH6OTsqcJcD/Responsive_Template?node-id=0%3A1&t=6TSZQq94XzOnD0i5-0)

![Untitled.png](Pixel%20Perfect%20Designing%20with%20Figma%20(Basic)%20(25-30m%20370236371e364c278786c8cc25cf263c/Untitled.png)