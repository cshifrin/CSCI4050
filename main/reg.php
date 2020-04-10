<?php 
    $email = $_POST['inputEmail'];
    $error = "";

    //checking to see if the email info is valid
    if (isset($_POST['submit'])) { //if the submit button is clicked
        if ($email == "user@email.com" || $email == "admin@email.com") { //CHECK DATABASE FOR EXISTING ACCOUNT WITH EMAIL HERE
            $error = "Oops! That email is already linked to an existing account!";
        }
        else {
            
            //UPDATE DATABASE WITH NEW USER INFO HERE
            //UPDATE USER TO "INACTIVE"
            //SEND CONFIRMATION EMAIL TO USER WITH CONFIRMATION NUMBER

            header("Location: regcon.php"); //redirects to registration confirmation page
        }
    }
?>

<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Registration</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<body>
    <div class="main-content">
        <h1>Registration</h1>
        <p class="error"><?php echo $error; ?></p>
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
                    <label for="inputEmail">Email (required)</label>
                    <input type="email" class="form-control" name="inputEmail" id="inputEmail" placeholder="example@email.com" required>
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
                    <input type="text" class="form-control" id="inputZip" name="inputZip" placeholder="12345">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputCardName">Name on Card</label>
                    <input type="text" class="form-control" id="inputCardName" name="inputCardName" placeholder="Example Card Name">
                </div>
                <div class="form-group col-md-4">
                    <label for="inputCardNo">Card Number</label>
                    <input type="text" class="form-control" id="inputCardNo" name="inputCardNo" placeholder="1234123412341234">
                </div>
                <div class="form-group col-md-2">
                    <label for="inputCardDate">Exp.</label>
                    <input type="text" class="form-control" id="inputCardDate" name="inputCardDate" placeholder="12/1234">
                </div>
            </div>
            <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>

            <button name="submit" type="submit" class="btn btn-outline-dark">Register</button>
        </form>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>