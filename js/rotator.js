let photo = document.getElementById('photos');
let photos = document.querySelectorAll('#photos > img');
let h = photos.length;
photo.style.width = 840 * h + "px";
let m = 0;
let count = document.getElementById('count');
count.innerText = `1 из ${h}`;

function movePhoto(a) {
    m -= a;
    if (m == 1) { m -= 1; }
    if (m == -h) { m += 1 }
    photo.style.marginLeft = (m * 840) + "px";
    count.innerText = `${-m+1} из ${h}`;
}