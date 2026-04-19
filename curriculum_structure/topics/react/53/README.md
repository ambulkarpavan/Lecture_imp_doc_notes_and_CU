# How does page loads in SPA

Serial: 48
Made for: Intermediate
Requirement: Good to Have
Time in minutes: 15
Learning Objectives: Routing Advance

# Introduction to Single Page Applications (SPAs) with React

In the dynamic world of web development, Single Page Applications (SPAs) have transformed the way users interact with web platforms. SPA, especially when powered by libraries like React, offer seamless and interactive user experiences by reducing the load on the server and eliminating the need for full-page refreshes. Let's delve deeper into how SPAs function, particularly when built using React.

---

# Detailed Explanation of SPA Page Loads

### Traditional Non-React Websites:

- When you navigate to `xyzabc.com`, the browser sends an initial request to the server.
- The server responds with a full HTML page, such as `index.html`, which is rendered in the browser.
- If you click a link like `/contact`, the server sends back `contact.html`, triggering a full page reload.

### React SPAs:

- The initial request to the server still retrieves an `index.html` file.
- Alongside, the server sends a JavaScript bundle.
- React then initializes and takes over the application on the client side.
- The `index.html` is initially almost empty and is dynamically populated by React components.

---

# Use-case & Benefits of SPAs

SPAs enhance user experience by:

- **Speed**: Reducing the time taken to load and navigate between pages.
- **Bandwidth**: Minimizing data exchange between the client and server.
- **User Experience**: Providing smooth transitions without page refreshes.

---

# Real World Examples of SPAs

Popular platforms like Google Maps, Facebook, and GitHub have embraced SPA architecture to provide fluid and app-like experiences on the web.

---

### Usage of SPAs in Web Development

When a user clicks on links within an SPA, such as `/contact` or `/about`:

- React intercepts the browser's default behavior of sending a new request to the server.
- It then dynamically injects the necessary components into the existing page.
- As a result, `ContactPage`, `AboutPage`, or similar components are rendered without a full page reload.

---

# Instructor Activity

As an instructor, I would walk through the images provided to showcase the difference in the request-response cycle between non-React websites and React-powered SPAs.

---

# Learners Activity

As learners, you would:

- Create a simple non-React website to understand the traditional request-response cycle.
- Build a basic React SPA to observe how React takes control and changes the content dynamically.

---

# Conclusion

The shift to SPAs, particularly with React, represents a significant leap in web application performance and user experience. By understanding the underlying mechanisms of SPAs, developers can create more efficient and responsive web applications.

- Initial request in a non-React website.

![Screenshot 2024-01-10 at 4.06.47 PM.png](How%20does%20page%20loads%20in%20SPA%2088eed3b3b4bd43ecbb8f13913d2123ae/Screenshot_2024-01-10_at_4.06.47_PM.png)

- The server responds with `index.html` in a non-React website

![Screenshot 2024-01-10 at 4.08.05 PM.png](How%20does%20page%20loads%20in%20SPA%2088eed3b3b4bd43ecbb8f13913d2123ae/Screenshot_2024-01-10_at_4.08.05_PM.png)

- Initial request in a React SPA.

![Screenshot 2024-01-10 at 5.13.10 PM.png](How%20does%20page%20loads%20in%20SPA%2088eed3b3b4bd43ecbb8f13913d2123ae/Screenshot_2024-01-10_at_5.13.10_PM.png)

- The server responds with `index.html` and a JavaScript bundle in a React SPA

![Screenshot 2024-01-10 at 5.17.47 PM.png](How%20does%20page%20loads%20in%20SPA%2088eed3b3b4bd43ecbb8f13913d2123ae/Screenshot_2024-01-10_at_5.17.47_PM.png)

- React takes over and dynamically injects components as the user navigates

![Screenshot 2024-01-10 at 5.25.16 PM.png](How%20does%20page%20loads%20in%20SPA%2088eed3b3b4bd43ecbb8f13913d2123ae/Screenshot_2024-01-10_at_5.25.16_PM.png)