 <style> 
.header{
  padding-left: 41%;
  padding-bottom: 2%;
  background-color: rgb(150, 202, 191) ;
  border-color: black;
  border: 5px;
  border-radius: 10px;
}
.button{
  column-gap: 20px;
  text-align: center;
}

p{
   display: inline;
   
  
}


p:hover{
  color: aliceblue;
  cursor: pointer;
}

.search{
  display: inline;
  margin-top:25px ;
  margin-left:15%;
  input{
    width: 70%;
    padding: 10px;
    border-radius: 5px;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
  }
  .navbar{
  padding-left: 9%;
  display: inline-block;
  cursor: pointer;
  
  
} 
}

.products{
   margin-top: 5%;
    padding-left: 37%;
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
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>
    <br>
    <br>
  <div class="header">
    <nav><h1>ℙ𝔼ℝ𝔽𝕌𝕄𝔼𝕊</h1></nav>
    
      <p class="button">Home|</p>
      <p class="button">Produucts|</p>
      <p class="button">About Us</p>
  </div>
  <br>
  <br>


  <div class="search">
    <input type="search" placeholder="Search"  value="">

    <div class="navbar">
   <i class="fa-solid fa-bars"></i>
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
