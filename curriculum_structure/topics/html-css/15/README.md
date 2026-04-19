# Tables (Basic) (20mins)

Before starting with syntax for HTML tables , do explain the need of the table and how tables make things easier by showing on google sheets.

![Screenshot 2023-11-02 160414.png](Tables%20(Basic)%20(20mins)%20605b05986f154abba66979d4002c9494/Screenshot_2023-11-02_160414.png)

## Tables

![Untitled](Tables%20(Basic)%20(20mins)%20605b05986f154abba66979d4002c9494/Untitled.png)

 

An HTML table is used to represent data in a tabular format, i.e., in rows and columns. This structure can be immensely useful for displaying information in a structured manner, like financial statements, calendars, and various kinds of lists.

Here's a basic breakdown of table-related elements:

### 1. `<table>`

This is the root element for a table. All other table elements are nested within it.

### 2. `<thead>`

This element wraps the set of rows that describe the table headers. Although not strictly required, it's useful for differentiating the header row(s) from the body rows.

### 3. `<tbody>`

This element wraps the set of rows that describe the actual data in the table. It is also not strictly required, but it's a good semantic element to differentiate the main content of the table from the headers and footers.

### 4. `<tfoot>`

This element wraps the set of rows that describe the table footers. It can be useful for displaying summaries, totals, or footnotes for the table's data.

### 5. `<tr>`

This element represents a table row. It wraps a set of table cells, which can be either header cells (`<th>`) or standard cells (`<td>`).

### 6. `<th>`

This element represents a header cell. By default, its content is bold and centered.

### 7. `<td>`

This element represents a standard table cell.

### 8. `<colgroup>` and `<col>`

These elements allow you to apply styles to an entire column (or a group of columns) at once.

### Example Code

---

Now, let's create a sample table to represent the sales data of a small company across a few months:

```html
<table border="1">
    <!-- Table Header -->
    <thead>
        <tr>
            <th>Month</th>
            <th>Product A Sales ($)</th>
            <th>Product B Sales ($)</th>
            <th>Total Sales ($)</th>
        </tr>
    </thead>

    <!-- Table Body -->
    <tbody>
        <tr>
            <td>January</td>
            <td>1200</td>
            <td>800</td>
            <td>2000</td>
        </tr>
        <tr>
            <td>February</td>
            <td>1300</td>
            <td>850</td>
            <td>2150</td>
        </tr>
        <tr>
            <td>March</td>
            <td>1250</td>
            <td>900</td>
            <td>2150</td>
        </tr>
    </tbody>

    <!-- Table Footer -->
    <tfoot>
        <tr>
            <td>Total</td>
            <td>3750</td>
            <td>2550</td>
            <td>6300</td>
        </tr>
    </tfoot>
</table>

```

In this table, we have:

- A header (`<thead>`) with titles for each column.
- A body (`<tbody>`) with the sales data for each month.
- A footer (`<tfoot>`) showing the total sales for each product and the grand total across months.

The `border="1"` attribute on the `<table>` tag is a quick way to add borders to the table for better visibility. However, in modern web development, styling is usually handled with CSS rather than inline attributes.

##