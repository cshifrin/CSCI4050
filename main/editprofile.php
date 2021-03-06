<?php 
    if (isset($_POST['submit'])) { //if the submit button is clicked        
        $name = $_POST['name'];

        //UPDATE DATABASE WITH NEW USER INFO HERE

        header("Location: userprofile.php"); //redirects to user profile page
    }
?>

<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Edit Profile</title>
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
        <h1><img height="40px" src="css/ep.png"> Edit Profile</h1>
        <form method="POST">
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputName">Name (required)</label>
                    <input type="text" class="form-control" name="inputName" id="inputName" placeholder="First Last" required>
                </div>
                <div class="form-group col-md-6">
                    <label for="inputPhone">Phone (required)</label>
                    <input type="tel" class="form-control" name="inputPhone" id="inputPhone" placeholder="1-(555)-555-5555" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputEmail">Email</label>
                    <input type="email" class="form-control" placeholder="example@email.com" disabled>
                </div>
                <div class="form-group col-md-6">
                    <label for="inputPassword">Password (required)</label>
                    <input type="password" class="form-control" name="inputPassword" id="inputPassword" placeholder="Example1234" required>
                </div>
            </div>
            <div class="form-group">
                <label for="inputAddress">Address</label>
                <input type="text" class="form-control" name="inputAddress" id="inputAddress" placeholder="1234 Example Street">
            </div>
            <div class="form-group">
                <label for="inputAddress2">Address 2</label>
                <input type="text" class="form-control" name="inputAddress2" id="inputAddress2" placeholder="Apartment, studio, or floor (if any)">
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCity">City</label>
                    <input type="text" class="form-control" name="inputCity" id="inputCity" placeholder="Example">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputState">State</label>
                    <input type="text" class="form-control" name="inputState" id="inputState" placeholder="EX">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputZip">Zip Code</label>
                    <input type="text" class="form-control" name="inputZip" id="inputZip" placeholder="12345">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCardName">Name on Card</label>
                    <input type="text" class="form-control" name="inputCardName" id="inputCardName" placeholder="Example Card Name">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputCardNo">Card Number</label>
                    <input type="text" class="form-control" name="inputCardNo" id="inputCardNo" placeholder="1234123412341234">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputCardDate">Exp.</label>
                    <input type="text" class="form-control" name="inputCardDate" id="inputCardDate" placeholder="12/1234">
                </div>
            </div>
            <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>

            <button name="submit" type="submit" class="btn btn-outline-dark">Save</button>
        </form>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>