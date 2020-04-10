<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Return Book</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<nav class="navbar navbar-expand-sm navbar-light">
    <a class="navbar-brand" href="#">Our Bookstore</a>
    <ul class="navbar-nav">
        <li class="nav-item"> <a class="nav-link" href="userprofile.php">Profile</a> </li>
        <li class="nav-item"> <a class="nav-link" href="search.php">Search Books</a> </li>
        <li class="nav-item"> <a class="nav-link" href="cart.php">Shopping Cart</a> </li>
    </ul>
</nav>

<body>
    <div class="main-content">
        <h1>Title</h1>
        <h2>Author</h2>
        <p>Description of the book</p>
        <p>$price</p>
        <p>Order Number: 123456789</p>
        <p>Note: When we receive the book, you will be given a refund and you will no longer see the selected book in
            your order history. Mail your book back to the following address:</p>
        <p>Boyd Graduate Studies Research Center, D.W. Brooks Drive, Athens, Georgia 30602-7415</p>
        <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>
    </div>
</body>

</html>