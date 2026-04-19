# Deployment ( Frontend )

Serial: 49

# Introduction

Today, we'll delve into the deployment of frontend web applications, a crucial step in making your website accessible to the public via the internet. This process involves uploading your website's files and databases to a server, which then serves the content to users. We'll also explore how to use Netlify and Vercel, two popular cloud services, for deployment.

# Detailed Explanation

### What is Deployment?

Deployment is the process of making your website or web application publicly accessible over the internet. It involves setting up your project on a server that hosts and serves your content. In the past, this required maintaining personal servers, but now cloud services like Netlify and Vercel offer more convenient solutions.

### Why Use Cloud Services?

1. **Infrastructure Management**: Cloud services manage the server infrastructure, reducing the maintenance burden.
2. **Accessibility**: Cloud-based applications can be accessed from anywhere.
3. **Cost-Effective**: Pay for what you use, without the overhead of managing physical servers.

# Use-case & Benefits

Deploying a website using cloud services like Netlify and Vercel offers significant advantages:

- **Ease of Use**: Simple interfaces and integration with development tools.
- **Scalability**: Easily handle varying traffic without manual intervention.
- **Continuous Deployment**: Automatically update your live application with changes from your repository.

# Real World Examples

- **Portfolios**: Freelancers deploying their portfolio sites.
- **Blogs**: Independent writers hosting their blogs.
- **E-commerce**: Small businesses setting up online stores.

# Usage

### Deploying with Netlify

1. **Create an Account**: Sign up on [Netlify](https://www.netlify.com/) using GitHub.
2. **Install Netlify CLI**: Use `npm install netlify-cli -g` for global installation.
3. **Prepare the Build**: Run `npm run build` to create an optimized production build.
4. **Serve Locally**: Install `serve` globally and use `serve -s build` to serve your build folder locally.
5. **Configure `package.json`**: Add `"homepage": "."` to handle relative paths.
6. **Initial Deployment**: Use `netlify deploy` to create a draft site, verify, and then deploy to production with `netlify deploy --prod`.
7. **Handle Redirects**: Add a `_redirects` file in the build folder with `/* /index.html 200`.

### Deploying with Vercel

1. **Install Vercel CLI**: Run `npm i -g vercel`.
2. **Prepare for Deployment**: Navigate to your project's root directory.
3. **Deploy**: Use `vercel` for a draft and `vercel --prod` for production.

# Instructor Activity

1. **Demonstration**: Deploy a simple React application on Netlify and Vercel.
2. **Explain CLI Commands**: Walk through the commands used during the deployment process.
3. **Discuss the Build Process**: Explain how `npm run build` works and its importance.

# Learners Activity

1. **Deployment Practice**: Have learners deploy a basic frontend application to Netlify and Vercel.
2. **Review Deployed Applications**: Share deployed application links for peer review.
3. **Troubleshooting Session**: Discuss any issues encountered during deployment and how to resolve them.

# Conclusion

Deployment is a vital step in web development, making your application accessible to a global audience. Cloud services like Netlify and Vercel simplify this process, allowing developers to focus on building great applications. Remember, deployment is not just about making your site live; it's about maintaining and updating it efficiently.