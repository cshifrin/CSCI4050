<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Manage Books</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<nav class="navbar navbar-expand-sm navbar-light">
    <a class="navbar-brand" href="#">Our Bookstore (Administrator View)</a>
    <ul class="navbar-nav">
        <li class="nav-item"> <a class="nav-link" href="adminprofile.php">Profile</a> </li>
    </ul>
</nav>

<body>
    <div class="main-content">
        <h1><img height="40px" src="css/mb.png"> Update Books</h1>
        <form>
            <div class="form-group">
                <label for="inputSearchManage">Search</label>
                <input class="form-control" id="inputSearchManage" placeholder="ID" required>
            </div>
            <button type="submit" class="btn btn-outline-dark">Search</button>
        </form>
        <br>
        <p>ID (<a href="">edit</a>), Title (<a href="">edit</a>), Author (<a href="">edit</a>), Price (<a href="">edit</a>),
            Publisher (<a href="">edit</a>), Subject (<a href="">edit</a>) - <a href="">DELETE BOOK</a></p>
        <p>ID (<a href="">edit</a>), Title (<a href="">edit</a>), Author (<a href="">edit</a>), Price (<a href="">edit</a>),
            Publisher (<a href="">edit</a>), Subject (<a href="">edit</a>) - <a href="">DELETE BOOK</a></p>
        <p>ID (<a href="">edit</a>), Title (<a href="">edit</a>), Author (<a href="">edit</a>), Price (<a href="">edit</a>),
            Publisher (<a href="">edit</a>), Subject (<a href="">edit</a>) - <a href="">DELETE BOOK</a></p>
    </div>
    <div class="main-content">
        <h1>Add Books</h1>
        <form>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label>ID</label>
                    <input class="form-control" placeholder="123456789">
                </div>
                <div class="form-group col-md-6">
                    <label>Title</label>
                    <input class="form-control" placeholder="Title">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label>Author</label>
                    <input class="form-control" placeholder="Author">
                </div>
                <div class="form-group col-md-6">
                    <label>Price</label>
                    <input class="form-control" placeholder="$$">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-md-6">
                    <label>Publisher</label>
                    <input class="form-control" placeholder="Publisher">
                </div>
                <div class="form-group col-md-6">
                    <label>Subject</label>
                    <input class="form-control" placeholder="Subject">
                </div>
            </div>
            <button type="submit" class="btn btn-outline-dark">Add Book</button>
        </form>
    </div>
</body>

<footer>
        <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
    </footer>
    
</html>