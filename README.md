 <style> 
.header{
  padding-left: 44%;
  background-color: rgb(150, 202, 191) ;
  border-color: black;
  border: 5px;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}
.button{
  column-gap: 20px;
  text-align: center;
}

li,ul,h1{
   display: inline;
  
}


li:hover{
  color: aliceblue;
  cursor: pointer;
}

.search{
  margin-top:20px ;
  margin-left:25%;
  input{
    width: 70%;
    padding: 10px;
    border-radius: 5px;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
  }
}

.products{
   margin-top: 5%;
    padding-left: 42%;
}

.box{
  border-color: rgb(0, 0, 0);
  border-width: 2px;
  border-style: solid;
  border-radius: 5px;
  display: inline-block;
  width: 277px;
  cursor: pointer;
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}
.buy{
  padding-left: 35%;
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
    <ul>
      <li class="button">Home|</li>
      <li class="button">Produucts|</li>
      <li class="button">About Us</li>
    </ul>
  </div>
  <div class="search">
    <input type="search" placeholder="Search"  value="">
  </div>

  <div class="products">
    <div class="box">
    <img src="perfume.jpeg">
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad vel nostrum repellat minima quos ex porro, fugiat officia hic sunt, ipsa voluptatem enim vitae tempora temporibus optio necessitatibus nesciunt laudantium.</p>
    <div class="buy">
    <a href="https://wa.me/919342792571"><input type="button" value="BUY NOW"></a>
    </div>
    </div>
  </div>

<div class="products">
    <div class="box">
    <img src="perfume.jpeg">
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
