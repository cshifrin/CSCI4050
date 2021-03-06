<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Checkout</title>
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
        <h1>Checkout</h1>
        <div class="book-list">
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <button type="button" class="btn btn-sm btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
            </div>
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <button type="button" class="btn btn-sm btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
            </div>
            <div class="book">
                <h3>Title</h3>
                <h4>Author</h4>
                <p>$price</p>
                <button type="button" class="btn btn-sm btn-outline-dark" onclick="window.location.href = 'bookdetails.php';">View
                    Book</button>
            </div>
        </div>
        <br><h2>Total: $price</h2><br>
        <form action="checkoutcon.php">
            <p>All fields are required!</p>
            <div class="form-group">
                <label for="inputAddress">Shipping Address</label>
                <input type="text" class="form-control" id="inputAddress" placeholder="1234 Example Street">
            </div>
            <div class="form-group">
                <label for="inputAddress2">Address 2</label>
                <input type="text" class="form-control" id="inputAddress2" placeholder="Apartment, studio, or floor (if any)">
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCity">City</label>
                    <input type="text" class="form-control" id="inputCity" placeholder="Example">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputState">State</label>
                    <input type="text" class="form-control" id="inputState" placeholder="EX">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputZip">Zip Code</label>
                    <input type="text" class="form-control" id="inputZip" placeholder="12345">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCardName">Name on Card</label>
                    <input type="text" class="form-control" id="inputCardName" placeholder="Example Card Name">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputCardNo">Card Number</label>
                    <input type="text" class="form-control" id="inputCardNo" placeholder="1234123412341234">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputCardDate">Exp.</label>
                    <input type="text" class="form-control" id="inputCardDate" placeholder="12/1234">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputPromotion">Promotion Code (if any)</label>
                    <input type="text" class="form-control" id="inputPromotion" placeholder="PromotionCode">
                </div>
            </div>
            <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>
            <button type="submit" class="btn btn-outline-dark">Checkout</button>
        </form>
    </div>
</body>

<footer>
        <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
    </footer>
    
</html>