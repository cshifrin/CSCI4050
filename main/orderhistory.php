<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Order History</title>
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
        <h1><img height="40px" src="css/voh.png"> Order History</h1>
        <div class="book-list">
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <p>Order Number: 123456789</p>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
                    <button type="button" class="btn btn-outline-dark" onclick="">Reorder (Add to Shopping Cart)</button>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookreturn.php';">Return
                    Book</button>
            </div>
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <p>Order Number: 123456789</p>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
                    <button type="button" class="btn btn-outline-dark" onclick="">Reorder (Add to Shopping Cart)</button>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookreturn.php';">Return
                    Book</button>
            </div>
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <p>Order Number: 123456789</p>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
                <button type="button" class="btn btn-outline-dark" onclick="">Reorder (Add to Shopping Cart)</button>
                <button type="button" class="btn btn-outline-dark" onclick="window.location.href = 'bookreturn.php';">Return
                    Book</button>
            </div>
        </div>
        <br>
        <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>
    </div>
</body>

<footer>
        <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
    </footer>
    
</html>