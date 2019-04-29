comments_div = document.getElementById("comments_div")
comment_div=document.getElementById("comment")
let commentsArr = []

function listComments(commentsArr) {
    commentsArr.forEach(comment => {
        let div = document.createElement("h4")
        comments_div.appendChild(div)
        div.innerHTML = comment_div.innerHTML
        div .setAttribute("style","width:80%")
        div.getElementsByTagName("span")[0].innerText = comment.text
        div.getElementsByTagName("label")[0].innerText = comment.user
        div.getElementsByTagName('button')[0].addEventListener('click', () => {
            report()
        })

    });
}

function addComment(id,user) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.response)
            console.log(response)
            let condition=commentsArr.filter((elem)=>{
                return elem.id==response.id
            })

            if (condition.length==0){   
                commentsArr.push(response)}
                console.log(commentsArr)
            comments_div.innerHTML=""
            listComments(commentsArr)
        }
    };
    let comment=document.getElementById("comment_body").value
    xhttp.open("POST", `http://127.0.0.1:8000/projects/${id}/comment`);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(`comment=${comment}&user=${user}`)
};