
function rate(projectId,user,rating) {
let div=document.getElementById("rating_div")
  var  current_star = rating-1;
  for (let i = 0; i < 5; i++) {
    let star = div.getElementsByClassName('stars')[i];
    star.addEventListener("click", displayRate);
    star.addEventListener("mouseover", mouseOver);
    star.addEventListener("mouseout", mouseOut);
  }
  function mouseOut() {
    for (let i = 0; i < 5; i++) {
      if (i <= current_star)
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/goldenstar.png";
      else
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/emptystar.png";
    }
  }
  function mouseOver() {
    //displayRate(this);
    // console.log(current_star)
    for (let i = 0; i < 5; i++) {
      if (i <= parseInt(this.getAttribute("id")))
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/goldenstar.png";
      else
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/emptystar.png";
    }
  }
  
  function displayRate() {
  
    current_star = parseInt(this.getAttribute("id"));
    for (let i = 0; i < 5; i++) {
      if (i <= current_star)
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/goldenstar.png";
      else
        div.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/emptystar.png";
    }

    rating_request(projectId);

  }
  
  function rating_request(projectId) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        window.location.reload();
      }
    };
    //get book_id to send it to the route.
  
    xhttp.open("POST", `http://127.0.0.1:8000/projects/${projectId}/rate`);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(`user=${user}&user_rating=${current_star+1}`)
  };
  
}
function retrieve_rate(total_rate) {
    total_rate = Math.abs(Math.round(total_rate));
    for (let i = 0; i < total_rate; i++) {
      document.getElementsByClassName("stars")[i].src = "http://127.0.0.1:8000/static/projects/img/goldenstar.png";
    }
  }