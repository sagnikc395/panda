## Building a SSG:

Static sites are very popular in the real world for blogs and other content-heavy websites because they're lightning-fast, secure, and easy to host. For example, the Boot.dev Blog is a production-level static site generated with Hugo.

### Static vs. Dynamic Sites

- A static site is what it sounds like... static. The content is always the same. Users can not:
  - Upload files
  - Log in
  - Leave comments
  - Save preferences

### HTML

- The primary output of a static site generator is HTML (HyperText Markup Language), because HTML contains all the content of a web page.

- HTML is a simple language for structuring content. It's not a "programming" language in the sense that it doesn't have variables, loops, or conditionals.

- HTML is a tree-like structure where each "tag" (e.g. <p>, the bits enclosed in angle brackets) can contain other tags, and the whole thing is enclosed in an outermost <html> tag. Let's break down the structure of this HTML file:

<html> is the root element of the document.
<head> contains metadata about the document. Anything in the <head> is not rendered visibly in the browser window.
<title> is the title of the document, which is displayed in the browser tab.
<body> contains the content of the document, which is what is rendered in the browser window.
<h1> is a top-level heading.
<p> is a paragraph of text.
<a> is a hyperlink. The href attribute is the URL the link points to. Attributes are key-value pairs that provide additional information about an element, like href="https://www.boot.dev".

### CSS

- CSS (Cascading Style Sheets) is another "not-really-a-programming-language" that styles HTML elements. It's a way to dress up your HTML with colors, fonts, responsive layouts, animations, etc.

```css
/_ Make all <h1 > HTML elements red _/ h1 {
  color: red;
}
```

- Or maybe we want the max-width of our paragraphs to be 50% of the screen width:

```css
/_ Make all <p > HTML elements 50% of the screen width _/ p {
  max-width: 50%;
}
```

## html kinda sucks -> enter markdown

- writing markdown is pure bliss, less-verbose markup language designed for the ease of writing.
- trouble is web browsers dont understand markdown.
- only understands html and css.
- our ssg will take a directory of markdown files and build a directory of HTML files.

## Architecture:

The flow of data through the full system is:

- Markdown files are in the /content directory. A template.html file is in the root of the project.
- The static site generator (the Python code in src/) reads the Markdown files and the template file.
- The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
- We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our local machine).
- We open a browser and navigate to http://localhost:8888 to view the rendered site.

## how does SSG works:

The vast majority of our coding will happen in the src/ directory because almost all of the work is done in steps 2 and 3 above. Here's a rough outline of what the final program will do when it runs:

- Delete everything in the /public directory.
- Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
- Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
- Open the file and read its contents.
- Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
- Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
- Raw markdown -> TextNode -> HTMLNode
- Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
- Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
- Write the full HTML string to a file for that page in the /public directory.
