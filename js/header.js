let headImg = document.querySelectorAll('#header_galery img');
let n = headImg.length;

setInterval(imgOpacity, 3000);

function imgOpacity() {
    n--;
    headImg[n].style.opacity = '0';
    if (n == 0) {
        n = headImg.length;
        for (let i = 0; i < headImg.length; i++) {
            headImg[i].style.opacity = '1';
        }
    }

}

let footer = document.querySelector('footer');
footer.innerHTML = "Сайт создан учащимися школы &#171;Cleverland&#187;"