<?php 
    $confNum = $_POST['confNum'];
    $error = "";

    //checking to see if the confirmation number is valid
    if (isset($_POST['submit'])) { //if the submit button is clicked
        if ($confNum == "123") { //CHECK FOR VALID CONFIRMATION NUMBER HERE

            //UPDATE USER TO "ACTIVE"

            header("Location: signin.php"); //redirects to sign in page
        }
        else {
            $error = "Oops! That's an invalid confirmation number!";
        }
    }
?>

<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Registration Confirmation</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<body>
    <div class="main-content" style="margin: 15%;">
        <h1>Successfully Registered!</h1>
        <p>Check your email for a confirmation code and enter it below! Then, you will be redirected to the sign in
            page.</p>
        <p class="error"><?php echo $error; ?></p>
        <form method="POST">
            <div class="form-group">
                <label for="confNum">Confirmation Code</label>
                <input type="text" class="form-control" name="confNum" id="confNum" placeholder="Code" required>
            </div>

            <button name="submit" type="submit" class="btn btn-outline-dark">Confirm Email</button>
        
        </form>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>