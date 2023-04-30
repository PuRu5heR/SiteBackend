function changePhoto(a) {
    let bg = document.getElementById('background');
    if (a.className == 'small') {
        a.className = 'large';
        bg.style.height = "100vh"
    } else {
        a.className = 'small';
        bg.style.height = "0vh"
    }

}