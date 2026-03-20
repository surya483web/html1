 <!DOCTYPE html>
<style>
.header{
  padding-left: 35%;
  background-color: rgb(150, 202, 191) ;
  border-color: black;
  border: 5px;
  border-radius: 10px;
}

.board{
  text-decoration: underline;
  padding-right: 50%;
  margin-bottom: 5%;
}


li,ul,h1{
  display:inline;
}

ul{
  margin-left: 60%;
  .board{
    column-gap: 30%;

  }
}

li:hover{
  color: aliceblue;
  cursor: pointer;
}

.search{
  margin-top:20px ;
  margin-left:20%;
  input{
    width: 80%;
    padding: 6px;
    border-radius: 5px;
  }
}

.products{
   margin-top: 5%;
    padding-left: 29%;
}

.box{
  border-color: rgb(0, 0, 0);
  border-width: 2px;
  border-style: solid;
  border-radius: 5px;
  display: inline-block;
  width: 277px;
  cursor: pointer;
}
.buy{
  padding-left: 30%;
  padding-bottom: 10%;
  cursor: pointer;
}
.buy:hover{
  background-color: rgb(20, 231, 199)
  color rgb(147, 127, 127);
}
.box:hover{
  background-color: gray;
  color: rgb(255, 255, 255);
}

</style>

<html lang="en">
<head>
  <title>Document</title>
</head>
<body>

  <div class="header">
    <nav><h1>ℙ𝔼ℝ𝔽𝕌𝕄𝔼𝕊</h1></nav>
    <ul><div class="board">
      <li>Home|</li>
      <li>Produucts|</li>
      <li>About Us</li>
    </ul>
  </div>
  </div>
  <div class="search">
    <input type="search" placeholder="Search"  value="">
  </div>

  <div class="products">
    <div class="box">
    <img src="C:\Users\Admin\Documents\html begining\perfume.jpeg">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad vel nostrum repellat minima quos ex porro, fugiat officia hic sunt, ipsa voluptatem enim vitae tempora temporibus optio necessitatibus nesciunt laudantium.</p>
    <div class="buy">
    <a href="https://wa.me/919342792571"><input type="button" value="BUY NOW"></a>
    </div>
    </div>
  </div>

<div class="products">
    <div class="box">
    <img src="C:\Users\Admin\Documents\html begining\perfume.jpeg">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad vel nostrum repellat minima quos ex porro, fugiat officia hic sunt, ipsa voluptatem enim vitae tempora temporibus optio necessitatibus nesciunt laudantium.</p>
    <div class="buy">
    <a href="https://wa.me/919342792571"><input type="button" value="BUY NOW"></a>
    </div>
    </div>
  </div>

  <div class="about">
  </div>
  <div class="contact">

  </div>
</body>
</html>
