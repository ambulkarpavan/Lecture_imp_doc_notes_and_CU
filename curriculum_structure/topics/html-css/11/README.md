# More meta tags (Advanced) (5-10mins)

Meta tags are vital components within the `<head>` section of an HTML document. They provide metadata about the document's content or give instructions to browsers on how to display it. While not directly visible on the page, meta tags can influence how web pages are described and displayed in search results.

Here are some of the most common meta tags and their purposes:

1. Charset (`<meta charset="UTF-8">`):
    - **Description:** Specifies the character encoding for the HTML document.
    - **Importance:** It ensures characters in the document are rendered correctly, especially for languages with special characters.
    - Ascii: [https://www.w3schools.com/charsets/ref_html_ascii.asp](https://www.w3schools.com/charsets/ref_html_ascii.asp)
    - Emojis: [https://www.w3schools.com/html/html_emojis.asp](https://www.w3schools.com/html/html_emojis.asp)
    
2. Viewport (`<meta name="viewport" content="width=device-width, initial-scale=1">`):
    - **Description:** Defines how a page should appear on mobile devices and is crucial for responsive design.
    - **Importance:** It ensures the website scales and sizes properly on all devices, especially mobile ones.
    
3. Description (`<meta name="description" content="A brief summary of the webpage's content">`):
    - **Description:** Provides a short and concise summary of the webpage's content.
    - **Importance:** Search engines often display this description in search results. A good description can entice users to click on your link.
    
4. Keywords (`<meta name="keywords" content="keyword1, keyword2, ...">`):
    - **Description:** Originally used to tell search engines what keywords the page should rank for.
    - **Importance:** Today, this tag holds less weight in search engine ranking algorithms due to over-optimization and keyword stuffing in the past. Some argue its relevance is minimal now.
5. Author (`<meta name="author" content="Name of the author">`):
    - **Description:** Specifies the author of the webpage.
    - **Importance:** Lets readers know who created the content, though it's not widely used for SEO purposes.
6. Refresh (`<meta http-equiv="refresh" content="5;url=https://example.com/">`):
    - **Description:** Automatically refreshes the page or redirects to another after a specified number of seconds.
    - **Importance:** Can be useful in certain situations like after a form submission or for timed redirects, but overuse can degrade user experience.
7. Social Media Tags (Open Graph, Twitter Cards, etc.):
    - **Description:** These are specific meta tags used to define how content appears when shared on social platforms like Facebook or Twitter. They might define a preview image, title, or description.
    - **Importance:** Ensures that when users share your content on social media, it's presented in an attractive and consistent manner.
    - *This engineers should explore on their own*
    - *Just [google](https://www.google.com/search?q=social+media+meta+tags&sca_esv=570874343&rlz=1C5CHFA_enIN1028IN1028&ei=dEceZcDsEbiei-gPzP6dwAw&ved=0ahUKEwjA9riulN6BAxU4zwIHHUx_B8gQ4dUDCBE&uact=5&oq=social+media+meta+tags&gs_lp=Egxnd3Mtd2l6LXNlcnAiFnNvY2lhbCBtZWRpYSBtZXRhIHRhZ3MyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsANI9wdQ1gVY1gVwAngBkAEAmAEAoAEAqgEAuAEDyAEA-AEB4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp) it*

These are just some of the meta tags available. Depending on your website's needs, you might use additional meta tags or skip some of the ones mentioned above. However, meta tags as a whole play a crucial role in influencing how a website interacts with browsers, search engines, and users.